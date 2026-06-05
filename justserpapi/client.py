"""High-level JustSerpAPI client generated from OpenAPI."""

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
        allowed_methods=frozenset({
            "DELETE",
            "GET",
            "HEAD",
            "OPTIONS",
            "PUT",
            "TRACE",
        }),
        respect_retry_after_header=True,
    )


class _BaseResource:
    def __init__(self, api: Any, timeout: TimeoutValue) -> None:
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


class GoogleAIResource(_BaseResource):
    def mode(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google AI Mode API."""
        return self._json_call(
            "ai_mode",
            query=query,
            **kwargs,
        )

    def overview(
        self,
        *,
        url: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google AI Overview API."""
        return self._json_call(
            "ai_overview",
            url=url,
            **kwargs,
        )


class GoogleFinanceResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Finance Search API."""
        return self._json_call(
            "finance_search",
            query=query,
            **kwargs,
        )


class GoogleHotelsResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        check_in_date: Any,
        check_out_date: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Hotels Search API."""
        return self._json_call(
            "hotels_search",
            query=query,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            **kwargs,
        )


class GoogleImagesResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Images Search API."""
        return self._json_call(
            "images_search",
            query=query,
            **kwargs,
        )


class GoogleImmersiveResource(_BaseResource):
    def product(
        self,
        *,
        page_token: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Immersive Product API."""
        return self._json_call(
            "immersive_product",
            page_token=page_token,
            **kwargs,
        )


class GoogleJobsResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Jobs Search API."""
        return self._json_call(
            "jobs_search",
            query=query,
            **kwargs,
        )


class GoogleLocalResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Local Search API."""
        return self._json_call(
            "local_search",
            query=query,
            **kwargs,
        )


class GoogleMapsResource(_BaseResource):
    def photos(
        self,
        *,
        data_id: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Maps Photos API."""
        return self._json_call(
            "maps_photos",
            data_id=data_id,
            **kwargs,
        )

    def places(self, **kwargs: Any) -> JSONDict:
        """Google Maps Places API."""
        return self._json_call("maps_places", **kwargs)

    def posts(
        self,
        *,
        data_id: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Maps Posts API."""
        return self._json_call(
            "maps_posts",
            data_id=data_id,
            **kwargs,
        )

    def reviews(
        self,
        *,
        data_id: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Maps Reviews API."""
        return self._json_call(
            "maps_reviews",
            data_id=data_id,
            **kwargs,
        )

    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Maps Search API."""
        return self._json_call(
            "maps_search",
            query=query,
            **kwargs,
        )


class GoogleNewsResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google News Search API."""
        return self._json_call(
            "news_search",
            query=query,
            **kwargs,
        )


class GooglePatentsResource(_BaseResource):
    def details(
        self,
        *,
        patent_id: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Patents Details API."""
        return self._json_call(
            "patent_details",
            patent_id=patent_id,
            **kwargs,
        )

    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Patents Search API."""
        return self._json_call(
            "patent_search",
            query=query,
            **kwargs,
        )


class GoogleScholarCiteResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Scholar Cite Search API."""
        return self._json_call(
            "scholar_cite_search",
            query=query,
            **kwargs,
        )


class GoogleScholarResource(_BaseResource):
    def __init__(self, api: Any, timeout: TimeoutValue) -> None:
        super().__init__(api=api, timeout=timeout)
        self.cite = GoogleScholarCiteResource(api, timeout)

    def author(
        self,
        *,
        author_id: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Scholar Author API."""
        return self._json_call(
            "scholar_author",
            author_id=author_id,
            **kwargs,
        )

    def profiles(
        self,
        *,
        mauthors: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Scholar Profiles API."""
        return self._json_call(
            "scholar_profiles",
            mauthors=mauthors,
            **kwargs,
        )

    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Scholar Search API."""
        return self._json_call(
            "scholar_search",
            query=query,
            **kwargs,
        )


class GoogleSearchResource(_BaseResource):
    def __call__(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Search API."""
        return self._json_call(
            "search",
            query=query,
            **kwargs,
        )

    def light(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Light Search API."""
        return self._json_call(
            "search_light",
            query=query,
            **kwargs,
        )

    def mobile(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Mobile Search API."""
        return self._json_call(
            "search_mobile",
            query=query,
            **kwargs,
        )


class GoogleShoppingResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Shopping Search API."""
        return self._json_call(
            "shopping_search",
            query=query,
            **kwargs,
        )


class GoogleShortsResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Shorts Search API."""
        return self._json_call(
            "shorts_search",
            query=query,
            **kwargs,
        )


class GoogleTrendsResource(_BaseResource):
    def autocomplete(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Trends Autocomplete API."""
        return self._json_call(
            "trends_autocomplete",
            query=query,
            **kwargs,
        )

    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Trends Search API."""
        return self._json_call(
            "trends_search",
            query=query,
            **kwargs,
        )

    def trending_now(
        self,
        *,
        geo: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Trends Trending Now API."""
        return self._json_call(
            "trends_trending_now",
            geo=geo,
            **kwargs,
        )


class GoogleVideosResource(_BaseResource):
    def search(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Videos Search API."""
        return self._json_call(
            "videos_search",
            query=query,
            **kwargs,
        )


class GoogleResource(_BaseResource):
    def __init__(self, api: Any, timeout: TimeoutValue) -> None:
        super().__init__(api=api, timeout=timeout)
        self.ai = GoogleAIResource(api, timeout)
        self.finance = GoogleFinanceResource(api, timeout)
        self.hotels = GoogleHotelsResource(api, timeout)
        self.images = GoogleImagesResource(api, timeout)
        self.immersive = GoogleImmersiveResource(api, timeout)
        self.jobs = GoogleJobsResource(api, timeout)
        self.local = GoogleLocalResource(api, timeout)
        self.maps = GoogleMapsResource(api, timeout)
        self.news = GoogleNewsResource(api, timeout)
        self.patents = GooglePatentsResource(api, timeout)
        self.scholar = GoogleScholarResource(api, timeout)
        self.search = GoogleSearchResource(api, timeout)
        self.shopping = GoogleShoppingResource(api, timeout)
        self.shorts = GoogleShortsResource(api, timeout)
        self.trends = GoogleTrendsResource(api, timeout)
        self.videos = GoogleVideosResource(api, timeout)

    def autocomplete(
        self,
        *,
        query: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Autocomplete API."""
        return self._json_call(
            "autocomplete",
            query=query,
            **kwargs,
        )

    def lens(
        self,
        *,
        url: Any,
        **kwargs: Any,
    ) -> JSONDict:
        """Google Lens API."""
        return self._json_call(
            "lens",
            url=url,
            **kwargs,
        )


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
        self.google = GoogleResource(GoogleAPIApi(self.api_client), timeout)

    def close(self) -> None:
        close = getattr(self.api_client, "close", None)
        if callable(close):
            close()
            return

        rest_client = getattr(self.api_client, "rest_client", None)
        pool_manager = getattr(rest_client, "pool_manager", None)
        if pool_manager is not None:
            pool_manager.clear()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()


JustSerpAPI = Client
