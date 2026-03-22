import unittest
from unittest.mock import patch
from typing import Any, Dict

from urllib3.util.retry import Retry

import justserpapi
from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.client import default_retry_strategy


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
    def test_google_search_uses_default_timeout_and_returns_json_dict(self) -> None:
        payload: Dict[str, Any] = {
            "code": 200,
            "message": "ok",
            "data": {
                "organic_results": [{"title": "Coffee", "link": "https://example.com"}],
            },
        }

        with patch.object(GoogleAPIApi, "search", return_value=payload) as search_mock:
            with justserpapi.Client(api_key="test-api-key", timeout=12.5) as client:
                response = client.google.search(query="coffee")

        self.assertIsInstance(response, dict)
        self.assertEqual("Coffee", response["data"]["organic_results"][0]["title"])
        search_mock.assert_called_once()
        self.assertEqual(12.5, search_mock.call_args.kwargs["_request_timeout"])

    def test_nested_google_resources_return_json_dicts(self) -> None:
        maps_payload = {"code": 200, "data": {"local_results": [{"title": "Cafe", "place_id": "abc"}]}}
        news_payload = {"code": 200, "data": {"news_results": [{"title": "Headline", "link": "https://example.com"}]}}
        images_payload = {"code": 200, "data": {"images_results": [{"title": "Cup", "image": "https://example.com/cup.jpg"}]}}
        shopping_payload = {"code": 200, "data": {"shopping_results": [{"title": "Grinder", "price": "$20"}]}}
        autocomplete_payload = {"code": 200, "data": {"suggestions": [{"value": "coffee shops"}]}}
        ai_payload = {"code": 200, "data": {"answer": "Coffee shops are local businesses."}}

        with patch.object(GoogleAPIApi, "maps_search", return_value=maps_payload):
            with patch.object(GoogleAPIApi, "news_search", return_value=news_payload):
                with patch.object(GoogleAPIApi, "images_search", return_value=images_payload):
                    with patch.object(GoogleAPIApi, "shopping_search", return_value=shopping_payload):
                        with patch.object(GoogleAPIApi, "autocomplete", return_value=autocomplete_payload):
                            with patch.object(GoogleAPIApi, "ai_overview", return_value=ai_payload):
                                with justserpapi.Client(api_key="test-api-key") as client:
                                    maps = client.google.maps.search(query="coffee")
                                    news = client.google.news.search(query="coffee")
                                    images = client.google.images.search(query="coffee")
                                    shopping = client.google.shopping.search(query="coffee")
                                    autocomplete = client.google.autocomplete(query="coffee")
                                    overview = client.google.ai.overview(url="https://example.com")

        self.assertIsInstance(maps, dict)
        self.assertEqual("Cafe", maps["data"]["local_results"][0]["title"])
        self.assertIsInstance(news, dict)
        self.assertEqual("Headline", news["data"]["news_results"][0]["title"])
        self.assertIsInstance(images, dict)
        self.assertEqual("Cup", images["data"]["images_results"][0]["title"])
        self.assertIsInstance(shopping, dict)
        self.assertEqual("Grinder", shopping["data"]["shopping_results"][0]["title"])
        self.assertIsInstance(autocomplete, dict)
        self.assertEqual("coffee shops", autocomplete["data"]["suggestions"][0]["value"])
        self.assertIsInstance(overview, dict)
        self.assertEqual("Coffee shops are local businesses.", overview["data"]["answer"])


if __name__ == "__main__":
    unittest.main()
