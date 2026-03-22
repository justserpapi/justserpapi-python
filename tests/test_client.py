import unittest
from unittest.mock import patch

from urllib3.util.retry import Retry

import justserpapi
from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.client import default_retry_strategy
from justserpapi.models import (
    GoogleImagesSearchResponse,
    GoogleMapsSearchResponse,
    GoogleNewsSearchResponse,
    GoogleSearchResponse,
    GoogleShoppingSearchResponse,
)


class ClientConfigurationTest(unittest.TestCase):
    def test_client_sets_common_configuration(self) -> None:
        client = justserpapi.Client(api_key="test-api-key")
        try:
            self.assertEqual("test-api-key", client.configuration.api_key["ApiKeyAuth"])
            self.assertIsInstance(client.configuration.retries, Retry)
            self.assertEqual(
                default_retry_strategy().total,
                client.configuration.retries.total,
            )
            self.assertEqual(
                "justserpapi/%s/python" % justserpapi.__version__,
                client.api_client.default_headers["User-Agent"],
            )
        finally:
            client.close()

    def test_client_preserves_custom_retry_object(self) -> None:
        retries = Retry(total=5, backoff_factor=1)
        client = justserpapi.Client(api_key="test-api-key", retries=retries)
        try:
            self.assertIs(retries, client.configuration.retries)
        finally:
            client.close()


class ClientDelegationTest(unittest.TestCase):
    def test_google_search_uses_default_timeout_and_returns_typed_model(self) -> None:
        payload = {
            "search_metadata": {"status": "Success"},
            "organic_results": [{"title": "Coffee", "link": "https://example.com"}],
        }

        with patch.object(GoogleAPIApi, "search", return_value=payload) as search_mock:
            with justserpapi.Client(api_key="test-api-key", timeout=12.5) as client:
                response = client.google.search(query="coffee")

        self.assertIsInstance(response, GoogleSearchResponse)
        self.assertEqual("Coffee", response.organic_results[0].title)
        search_mock.assert_called_once()
        self.assertEqual(12.5, search_mock.call_args.kwargs["_request_timeout"])

    def test_nested_google_resources_return_typed_models(self) -> None:
        maps_payload = {"local_results": [{"title": "Cafe", "place_id": "abc"}]}
        news_payload = {"news_results": [{"title": "Headline", "link": "https://example.com"}]}
        images_payload = {"images_results": [{"title": "Cup", "image": "https://example.com/cup.jpg"}]}
        shopping_payload = {"shopping_results": [{"title": "Grinder", "price": "$20"}]}

        with patch.object(GoogleAPIApi, "maps_search", return_value=maps_payload):
            with patch.object(GoogleAPIApi, "news_search", return_value=news_payload):
                with patch.object(GoogleAPIApi, "images_search", return_value=images_payload):
                    with patch.object(GoogleAPIApi, "shopping_search", return_value=shopping_payload):
                        with justserpapi.Client(api_key="test-api-key") as client:
                            maps = client.google.maps.search(query="coffee")
                            news = client.google.news.search(query="coffee")
                            images = client.google.images.search(query="coffee")
                            shopping = client.google.shopping.search(query="coffee")

        self.assertIsInstance(maps, GoogleMapsSearchResponse)
        self.assertIsInstance(news, GoogleNewsSearchResponse)
        self.assertIsInstance(images, GoogleImagesSearchResponse)
        self.assertIsInstance(shopping, GoogleShoppingSearchResponse)


if __name__ == "__main__":
    unittest.main()
