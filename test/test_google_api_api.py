# coding: utf-8

import unittest

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.exceptions import UnauthorizedException
from justserpapi.rest import RESTResponse


class _DummyHTTPResponse:
    def __init__(self, *, status: int, data: bytes, headers: dict[str, str], reason: str) -> None:
        self.status = status
        self.data = data
        self.headers = headers
        self.reason = reason


class TestGoogleAPIApi(unittest.TestCase):
    def setUp(self) -> None:
        configuration = Configuration(host="https://api.justserpapi.com")
        configuration.api_key["ApiKeyAuth"] = "test-api-key"
        self.api_client = ApiClient(configuration)
        self.api = GoogleAPIApi(self.api_client)

    def tearDown(self) -> None:
        self.api_client.close()

    def test_search_serialization_includes_auth_header_and_query_params(self) -> None:
        method, url, headers, body, post_params = self.api._search_serialize(  # pylint: disable=protected-access
            query="coffee shops",
            page=1,
            language="en",
            _headers={},
            _request_auth=None,
            _content_type=None,
            _host_index=0,
        )

        self.assertEqual("GET", method)
        self.assertIn("/api/v1/google/search", url)
        self.assertIn("query=coffee%20shops", url)
        self.assertIn("page=1", url)
        self.assertEqual("test-api-key", headers["X-API-Key"])
        self.assertEqual([], post_params)
        self.assertIsNone(body)

    def test_response_deserialize_raises_typed_error_for_401(self) -> None:
        response = RESTResponse(
            _DummyHTTPResponse(
                status=401,
                reason="Unauthorized",
                data=b'{"message":"missing api key"}',
                headers={"content-type": "application/json"},
            )
        )
        response.read()

        with self.assertRaises(UnauthorizedException) as exc_info:
            self.api_client.response_deserialize(
                response_data=response,
                response_types_map={"401": "object"},
            )

        self.assertEqual(401, exc_info.exception.status)
        self.assertEqual({"message": "missing api key"}, exc_info.exception.data)


if __name__ == "__main__":
    unittest.main()
