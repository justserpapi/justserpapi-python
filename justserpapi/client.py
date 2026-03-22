"""High-level JustSerpAPI client with stable entrypoints."""

from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, Union

from urllib3.util.retry import Retry

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration

TimeoutValue = Optional[Union[float, Tuple[float, float]]]
JSONDict = Dict[str, Any]

DEFAULT_HOST = "https://api.justserpapi.com"
DEFAULT_TIMEOUT: TimeoutValue = 30.0


def default_retry_strategy() -> Retry:
    """Return the SDK's default retry strategy."""

    return Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=0.2,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"DELETE", "GET", "HEAD", "OPTIONS", "PUT", "TRACE"}),
        respect_retry_after_header=True,
    )


class _GoogleBaseResource:
    def __init__(self, api: GoogleAPIApi, timeout: TimeoutValue) -> None:
        self._api = api
        self._timeout = timeout

    def _with_timeout(self, kwargs: dict[str, Any]) -> dict[str, Any]:
        if "_request_timeout" not in kwargs and self._timeout is not None:
            kwargs["_request_timeout"] = self._timeout
        return kwargs

    def _json_call(self, method_name: str, **kwargs: Any) -> JSONDict:
        payload = getattr(self._api, method_name)(**self._with_timeout(kwargs))
        if isinstance(payload, dict):
            return payload
        raise TypeError(
            "%s returned %s instead of a JSON object."
            % (method_name, type(payload).__name__)
        )


class GoogleMapsResource(_GoogleBaseResource):
    def search(self, *, query: str, **kwargs: Any) -> JSONDict:
        return self._json_call("maps_search", query=query, **kwargs)


class GoogleNewsResource(_GoogleBaseResource):
    def search(self, *, query: str, **kwargs: Any) -> JSONDict:
        return self._json_call("news_search", query=query, **kwargs)


class GoogleImagesResource(_GoogleBaseResource):
    def search(self, *, query: str, **kwargs: Any) -> JSONDict:
        return self._json_call("images_search", query=query, **kwargs)


class GoogleShoppingResource(_GoogleBaseResource):
    def search(self, *, query: str, **kwargs: Any) -> JSONDict:
        return self._json_call("shopping_search", query=query, **kwargs)


class GoogleAIResource(_GoogleBaseResource):
    def overview(self, *, url: str, **kwargs: Any) -> JSONDict:
        return self._json_call("ai_overview", url=url, **kwargs)

    def mode(self, *, query: str, **kwargs: Any) -> JSONDict:
        return self._json_call("ai_mode", query=query, **kwargs)


class GoogleResource(_GoogleBaseResource):
    """Promoted Google entrypoints."""

    def __init__(self, api_client: ApiClient, timeout: TimeoutValue) -> None:
        api = GoogleAPIApi(api_client)
        super().__init__(api=api, timeout=timeout)
        self.maps = GoogleMapsResource(api, timeout)
        self.news = GoogleNewsResource(api, timeout)
        self.images = GoogleImagesResource(api, timeout)
        self.shopping = GoogleShoppingResource(api, timeout)
        self.ai = GoogleAIResource(api, timeout)

    def search(self, *, query: str, **kwargs: Any) -> JSONDict:
        return self._json_call("search", query=query, **kwargs)

    def autocomplete(self, *, query: str, **kwargs: Any) -> JSONDict:
        return self._json_call("autocomplete", query=query, **kwargs)


class Client:
    """High-level JustSerpAPI SDK entrypoint."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: str = DEFAULT_HOST,
        timeout: TimeoutValue = DEFAULT_TIMEOUT,
        retries: Optional[Union[int, Retry]] = None,
        configuration: Optional[Configuration] = None,
    ) -> None:
        if configuration is None:
            configuration = Configuration(
                host=base_url,
                retries=default_retry_strategy() if retries is None else retries,
            )
        else:
            if base_url != DEFAULT_HOST:
                configuration.host = base_url
            if retries is not None:
                configuration.retries = retries
            elif configuration.retries is None:
                configuration.retries = default_retry_strategy()

        if api_key is not None:
            configuration.api_key["ApiKeyAuth"] = api_key

        self.configuration = configuration
        self.api_client = ApiClient(configuration)
        self.google = GoogleResource(self.api_client, timeout)

    def close(self) -> None:
        close = getattr(self.api_client, "close", None)
        if callable(close):
            close()
            return

        pool_manager = getattr(getattr(self.api_client, "rest_client", None), "pool_manager", None)
        if pool_manager is not None:
            pool_manager.clear()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()


JustSerpAPI = Client
