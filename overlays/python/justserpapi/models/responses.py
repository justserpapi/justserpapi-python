"""Typed response models for the promoted high-level SDK surface."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class BasePayloadModel(BaseModel):
    """Permissive base model for partially typed API payloads."""

    model_config = ConfigDict(extra="allow")


class SearchMetadata(BasePayloadModel):
    id: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    processed_at: Optional[str] = None
    raw_html_file: Optional[str] = None


class Pagination(BasePayloadModel):
    current: Optional[int] = None
    next: Optional[str] = None
    next_page_token: Optional[str] = None
    previous: Optional[str] = None


class OrganicResult(BasePayloadModel):
    title: Optional[str] = None
    link: Optional[str] = None
    snippet: Optional[str] = None
    position: Optional[int] = None


class PlaceResult(BasePayloadModel):
    title: Optional[str] = None
    place_id: Optional[str] = None
    address: Optional[str] = None
    rating: Optional[float] = None
    reviews: Optional[int] = None


class ImageResult(BasePayloadModel):
    title: Optional[str] = None
    image: Optional[str] = None
    source: Optional[str] = None
    link: Optional[str] = None


class NewsResult(BasePayloadModel):
    title: Optional[str] = None
    link: Optional[str] = None
    source: Optional[str] = None
    published: Optional[str] = None
    snippet: Optional[str] = None


class ShoppingResult(BasePayloadModel):
    title: Optional[str] = None
    link: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    rating: Optional[float] = None


class AutocompleteSuggestion(BasePayloadModel):
    value: Optional[str] = None
    score: Optional[float] = None


class BaseSearchResponse(BasePayloadModel):
    search_metadata: Optional[SearchMetadata] = None
    pagination: Optional[Pagination] = None
    request_info: Optional[Dict[str, Any]] = None


class GoogleSearchResponse(BaseSearchResponse):
    organic_results: List[OrganicResult] = Field(default_factory=list)
    related_searches: List[Dict[str, Any]] = Field(default_factory=list)
    ads: List[Dict[str, Any]] = Field(default_factory=list)


class GoogleMapsSearchResponse(BaseSearchResponse):
    local_results: List[PlaceResult] = Field(default_factory=list)
    places_results: List[PlaceResult] = Field(default_factory=list)


class GoogleNewsSearchResponse(BaseSearchResponse):
    news_results: List[NewsResult] = Field(default_factory=list)


class GoogleImagesSearchResponse(BaseSearchResponse):
    images_results: List[ImageResult] = Field(default_factory=list)


class GoogleShoppingSearchResponse(BaseSearchResponse):
    shopping_results: List[ShoppingResult] = Field(default_factory=list)


class GoogleAIOverviewResponse(BasePayloadModel):
    title: Optional[str] = None
    answer: Optional[str] = None
    sources: List[Dict[str, Any]] = Field(default_factory=list)


class GoogleAutocompleteResponse(BasePayloadModel):
    suggestions: List[AutocompleteSuggestion] = Field(default_factory=list)
