# justserpapi.api.google_api_api.GoogleAPIApi

Internal generated reference for the Google API surface. New integrations should use `justserpapi.Client`; this document only describes the underlying generated module.

All URIs are relative to *https://api.justserpapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_mode**](GoogleAPIApi.md#ai_mode) | **GET** /api/v1/google/ai-mode | Google AI Mode API
[**ai_overview**](GoogleAPIApi.md#ai_overview) | **GET** /api/v1/google/ai-overview | Google AI Overview API
[**autocomplete**](GoogleAPIApi.md#autocomplete) | **GET** /api/v1/google/autocomplete | Google Autocomplete API
[**finance_search**](GoogleAPIApi.md#finance_search) | **GET** /api/v1/google/finance/search | Google Finance Search API
[**hotels_search**](GoogleAPIApi.md#hotels_search) | **GET** /api/v1/google/hotels/search | Google Hotels Search API
[**images_search**](GoogleAPIApi.md#images_search) | **GET** /api/v1/google/images/search | Google Images Search API
[**immersive_product**](GoogleAPIApi.md#immersive_product) | **GET** /api/v1/google/immersive/product | Google Immersive Product API
[**jobs_search**](GoogleAPIApi.md#jobs_search) | **GET** /api/v1/google/jobs/search | Google Jobs Search API
[**lens**](GoogleAPIApi.md#lens) | **GET** /api/v1/google/lens | Google Lens API
[**local_search**](GoogleAPIApi.md#local_search) | **GET** /api/v1/google/local/search | Google Local Search API
[**maps_photos**](GoogleAPIApi.md#maps_photos) | **GET** /api/v1/google/maps/photos | Google Maps Photos API
[**maps_places**](GoogleAPIApi.md#maps_places) | **GET** /api/v1/google/maps/places | Google Maps Places API
[**maps_posts**](GoogleAPIApi.md#maps_posts) | **GET** /api/v1/google/maps/posts | Google Maps Posts API
[**maps_reviews**](GoogleAPIApi.md#maps_reviews) | **GET** /api/v1/google/maps/reviews | Google Maps Reviews API
[**maps_search**](GoogleAPIApi.md#maps_search) | **GET** /api/v1/google/maps/search | Google Maps Search API
[**news_search**](GoogleAPIApi.md#news_search) | **GET** /api/v1/google/news/search | Google News Search API
[**patent_details**](GoogleAPIApi.md#patent_details) | **GET** /api/v1/google/patents/details | Google Patents Details API
[**patent_search**](GoogleAPIApi.md#patent_search) | **GET** /api/v1/google/patents/search | Google Patents Search API
[**scholar_author**](GoogleAPIApi.md#scholar_author) | **GET** /api/v1/google/scholar/author | Google Scholar Author API
[**scholar_cite_search**](GoogleAPIApi.md#scholar_cite_search) | **GET** /api/v1/google/scholar/cite/search | Google Scholar Cite Search API
[**scholar_profiles**](GoogleAPIApi.md#scholar_profiles) | **GET** /api/v1/google/scholar/profiles | Google Scholar Profiles API
[**scholar_search**](GoogleAPIApi.md#scholar_search) | **GET** /api/v1/google/scholar/search | Google Scholar Search API
[**search**](GoogleAPIApi.md#search) | **GET** /api/v1/google/search | Google Search API
[**search_light**](GoogleAPIApi.md#search_light) | **GET** /api/v1/google/search/light | Google Light Search API
[**search_mobile**](GoogleAPIApi.md#search_mobile) | **GET** /api/v1/google/search/mobile | Google Mobile Search API
[**shopping_search**](GoogleAPIApi.md#shopping_search) | **GET** /api/v1/google/shopping/search | Google Shopping Search API
[**shorts_search**](GoogleAPIApi.md#shorts_search) | **GET** /api/v1/google/shorts/search | Google Shorts Search API
[**trends_autocomplete**](GoogleAPIApi.md#trends_autocomplete) | **GET** /api/v1/google/trends/autocomplete | Google Trends Autocomplete API
[**trends_search**](GoogleAPIApi.md#trends_search) | **GET** /api/v1/google/trends/search | Google Trends Search API
[**trends_trending_now**](GoogleAPIApi.md#trends_trending_now) | **GET** /api/v1/google/trends/trending-now | Google Trends Trending Now API
[**videos_search**](GoogleAPIApi.md#videos_search) | **GET** /api/v1/google/videos/search | Google Videos Search API


# **ai_mode**
> object ai_mode(query, html=html, country=country, uule=uule, location=location, safe=safe)

Google AI Mode API

Access Google's AI-powered search mode with our specialized API. Get structured AI overviews and conversational search results with high speed and reliability.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google Search (e.g., 'coffee shops', 'how to bake a cake').
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    location = 'location_example' # str | The textual location name (e.g., 'New York, NY') to localize the search results. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)

    try:
        # Google AI Mode API
        api_response = api_instance.ai_mode(query, html=html, country=country, uule=uule, location=location, safe=safe)
        print("The response of GoogleAPIApi->ai_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->ai_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google Search (e.g., &#39;coffee shops&#39;, &#39;how to bake a cake&#39;). | 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **location** | **str**| The textual location name (e.g., &#39;New York, NY&#39;) to localize the search results. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_overview**
> object ai_overview(url)

Google AI Overview API

Scrape Google's AI-generated search overviews with our Google AI Overview API. Get structured insights and summaries directly from Google's generative search experience.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    url = 'url_example' # str | The unique URL generated by Google to access the AI Overview. This URL is typically extracted from the 'ai_overview_url' field in a <a href=\"/reference/google/search\">Google Search API</a> response. Note: This URL is transient and usually expires within 2 minutes.

    try:
        # Google AI Overview API
        api_response = api_instance.ai_overview(url)
        print("The response of GoogleAPIApi->ai_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->ai_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The unique URL generated by Google to access the AI Overview. This URL is typically extracted from the &#39;ai_overview_url&#39; field in a &lt;a href&#x3D;\&quot;/reference/google/search\&quot;&gt;Google Search API&lt;/a&gt; response. Note: This URL is transient and usually expires within 2 minutes. | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete**
> object autocomplete(query, country=country, language=language)

Google Autocomplete API

Powerful Google Autocomplete API to fetch real-time search suggestions. Ideal for keyword discovery, SEO optimization, and improving user search experience.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query to get autocomplete suggestions for. As you type, Google provides real-time predictions based on popular searches.
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)

    try:
        # Google Autocomplete API
        api_response = api_instance.autocomplete(query, country=country, language=language)
        print("The response of GoogleAPIApi->autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query to get autocomplete suggestions for. As you type, Google provides real-time predictions based on popular searches. | 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finance_search**
> object finance_search(query, html=html, language=language)

Google Finance Search API

Scrape real-time stock market data, financial news, and currency exchange rates with our Google Finance Search SERP API. Get structured financial information directly from Google Finance with high reliability.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The stock symbol, company name, or index you want to search for on Google Finance (e.g., 'AAPL', 'Tesla', 'S&P 500').
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)

    try:
        # Google Finance Search API
        api_response = api_instance.finance_search(query, html=html, language=language)
        print("The response of GoogleAPIApi->finance_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->finance_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The stock symbol, company name, or index you want to search for on Google Finance (e.g., &#39;AAPL&#39;, &#39;Tesla&#39;, &#39;S&amp;P 500&#39;). | 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_search**
> object hotels_search(query, check_in_date, check_out_date, next_page_token=next_page_token, adults=adults, children=children, children_ages=children_ages, html=html, language=language, country=country, currency=currency, sort_by=sort_by, min_price=min_price, max_price=max_price, property_types=property_types, amenities=amenities, rating=rating, brands=brands, hotel_class=hotel_class, free_cancellation=free_cancellation, special_offers=special_offers, eco_certified=eco_certified, vacation_rentals=vacation_rentals, bedrooms=bedrooms, bathrooms=bathrooms, property_token=property_token)

Google Hotels Search API

Scrape hotel listings, prices, ratings, and availability with our Google Hotels Search API. Get structured travel data for competitive analysis and booking insights.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The destination or specific hotel name you are searching for (e.g., 'Paris', 'Hilton New York').
    check_in_date = 'check_in_date_example' # str | The hotel check-in date in 'YYYY-MM-DD' format (e.g., '2026-05-20').
    check_out_date = 'check_out_date_example' # str | The hotel check-out date in 'YYYY-MM-DD' format (e.g., '2026-05-25').
    next_page_token = 'next_page_token_example' # str | The token used to retrieve the next page of hotel results. This token is found in the 'next_page_token' field of a previous response. (optional)
    adults = 2 # int | The number of adults staying in the room. (optional)
    children = 0 # int | The number of children staying in the room. (optional)
    children_ages = 'children_ages_example' # str | The ages of the children, separated by commas (e.g., '5,10'). The number of ages must match the 'children' parameter. (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    currency = 'USD' # str | The three-letter ISO currency code for displaying prices (e.g., 'USD', 'EUR'). See <a href=\"/reference/hotels/google-hotels-currency\">Google Hotels Currency</a>. (optional)
    sort_by = 'sort_by_example' # str | The criteria to sort hotel results. Supported values: '3' (Lowest price), '8' (Highest rating), '13' (Most reviews). (optional)
    min_price = 'min_price_example' # str | Minimum price filter for the hotel stay. (optional)
    max_price = 'max_price_example' # str | Maximum price filter for the hotel stay. (optional)
    property_types = 'property_types_example' # str | Filter by hotel property types. See the <a href=\"/reference/hotels/google-hotels-property-types\">Google Property Types</a> for the full list of supported hotel property types. For vacation rentals, refer to the <a href=\"/reference/hotels/google-hotels-vacation-rentals-property-types\">Google Hotels Vacation Rentals Property Types</a>. (optional)
    amenities = 'amenities_example' # str | Filter by specific amenities (e.g., '35' for free Wi-Fi). <a href=\"/reference/hotels/google-hotels-amenities\">Google Hotels Amenities</a> (hotel amenities). <a href=\"/reference/hotels/google-hotels-vacation-rentals-amenities\">Google Hotels Vacation Rentals Amenities</a> (vacation rental amenities) (optional)
    rating = 'rating_example' # str | Filter by minimum guest rating. Supported values: '7' (3.5+), '8' (4.0+), '9' (4.5+). (optional)
    brands = 'brands_example' # str | Filter by specific hotel brand IDs. IDs can be comma-separated. (optional)
    hotel_class = 'hotel_class_example' # str | Filter by hotel star ratings. Supported values: '2', '3', '4', '5'. Can be comma-separated. (optional)
    free_cancellation = 'free_cancellation_example' # str | Filter for hotels that offer free cancellation. Set to '1' or 'true' to enable. (optional)
    special_offers = 'special_offers_example' # str | Filter for hotels currently offering special deals or discounts. Set to '1' or 'true' to enable. (optional)
    eco_certified = 'eco_certified_example' # str | Filter for hotels that are eco-certified. Set to '1' or 'true' to enable. (optional)
    vacation_rentals = False # bool | Set to true to search for vacation rentals instead of standard hotels. (optional)
    bedrooms = 'bedrooms_example' # str | Minimum number of bedrooms required (applies to vacation rentals). (optional)
    bathrooms = 'bathrooms_example' # str | Minimum number of bathrooms required (applies to vacation rentals). (optional)
    property_token = 'property_token_example' # str | The unique token for a specific hotel property to fetch detailed information. (optional)

    try:
        # Google Hotels Search API
        api_response = api_instance.hotels_search(query, check_in_date, check_out_date, next_page_token=next_page_token, adults=adults, children=children, children_ages=children_ages, html=html, language=language, country=country, currency=currency, sort_by=sort_by, min_price=min_price, max_price=max_price, property_types=property_types, amenities=amenities, rating=rating, brands=brands, hotel_class=hotel_class, free_cancellation=free_cancellation, special_offers=special_offers, eco_certified=eco_certified, vacation_rentals=vacation_rentals, bedrooms=bedrooms, bathrooms=bathrooms, property_token=property_token)
        print("The response of GoogleAPIApi->hotels_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->hotels_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The destination or specific hotel name you are searching for (e.g., &#39;Paris&#39;, &#39;Hilton New York&#39;). | 
 **check_in_date** | **str**| The hotel check-in date in &#39;YYYY-MM-DD&#39; format (e.g., &#39;2026-05-20&#39;). | 
 **check_out_date** | **str**| The hotel check-out date in &#39;YYYY-MM-DD&#39; format (e.g., &#39;2026-05-25&#39;). | 
 **next_page_token** | **str**| The token used to retrieve the next page of hotel results. This token is found in the &#39;next_page_token&#39; field of a previous response. | [optional] 
 **adults** | **int**| The number of adults staying in the room. | [optional] 
 **children** | **int**| The number of children staying in the room. | [optional] 
 **children_ages** | **str**| The ages of the children, separated by commas (e.g., &#39;5,10&#39;). The number of ages must match the &#39;children&#39; parameter. | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **currency** | **str**| The three-letter ISO currency code for displaying prices (e.g., &#39;USD&#39;, &#39;EUR&#39;). See &lt;a href&#x3D;\&quot;/reference/hotels/google-hotels-currency\&quot;&gt;Google Hotels Currency&lt;/a&gt;. | [optional] 
 **sort_by** | **str**| The criteria to sort hotel results. Supported values: &#39;3&#39; (Lowest price), &#39;8&#39; (Highest rating), &#39;13&#39; (Most reviews). | [optional] 
 **min_price** | **str**| Minimum price filter for the hotel stay. | [optional] 
 **max_price** | **str**| Maximum price filter for the hotel stay. | [optional] 
 **property_types** | **str**| Filter by hotel property types. See the &lt;a href&#x3D;\&quot;/reference/hotels/google-hotels-property-types\&quot;&gt;Google Property Types&lt;/a&gt; for the full list of supported hotel property types. For vacation rentals, refer to the &lt;a href&#x3D;\&quot;/reference/hotels/google-hotels-vacation-rentals-property-types\&quot;&gt;Google Hotels Vacation Rentals Property Types&lt;/a&gt;. | [optional] 
 **amenities** | **str**| Filter by specific amenities (e.g., &#39;35&#39; for free Wi-Fi). &lt;a href&#x3D;\&quot;/reference/hotels/google-hotels-amenities\&quot;&gt;Google Hotels Amenities&lt;/a&gt; (hotel amenities). &lt;a href&#x3D;\&quot;/reference/hotels/google-hotels-vacation-rentals-amenities\&quot;&gt;Google Hotels Vacation Rentals Amenities&lt;/a&gt; (vacation rental amenities) | [optional] 
 **rating** | **str**| Filter by minimum guest rating. Supported values: &#39;7&#39; (3.5+), &#39;8&#39; (4.0+), &#39;9&#39; (4.5+). | [optional] 
 **brands** | **str**| Filter by specific hotel brand IDs. IDs can be comma-separated. | [optional] 
 **hotel_class** | **str**| Filter by hotel star ratings. Supported values: &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;. Can be comma-separated. | [optional] 
 **free_cancellation** | **str**| Filter for hotels that offer free cancellation. Set to &#39;1&#39; or &#39;true&#39; to enable. | [optional] 
 **special_offers** | **str**| Filter for hotels currently offering special deals or discounts. Set to &#39;1&#39; or &#39;true&#39; to enable. | [optional] 
 **eco_certified** | **str**| Filter for hotels that are eco-certified. Set to &#39;1&#39; or &#39;true&#39; to enable. | [optional] 
 **vacation_rentals** | **bool**| Set to true to search for vacation rentals instead of standard hotels. | [optional] 
 **bedrooms** | **str**| Minimum number of bedrooms required (applies to vacation rentals). | [optional] 
 **bathrooms** | **str**| Minimum number of bathrooms required (applies to vacation rentals). | [optional] 
 **property_token** | **str**| The unique token for a specific hotel property to fetch detailed information. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_search**
> object images_search(query, html=html, page=page, domain=domain, country=country, cr=cr, language=language, lr=lr, uule=uule, period_unit=period_unit, period_value=period_value, start_date=start_date, end_date=end_date, chips=chips, tbs=tbs, imgar=imgar, imgsz=imgsz, image_color=image_color, image_type=image_type, licenses=licenses, safe=safe, nfpr=nfpr, filter=filter)

Google Images Search API

Scrape high-resolution images and metadata from Google Images. Our API supports advanced filters like image size, color, type, and usage rights for precise visual data extraction.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for images (e.g., 'mountain landscape', 'luxury cars').
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    cr = 'cr_example' # str | Limits results to search results from specific countries. Format: 'countryXX'. See <a href=\"/reference/google-cr-countries\">Google CR Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    period_unit = 'period_unit_example' # str | Time unit for 'recent' image results. Supported values: 's' (Second), 'n' (Minute), 'h' (Hour), 'd' (Day), 'w' (Week), 'm' (Month), 'y' (Year). (optional)
    period_value = 'period_value_example' # str | Time duration value used with 'period_unit' (e.g., 15 for 15 days). Default: 1. (optional)
    start_date = 'start_date_example' # str | Start date for restricting images to a time range. Format: 'YYYYMMDD' (e.g., '20241201'). (optional)
    end_date = 'end_date_example' # str | End date for restricting images to a time range. Format: 'YYYYMMDD' (e.g., '20241231'). (optional)
    chips = 'chips_example' # str | Additional suggested search terms (chips) to filter images. Values are obtained from previous responses. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)
    imgar = 'imgar_example' # str | Filter by image aspect ratio. Supported values: 's' (Square), 't' (Tall), 'w' (Wide), 'xw' (Panoramic). (optional)
    imgsz = 'imgsz_example' # str | Filter by image size. Supported values: 'l' (Large), 'm' (Medium), 'i' (Icon), and specific resolutions like '4mp', '10mp'. (optional)
    image_color = 'image_color_example' # str | Filter images by a dominant color (e.g., 'red', 'blue', 'bw' for black and white, 'trans' for transparent). (optional)
    image_type = 'image_type_example' # str | Filter by image type. Supported values: 'face', 'photo', 'clipart', 'lineart', 'animated'. (optional)
    licenses = 'licenses_example' # str | Filter by usage rights and licenses. Supported values: 'f' (Free to use), 'fc' (Commercial use), 'cl' (Creative Commons). (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    nfpr = '0' # str | Controls Google's auto-correction. Set to '1' to exclude corrected results, '0' to include them. (optional)
    filter = 'filter_example' # str | Toggle 'Similar Results' and 'Omitted Results' filters. Set to '1' (default) to enable, '0' to disable. (optional)

    try:
        # Google Images Search API
        api_response = api_instance.images_search(query, html=html, page=page, domain=domain, country=country, cr=cr, language=language, lr=lr, uule=uule, period_unit=period_unit, period_value=period_value, start_date=start_date, end_date=end_date, chips=chips, tbs=tbs, imgar=imgar, imgsz=imgsz, image_color=image_color, image_type=image_type, licenses=licenses, safe=safe, nfpr=nfpr, filter=filter)
        print("The response of GoogleAPIApi->images_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->images_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for images (e.g., &#39;mountain landscape&#39;, &#39;luxury cars&#39;). | 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **cr** | **str**| Limits results to search results from specific countries. Format: &#39;countryXX&#39;. See &lt;a href&#x3D;\&quot;/reference/google-cr-countries\&quot;&gt;Google CR Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **period_unit** | **str**| Time unit for &#39;recent&#39; image results. Supported values: &#39;s&#39; (Second), &#39;n&#39; (Minute), &#39;h&#39; (Hour), &#39;d&#39; (Day), &#39;w&#39; (Week), &#39;m&#39; (Month), &#39;y&#39; (Year). | [optional] 
 **period_value** | **str**| Time duration value used with &#39;period_unit&#39; (e.g., 15 for 15 days). Default: 1. | [optional] 
 **start_date** | **str**| Start date for restricting images to a time range. Format: &#39;YYYYMMDD&#39; (e.g., &#39;20241201&#39;). | [optional] 
 **end_date** | **str**| End date for restricting images to a time range. Format: &#39;YYYYMMDD&#39; (e.g., &#39;20241231&#39;). | [optional] 
 **chips** | **str**| Additional suggested search terms (chips) to filter images. Values are obtained from previous responses. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **imgar** | **str**| Filter by image aspect ratio. Supported values: &#39;s&#39; (Square), &#39;t&#39; (Tall), &#39;w&#39; (Wide), &#39;xw&#39; (Panoramic). | [optional] 
 **imgsz** | **str**| Filter by image size. Supported values: &#39;l&#39; (Large), &#39;m&#39; (Medium), &#39;i&#39; (Icon), and specific resolutions like &#39;4mp&#39;, &#39;10mp&#39;. | [optional] 
 **image_color** | **str**| Filter images by a dominant color (e.g., &#39;red&#39;, &#39;blue&#39;, &#39;bw&#39; for black and white, &#39;trans&#39; for transparent). | [optional] 
 **image_type** | **str**| Filter by image type. Supported values: &#39;face&#39;, &#39;photo&#39;, &#39;clipart&#39;, &#39;lineart&#39;, &#39;animated&#39;. | [optional] 
 **licenses** | **str**| Filter by usage rights and licenses. Supported values: &#39;f&#39; (Free to use), &#39;fc&#39; (Commercial use), &#39;cl&#39; (Creative Commons). | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **nfpr** | **str**| Controls Google&#39;s auto-correction. Set to &#39;1&#39; to exclude corrected results, &#39;0&#39; to include them. | [optional] 
 **filter** | **str**| Toggle &#39;Similar Results&#39; and &#39;Omitted Results&#39; filters. Set to &#39;1&#39; (default) to enable, &#39;0&#39; to disable. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **immersive_product**
> object immersive_product(page_token, stores=stores, sori=sori, country=country, language=language)

Google Immersive Product API

Access rich product data and immersive shopping results from Google. Scrape detailed product features, 3D views (where available), and pricing information.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    page_token = 'page_token_example' # str | The unique token used to retrieve detailed product information in Google's immersive view. This token is typically found in Google Shopping or Search results.
    stores = False # bool | If set to true, the API will retrieve a list of more sellers for the product. Use this together with the 'sori' parameter. (optional)
    sori = 56 # int | Pagination offset for seller results. Set this to the number of sellers already retrieved to get the next set. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)

    try:
        # Google Immersive Product API
        api_response = api_instance.immersive_product(page_token, stores=stores, sori=sori, country=country, language=language)
        print("The response of GoogleAPIApi->immersive_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->immersive_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**| The unique token used to retrieve detailed product information in Google&#39;s immersive view. This token is typically found in Google Shopping or Search results. | 
 **stores** | **bool**| If set to true, the API will retrieve a list of more sellers for the product. Use this together with the &#39;sori&#39; parameter. | [optional] 
 **sori** | **int**| Pagination offset for seller results. Set this to the number of sellers already retrieved to get the next set. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_search**
> object jobs_search(query, country=country, language=language, next_page_token=next_page_token, chips=chips, lrad=lrad, ltype=ltype, uds=uds, uule=uule)

Google Jobs Search API

Scrape real-time job listings from Google Jobs with our specialized API. Extract structured data including job titles, descriptions, companies, and locations for HR tech and recruitment apps.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The job search query (e.g., 'software engineer', 'data scientist London').
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    next_page_token = 'next_page_token_example' # str | Token for retrieving the next page of job results. Found in 'next_page_token' of a previous response. (optional)
    chips = 'chips_example' # str | Additional search filters (chips) such as job type, date posted, etc. Use values returned in previous responses. (optional)
    lrad = 'lrad_example' # str | Search radius in miles around the specified location. (optional)
    ltype = 'ltype_example' # str | Filter by job location type. Set to '1' for work-from-home (remote) jobs. (optional)
    uds = 'uds_example' # str | Advanced Google-provided filter string for job results. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) to localize job results to a specific geographic area. (optional)

    try:
        # Google Jobs Search API
        api_response = api_instance.jobs_search(query, country=country, language=language, next_page_token=next_page_token, chips=chips, lrad=lrad, ltype=ltype, uds=uds, uule=uule)
        print("The response of GoogleAPIApi->jobs_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->jobs_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The job search query (e.g., &#39;software engineer&#39;, &#39;data scientist London&#39;). | 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **next_page_token** | **str**| Token for retrieving the next page of job results. Found in &#39;next_page_token&#39; of a previous response. | [optional] 
 **chips** | **str**| Additional search filters (chips) such as job type, date posted, etc. Use values returned in previous responses. | [optional] 
 **lrad** | **str**| Search radius in miles around the specified location. | [optional] 
 **ltype** | **str**| Filter by job location type. Set to &#39;1&#39; for work-from-home (remote) jobs. | [optional] 
 **uds** | **str**| Advanced Google-provided filter string for job results. | [optional] 
 **uule** | **str**| Encoded location string (UULE) to localize job results to a specific geographic area. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lens**
> object lens(url, country=country, language=language, product=product, visual_matches=visual_matches, exact_matches=exact_matches)

Google Lens API

Extract visual search results and product information using our Google Lens API. Scrape image-based search data, including identified objects and related web links.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    url = 'url_example' # str | The URL of the image you want to analyze with Google Lens. Must be a publicly accessible image URL.
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    product = False # bool | If set to true, the API will specifically look for product matches and shopping results. (optional)
    visual_matches = False # bool | If set to true, the API will return visually similar images and matches. (optional)
    exact_matches = False # bool | If set to true, the API will search for exact duplicates of the provided image. (optional)

    try:
        # Google Lens API
        api_response = api_instance.lens(url, country=country, language=language, product=product, visual_matches=visual_matches, exact_matches=exact_matches)
        print("The response of GoogleAPIApi->lens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->lens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The URL of the image you want to analyze with Google Lens. Must be a publicly accessible image URL. | 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **product** | **bool**| If set to true, the API will specifically look for product matches and shopping results. | [optional] 
 **visual_matches** | **bool**| If set to true, the API will return visually similar images and matches. | [optional] 
 **exact_matches** | **bool**| If set to true, the API will search for exact duplicates of the provided image. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_search**
> object local_search(query, page=page, location=location, uule=uule, country=country, language=language, domain=domain, ludocid=ludocid, tbs=tbs)

Google Local Search API

Scrape local business listings and map results with our Google Local Search API. Get structured data including addresses, phone numbers, and ratings for businesses in any location.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for local businesses (e.g., 'pizza', 'dentist near me').
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    location = 'location_example' # str | The textual location name (e.g., 'New York, NY') to localize the search results. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    ludocid = 'ludocid_example' # str | The unique Google Business Profile listing ID (CID) to get details for a specific business. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)

    try:
        # Google Local Search API
        api_response = api_instance.local_search(query, page=page, location=location, uule=uule, country=country, language=language, domain=domain, ludocid=ludocid, tbs=tbs)
        print("The response of GoogleAPIApi->local_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->local_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for local businesses (e.g., &#39;pizza&#39;, &#39;dentist near me&#39;). | 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **location** | **str**| The textual location name (e.g., &#39;New York, NY&#39;) to localize the search results. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **ludocid** | **str**| The unique Google Business Profile listing ID (CID) to get details for a specific business. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_photos**
> object maps_photos(data_id, language=language, category_id=category_id, next_page_token=next_page_token)

Google Maps Photos API

Extract high-quality photos from Google Maps locations with our Google Maps Photos API. Scrape image URLs and metadata for business listings and points of interest.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    data_id = 'data_id_example' # str | The unique Google Maps location ID (feature ID). You can get this from our Google Maps Search API.
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    category_id = 'category_id_example' # str | The unique ID for a photo category (e.g., 'Interior', 'Exterior'). Found in previous Maps Photos API responses. (optional)
    next_page_token = 'next_page_token_example' # str | Token for retrieving the next page of photo results. (optional)

    try:
        # Google Maps Photos API
        api_response = api_instance.maps_photos(data_id, language=language, category_id=category_id, next_page_token=next_page_token)
        print("The response of GoogleAPIApi->maps_photos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->maps_photos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_id** | **str**| The unique Google Maps location ID (feature ID). You can get this from our Google Maps Search API. | 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **category_id** | **str**| The unique ID for a photo category (e.g., &#39;Interior&#39;, &#39;Exterior&#39;). Found in previous Maps Photos API responses. | [optional] 
 **next_page_token** | **str**| Token for retrieving the next page of photo results. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_places**
> object maps_places(place_id=place_id, data_id=data_id, country=country)

Google Maps Places API

Get comprehensive details about specific locations using the Google Maps Places API. Scrape contact info, business hours, coordinates, and more from Google Maps.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    place_id = 'place_id_example' # str | The unique Google Place ID. Obtainable via the Google Maps Search API. Use this or 'data_id'. (optional)
    data_id = 'data_id_example' # str | The unique Google Maps location data ID. Use this or 'place_id'. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)

    try:
        # Google Maps Places API
        api_response = api_instance.maps_places(place_id=place_id, data_id=data_id, country=country)
        print("The response of GoogleAPIApi->maps_places:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->maps_places: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_id** | **str**| The unique Google Place ID. Obtainable via the Google Maps Search API. Use this or &#39;data_id&#39;. | [optional] 
 **data_id** | **str**| The unique Google Maps location data ID. Use this or &#39;place_id&#39;. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_posts**
> object maps_posts(data_id, next_page_token=next_page_token)

Google Maps Posts API

Scrape business updates and posts from Google Maps. Use our Google Maps Posts API to keep track of local business announcements and promotional content.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    data_id = 'data_id_example' # str | The unique Google Maps location ID (feature ID). You can get this from our Google Maps Search API.
    next_page_token = 'next_page_token_example' # str | Token used to retrieve the next page of business posts. (optional)

    try:
        # Google Maps Posts API
        api_response = api_instance.maps_posts(data_id, next_page_token=next_page_token)
        print("The response of GoogleAPIApi->maps_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->maps_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_id** | **str**| The unique Google Maps location ID (feature ID). You can get this from our Google Maps Search API. | 
 **next_page_token** | **str**| Token used to retrieve the next page of business posts. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_reviews**
> object maps_reviews(data_id, language=language, sort_by=sort_by, topic_id=topic_id, next_page_token=next_page_token, results=results)

Google Maps Reviews API

Extract user reviews and ratings from Google Maps with our Google Maps Reviews API. Get structured data for sentiment analysis and brand reputation management.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    data_id = 'data_id_example' # str | The unique Google Maps location ID (feature ID). You can get this from our Google Maps Search API.
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    sort_by = 'qualityScore' # str | Sorting order for reviews. Supported values: 'qualityScore' (Relevance), 'newestFirst' (Newest), 'ratingHigh' (Highest rating), 'ratingLow' (Lowest rating). (optional)
    topic_id = 'topic_id_example' # str | Filter reviews by a specific topic ID. Topic IDs are obtained from previous Maps Reviews API responses. (optional)
    next_page_token = 'next_page_token_example' # str | Token for retrieving the next page of reviews. (optional)
    results = 10 # int | The maximum number of reviews to return per page (range: 1-20). (optional)

    try:
        # Google Maps Reviews API
        api_response = api_instance.maps_reviews(data_id, language=language, sort_by=sort_by, topic_id=topic_id, next_page_token=next_page_token, results=results)
        print("The response of GoogleAPIApi->maps_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->maps_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_id** | **str**| The unique Google Maps location ID (feature ID). You can get this from our Google Maps Search API. | 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **sort_by** | **str**| Sorting order for reviews. Supported values: &#39;qualityScore&#39; (Relevance), &#39;newestFirst&#39; (Newest), &#39;ratingHigh&#39; (Highest rating), &#39;ratingLow&#39; (Lowest rating). | [optional] 
 **topic_id** | **str**| Filter reviews by a specific topic ID. Topic IDs are obtained from previous Maps Reviews API responses. | [optional] 
 **next_page_token** | **str**| Token for retrieving the next page of reviews. | [optional] 
 **results** | **int**| The maximum number of reviews to return per page (range: 1-20). | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_search**
> object maps_search(query, ll=ll, domain=domain, language=language, country=country, data=data, place_id=place_id, page=page)

Google Maps Search API

Powerful Google Maps SERP API to scrape business listings and local search results. Perfect for lead generation and local SEO tracking with precise coordinate support.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google Maps (e.g., 'restaurants', 'hospitals in New York').
    ll = 'll_example' # str | GPS coordinates for the search origin. Format: '@<latitude>,<longitude>,<zoom>'. Required for precise localization and pagination. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    data = 'data_example' # str | Advanced Google Maps data parameter used for certain map/place-specific result filters and views. It can be copied from a Google Maps URL after applying filters, or constructed for specific place searches. This parameter is commonly used when type = \"place\". If you’re not familiar with it, you can leave it empty. (optional)
    place_id = 'place_id_example' # str | The unique Google Place ID to directly retrieve information for a specific location. (optional)
    page = 0 # int | The results pagination offset. Start at 0 and increment by 20 for each subsequent page. (optional)

    try:
        # Google Maps Search API
        api_response = api_instance.maps_search(query, ll=ll, domain=domain, language=language, country=country, data=data, place_id=place_id, page=page)
        print("The response of GoogleAPIApi->maps_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->maps_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google Maps (e.g., &#39;restaurants&#39;, &#39;hospitals in New York&#39;). | 
 **ll** | **str**| GPS coordinates for the search origin. Format: &#39;@&lt;latitude&gt;,&lt;longitude&gt;,&lt;zoom&gt;&#39;. Required for precise localization and pagination. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **data** | **str**| Advanced Google Maps data parameter used for certain map/place-specific result filters and views. It can be copied from a Google Maps URL after applying filters, or constructed for specific place searches. This parameter is commonly used when type &#x3D; \&quot;place\&quot;. If you’re not familiar with it, you can leave it empty. | [optional] 
 **place_id** | **str**| The unique Google Place ID to directly retrieve information for a specific location. | [optional] 
 **page** | **int**| The results pagination offset. Start at 0 and increment by 20 for each subsequent page. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_search**
> object news_search(query, country=country, language=language, topic_token=topic_token, publication_token=publication_token, section_token=section_token, so=so)

Google News Search API

Get real-time news headlines and stories with our Google News Search API. Scrape structured data from Google News, including source info, publication dates, and related topics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google News (e.g., 'artificial intelligence', 'climate change').
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    topic_token = 'topic_token_example' # str | The Google News topic token to retrieve results for a specific category (e.g., 'World', 'Technology'). Obtained from previous responses. (optional)
    publication_token = 'publication_token_example' # str | The Google News publication token to fetch results from a specific source (e.g., 'CNN', 'BBC'). Obtained from previous responses. (optional)
    section_token = 'section_token_example' # str | The Google News section token to access a specific subsection within a topic or publication. (optional)
    so = 'so_example' # str | Sorting order for news results. Supported values: '0' (Relevance, default), '1' (Date). Only works with 'story_token'. (optional)

    try:
        # Google News Search API
        api_response = api_instance.news_search(query, country=country, language=language, topic_token=topic_token, publication_token=publication_token, section_token=section_token, so=so)
        print("The response of GoogleAPIApi->news_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->news_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google News (e.g., &#39;artificial intelligence&#39;, &#39;climate change&#39;). | 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **topic_token** | **str**| The Google News topic token to retrieve results for a specific category (e.g., &#39;World&#39;, &#39;Technology&#39;). Obtained from previous responses. | [optional] 
 **publication_token** | **str**| The Google News publication token to fetch results from a specific source (e.g., &#39;CNN&#39;, &#39;BBC&#39;). Obtained from previous responses. | [optional] 
 **section_token** | **str**| The Google News section token to access a specific subsection within a topic or publication. | [optional] 
 **so** | **str**| Sorting order for news results. Supported values: &#39;0&#39; (Relevance, default), &#39;1&#39; (Date). Only works with &#39;story_token&#39;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patent_details**
> object patent_details(patent_id, language=language, html=html)

Google Patents Details API

Get comprehensive patent information with our Google Patents Details API. Extract structured data including patent abstracts, claims, descriptions, and legal statuses.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    patent_id = 'patent_id_example' # str | The unique Google Patent ID (e.g., 'US1234567B1').
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)

    try:
        # Google Patents Details API
        api_response = api_instance.patent_details(patent_id, language=language, html=html)
        print("The response of GoogleAPIApi->patent_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->patent_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patent_id** | **str**| The unique Google Patent ID (e.g., &#39;US1234567B1&#39;). | 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patent_search**
> object patent_search(query, page=page, num=num, sort=sort, clustered=clustered, dups=dups, patents=patents, scholar=scholar, before=before, after=after, inventor=inventor, assignee=assignee, country=country, language=language, status=status, type=type, litigation=litigation)

Google Patents Search API

Powerful Google Patents SERP API to search and scrape patent documents. Filter results by inventor, assignee, date, and status for detailed intellectual property research.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for patents (e.g., 'autonomous vehicles', 'blockchain security').
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    num = 10 # int | The number of results to return per page (range: 1-100). (optional)
    sort = 'sort_example' # str | Sorting order for patent results. Supported values: 'new' (Newest), 'old' (Oldest). (optional)
    clustered = True # bool | If set to true, results will be grouped by classification. (optional)
    dups = 'dups_example' # str | Deduplication method. Supported values: 'language' (by Publication). (optional)
    patents = True # bool | Whether to include Google Patents results. (optional)
    scholar = False # bool | Whether to include Google Scholar results. (optional)
    before = 'before_example' # str | Latest date to include. Format: 'type:YYYYMMDD' (e.g., 'publication:20230101'). (optional)
    after = 'after_example' # str | Earliest date to include. Format: 'type:YYYYMMDD' (e.g., 'filing:20200101'). (optional)
    inventor = 'inventor_example' # str | Filter by patent inventor(s). Multiple values can be comma-separated. (optional)
    assignee = 'assignee_example' # str | Filter by patent assignee(s). Multiple values can be comma-separated. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    status = 'status_example' # str | Filter by patent status. Supported values: 'GRANT', 'APPLICATION'. (optional)
    type = 'type_example' # str | Filter by patent type. Supported values: 'PATENT', 'DESIGN'. (optional)
    litigation = 'litigation_example' # str | Filter by litigation status. Supported values: 'YES', 'NO'. (optional)

    try:
        # Google Patents Search API
        api_response = api_instance.patent_search(query, page=page, num=num, sort=sort, clustered=clustered, dups=dups, patents=patents, scholar=scholar, before=before, after=after, inventor=inventor, assignee=assignee, country=country, language=language, status=status, type=type, litigation=litigation)
        print("The response of GoogleAPIApi->patent_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->patent_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for patents (e.g., &#39;autonomous vehicles&#39;, &#39;blockchain security&#39;). | 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **num** | **int**| The number of results to return per page (range: 1-100). | [optional] 
 **sort** | **str**| Sorting order for patent results. Supported values: &#39;new&#39; (Newest), &#39;old&#39; (Oldest). | [optional] 
 **clustered** | **bool**| If set to true, results will be grouped by classification. | [optional] 
 **dups** | **str**| Deduplication method. Supported values: &#39;language&#39; (by Publication). | [optional] 
 **patents** | **bool**| Whether to include Google Patents results. | [optional] 
 **scholar** | **bool**| Whether to include Google Scholar results. | [optional] 
 **before** | **str**| Latest date to include. Format: &#39;type:YYYYMMDD&#39; (e.g., &#39;publication:20230101&#39;). | [optional] 
 **after** | **str**| Earliest date to include. Format: &#39;type:YYYYMMDD&#39; (e.g., &#39;filing:20200101&#39;). | [optional] 
 **inventor** | **str**| Filter by patent inventor(s). Multiple values can be comma-separated. | [optional] 
 **assignee** | **str**| Filter by patent assignee(s). Multiple values can be comma-separated. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **status** | **str**| Filter by patent status. Supported values: &#39;GRANT&#39;, &#39;APPLICATION&#39;. | [optional] 
 **type** | **str**| Filter by patent type. Supported values: &#39;PATENT&#39;, &#39;DESIGN&#39;. | [optional] 
 **litigation** | **str**| Filter by litigation status. Supported values: &#39;YES&#39;, &#39;NO&#39;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scholar_author**
> object scholar_author(author_id, results=results, language=language, view_op=view_op, sort=sort, citation_id=citation_id)

Google Scholar Author API

Scrape Google Scholar author profiles to get comprehensive lists of publications, citations, and research interests. Structured data for academic research and talent discovery.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    author_id = 'author_id_example' # str | The unique Google Scholar ID of the researcher/author (e.g., 'LSs6DR8AAAAJ').
    results = 20 # int | The number of results to return per page. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    view_op = 'view_op_example' # str | Specific view operation for the author profile. Use 'list_colleagues' to see co-authors or 'view_citation' for article details. (optional)
    sort = 'sort_example' # str | Sorting criteria for the author's publications. Supported values: 'title', 'pubdate'. (optional)
    citation_id = 'citation_id_example' # str | The citation ID to view details for (required when 'view_op' is 'view_citation'). (optional)

    try:
        # Google Scholar Author API
        api_response = api_instance.scholar_author(author_id, results=results, language=language, view_op=view_op, sort=sort, citation_id=citation_id)
        print("The response of GoogleAPIApi->scholar_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->scholar_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **str**| The unique Google Scholar ID of the researcher/author (e.g., &#39;LSs6DR8AAAAJ&#39;). | 
 **results** | **int**| The number of results to return per page. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **view_op** | **str**| Specific view operation for the author profile. Use &#39;list_colleagues&#39; to see co-authors or &#39;view_citation&#39; for article details. | [optional] 
 **sort** | **str**| Sorting criteria for the author&#39;s publications. Supported values: &#39;title&#39;, &#39;pubdate&#39;. | [optional] 
 **citation_id** | **str**| The citation ID to view details for (required when &#39;view_op&#39; is &#39;view_citation&#39;). | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scholar_cite_search**
> object scholar_cite_search(query, language=language)

Google Scholar Cite Search API

Retrieve citation information for specific academic papers and articles. This API provides structured bibtex and citation formats directly from Google Scholar.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The unique ID of a Google Scholar search result to retrieve citation formats for. Found in the 'id' field of previous Scholar Search responses.
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)

    try:
        # Google Scholar Cite Search API
        api_response = api_instance.scholar_cite_search(query, language=language)
        print("The response of GoogleAPIApi->scholar_cite_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->scholar_cite_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The unique ID of a Google Scholar search result to retrieve citation formats for. Found in the &#39;id&#39; field of previous Scholar Search responses. | 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scholar_profiles**
> object scholar_profiles(mauthors, after_author=after_author, before_author=before_author)

Google Scholar Profiles API

Search and extract data from Google Scholar user profiles. Get real-time access to researcher information, h-index, and publication history.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    mauthors = 'mauthors_example' # str | The search query for author profiles (e.g., 'John Smith', 'Harvard University').
    after_author = 'after_author_example' # str | Token used to retrieve the next page of author profiles. (optional)
    before_author = 'before_author_example' # str | Token used to retrieve the previous page of author profiles. (optional)

    try:
        # Google Scholar Profiles API
        api_response = api_instance.scholar_profiles(mauthors, after_author=after_author, before_author=before_author)
        print("The response of GoogleAPIApi->scholar_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->scholar_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mauthors** | **str**| The search query for author profiles (e.g., &#39;John Smith&#39;, &#39;Harvard University&#39;). | 
 **after_author** | **str**| Token used to retrieve the next page of author profiles. | [optional] 
 **before_author** | **str**| Token used to retrieve the previous page of author profiles. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scholar_search**
> object scholar_search(query, html=html, cites=cites, as_ylo=as_ylo, as_yhi=as_yhi, scisbd=scisbd, cluster=cluster, language=language, lr=lr, page=page, results=results, as_sdt=as_sdt, safe=safe, filter=filter, as_vis=as_vis, as_rr=as_rr)

Google Scholar Search API

Comprehensive Google Scholar SERP API to scrape academic papers, patents, and legal documents. Filter by date, relevance, and citation count for precise research data.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The academic search query (e.g., 'machine learning', 'CRISPR gene editing'). Supports advanced operators like 'author:'.
    html = False # bool | Set to true to return the raw HTML of the Google Scholar search page. (optional)
    cites = 'cites_example' # str | Return articles that cite the article with the specified ID. (optional)
    as_ylo = 'as_ylo_example' # str | Minimum publication year filter (e.g., '2020'). (optional)
    as_yhi = 'as_yhi_example' # str | Maximum publication year filter (e.g., '2024'). (optional)
    scisbd = 'scisbd_example' # str | Controls whether to return only abstract results (1) or all results (0). (optional)
    cluster = 'cluster_example' # str | The unique ID of an article cluster to retrieve all versions of a specific work. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    results = 10 # int | The number of search results to return per page. (optional)
    as_sdt = 'as_sdt_example' # str | Advanced filter for specific document types or legal jurisdictions. E.g., '7' to include patents. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    filter = 'filter_example' # str | Toggle 'Similar Results' and 'Omitted Results' filters. Set to '1' (default) to enable, '0' to disable. (optional)
    as_vis = 'as_vis_example' # str | Controls whether citations are included in the results: 1 = exclude, 0 (default) = include. (optional)
    as_rr = 'as_rr_example' # str | Controls whether to show only review articles (topic overviews or discussions of the searched works/authors). Set to 1 to enable the filter, or 0 (default) to return all results. (optional)

    try:
        # Google Scholar Search API
        api_response = api_instance.scholar_search(query, html=html, cites=cites, as_ylo=as_ylo, as_yhi=as_yhi, scisbd=scisbd, cluster=cluster, language=language, lr=lr, page=page, results=results, as_sdt=as_sdt, safe=safe, filter=filter, as_vis=as_vis, as_rr=as_rr)
        print("The response of GoogleAPIApi->scholar_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->scholar_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The academic search query (e.g., &#39;machine learning&#39;, &#39;CRISPR gene editing&#39;). Supports advanced operators like &#39;author:&#39;. | 
 **html** | **bool**| Set to true to return the raw HTML of the Google Scholar search page. | [optional] 
 **cites** | **str**| Return articles that cite the article with the specified ID. | [optional] 
 **as_ylo** | **str**| Minimum publication year filter (e.g., &#39;2020&#39;). | [optional] 
 **as_yhi** | **str**| Maximum publication year filter (e.g., &#39;2024&#39;). | [optional] 
 **scisbd** | **str**| Controls whether to return only abstract results (1) or all results (0). | [optional] 
 **cluster** | **str**| The unique ID of an article cluster to retrieve all versions of a specific work. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **results** | **int**| The number of search results to return per page. | [optional] 
 **as_sdt** | **str**| Advanced filter for specific document types or legal jurisdictions. E.g., &#39;7&#39; to include patents. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **filter** | **str**| Toggle &#39;Similar Results&#39; and &#39;Omitted Results&#39; filters. Set to &#39;1&#39; (default) to enable, &#39;0&#39; to disable. | [optional] 
 **as_vis** | **str**| Controls whether citations are included in the results: 1 &#x3D; exclude, 0 (default) &#x3D; include. | [optional] 
 **as_rr** | **str**| Controls whether to show only review articles (topic overviews or discussions of the searched works/authors). Set to 1 to enable the filter, or 0 (default) to return all results. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> object search(query, page=page, html=html, language=language, lr=lr, domain=domain, country=country, cr=cr, uule=uule, location=location, ludocid=ludocid, lsig=lsig, kgmid=kgmid, si=si, ibp=ibp, uds=uds, tbs=tbs, safe=safe, nfpr=nfpr, filter=filter)

Google Search API

Powerful Google Search SERP API to scrape organic search results, ads, knowledge panels, and more. Get real-time, structured data from Google Search with global location support and proxy rotation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google Search (e.g., 'coffee shops', 'how to bake a cake').
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    cr = 'cr_example' # str | Limits results to search results from specific countries. Format: 'countryXX'. See <a href=\"/reference/google-cr-countries\">Google CR Countries</a>. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    location = 'location_example' # str | The textual location name (e.g., 'New York, NY') to localize the search results. (optional)
    ludocid = 'ludocid_example' # str | Google local business CID (place identifier). Used to target a specific Google Business Profile / local listing. Advanced parameter — if you don’t know it, you can omit it. (optional)
    lsig = 'lsig_example' # str | Signature parameter (lsig) sometimes required for certain Knowledge Graph / local map view features. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    kgmid = 'kgmid_example' # str | Knowledge Graph entity/listing ID (KGMID) used to retrieve details for a specific entity. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    si = 'si_example' # str | Cached search context parameter (si) used to reproduce specific Google search result views/context (e.g. some Knowledge Graph tabs). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    ibp = 'ibp_example' # str | Parameter (ibp) used to control certain Google UI expansions or rendering modes (commonly in local/business result views). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    uds = 'uds_example' # str | Advanced filter token (uds) used for specific Google search sub-filters. This is an advanced technical parameter, usually provided by Google in filter options/results — if you’re not familiar with it, you can leave it empty. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    nfpr = '0' # str | Controls Google's auto-correction. Set to '1' to exclude corrected results, '0' to include them. (optional)
    filter = 'filter_example' # str | Toggle 'Similar Results' and 'Omitted Results' filters. Set to '1' (default) to enable, '0' to disable. (optional)

    try:
        # Google Search API
        api_response = api_instance.search(query, page=page, html=html, language=language, lr=lr, domain=domain, country=country, cr=cr, uule=uule, location=location, ludocid=ludocid, lsig=lsig, kgmid=kgmid, si=si, ibp=ibp, uds=uds, tbs=tbs, safe=safe, nfpr=nfpr, filter=filter)
        print("The response of GoogleAPIApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google Search (e.g., &#39;coffee shops&#39;, &#39;how to bake a cake&#39;). | 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **cr** | **str**| Limits results to search results from specific countries. Format: &#39;countryXX&#39;. See &lt;a href&#x3D;\&quot;/reference/google-cr-countries\&quot;&gt;Google CR Countries&lt;/a&gt;. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **location** | **str**| The textual location name (e.g., &#39;New York, NY&#39;) to localize the search results. | [optional] 
 **ludocid** | **str**| Google local business CID (place identifier). Used to target a specific Google Business Profile / local listing. Advanced parameter — if you don’t know it, you can omit it. | [optional] 
 **lsig** | **str**| Signature parameter (lsig) sometimes required for certain Knowledge Graph / local map view features. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **kgmid** | **str**| Knowledge Graph entity/listing ID (KGMID) used to retrieve details for a specific entity. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **si** | **str**| Cached search context parameter (si) used to reproduce specific Google search result views/context (e.g. some Knowledge Graph tabs). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **ibp** | **str**| Parameter (ibp) used to control certain Google UI expansions or rendering modes (commonly in local/business result views). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **uds** | **str**| Advanced filter token (uds) used for specific Google search sub-filters. This is an advanced technical parameter, usually provided by Google in filter options/results — if you’re not familiar with it, you can leave it empty. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **nfpr** | **str**| Controls Google&#39;s auto-correction. Set to &#39;1&#39; to exclude corrected results, &#39;0&#39; to include them. | [optional] 
 **filter** | **str**| Toggle &#39;Similar Results&#39; and &#39;Omitted Results&#39; filters. Set to &#39;1&#39; (default) to enable, &#39;0&#39; to disable. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_light**
> object search_light(query, page=page, html=html, language=language, lr=lr, domain=domain, country=country, cr=cr, uule=uule, location=location, ludocid=ludocid, lsig=lsig, kgmid=kgmid, si=si, ibp=ibp, uds=uds, tbs=tbs, safe=safe, nfpr=nfpr, filter=filter)

Google Light Search API

A fast and lightweight Google Search API designed for high-speed retrieval of essential SERP data. Ideal for applications that need quick organic results with minimal overhead.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google Search (e.g., 'coffee shops', 'how to bake a cake').
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    cr = 'cr_example' # str | Limits results to search results from specific countries. Format: 'countryXX'. See <a href=\"/reference/google-cr-countries\">Google CR Countries</a>. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    location = 'location_example' # str | The textual location name (e.g., 'New York, NY') to localize the search results. (optional)
    ludocid = 'ludocid_example' # str | Google local business CID (place identifier). Used to target a specific Google Business Profile / local listing. Advanced parameter — if you don’t know it, you can omit it. (optional)
    lsig = 'lsig_example' # str | Signature parameter (lsig) sometimes required for certain Knowledge Graph / local map view features. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    kgmid = 'kgmid_example' # str | Knowledge Graph entity/listing ID (KGMID) used to retrieve details for a specific entity. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    si = 'si_example' # str | Cached search context parameter (si) used to reproduce specific Google search result views/context (e.g. some Knowledge Graph tabs). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    ibp = 'ibp_example' # str | Parameter (ibp) used to control certain Google UI expansions or rendering modes (commonly in local/business result views). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    uds = 'uds_example' # str | Advanced filter token (uds) used for specific Google search sub-filters. This is an advanced technical parameter, usually provided by Google in filter options/results — if you’re not familiar with it, you can leave it empty. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    nfpr = '0' # str | Controls Google's auto-correction. Set to '1' to exclude corrected results, '0' to include them. (optional)
    filter = 'filter_example' # str | Toggle 'Similar Results' and 'Omitted Results' filters. Set to '1' (default) to enable, '0' to disable. (optional)

    try:
        # Google Light Search API
        api_response = api_instance.search_light(query, page=page, html=html, language=language, lr=lr, domain=domain, country=country, cr=cr, uule=uule, location=location, ludocid=ludocid, lsig=lsig, kgmid=kgmid, si=si, ibp=ibp, uds=uds, tbs=tbs, safe=safe, nfpr=nfpr, filter=filter)
        print("The response of GoogleAPIApi->search_light:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->search_light: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google Search (e.g., &#39;coffee shops&#39;, &#39;how to bake a cake&#39;). | 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **cr** | **str**| Limits results to search results from specific countries. Format: &#39;countryXX&#39;. See &lt;a href&#x3D;\&quot;/reference/google-cr-countries\&quot;&gt;Google CR Countries&lt;/a&gt;. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **location** | **str**| The textual location name (e.g., &#39;New York, NY&#39;) to localize the search results. | [optional] 
 **ludocid** | **str**| Google local business CID (place identifier). Used to target a specific Google Business Profile / local listing. Advanced parameter — if you don’t know it, you can omit it. | [optional] 
 **lsig** | **str**| Signature parameter (lsig) sometimes required for certain Knowledge Graph / local map view features. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **kgmid** | **str**| Knowledge Graph entity/listing ID (KGMID) used to retrieve details for a specific entity. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **si** | **str**| Cached search context parameter (si) used to reproduce specific Google search result views/context (e.g. some Knowledge Graph tabs). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **ibp** | **str**| Parameter (ibp) used to control certain Google UI expansions or rendering modes (commonly in local/business result views). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **uds** | **str**| Advanced filter token (uds) used for specific Google search sub-filters. This is an advanced technical parameter, usually provided by Google in filter options/results — if you’re not familiar with it, you can leave it empty. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **nfpr** | **str**| Controls Google&#39;s auto-correction. Set to &#39;1&#39; to exclude corrected results, &#39;0&#39; to include them. | [optional] 
 **filter** | **str**| Toggle &#39;Similar Results&#39; and &#39;Omitted Results&#39; filters. Set to &#39;1&#39; (default) to enable, &#39;0&#39; to disable. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_mobile**
> object search_mobile(query, page=page, html=html, language=language, lr=lr, domain=domain, country=country, cr=cr, uule=uule, location=location, ludocid=ludocid, lsig=lsig, kgmid=kgmid, si=si, ibp=ibp, uds=uds, tbs=tbs, safe=safe, nfpr=nfpr, filter=filter)

Google Mobile Search API

Scrape mobile-optimized Google search results with our Mobile SERP API. Simulates real mobile devices to provide accurate mobile rankings, features, and layouts for SEO tracking.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google Search (e.g., 'coffee shops', 'how to bake a cake').
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    cr = 'cr_example' # str | Limits results to search results from specific countries. Format: 'countryXX'. See <a href=\"/reference/google-cr-countries\">Google CR Countries</a>. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    location = 'location_example' # str | The textual location name (e.g., 'New York, NY') to localize the search results. (optional)
    ludocid = 'ludocid_example' # str | Google local business CID (place identifier). Used to target a specific Google Business Profile / local listing. Advanced parameter — if you don’t know it, you can omit it. (optional)
    lsig = 'lsig_example' # str | Signature parameter (lsig) sometimes required for certain Knowledge Graph / local map view features. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    kgmid = 'kgmid_example' # str | Knowledge Graph entity/listing ID (KGMID) used to retrieve details for a specific entity. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    si = 'si_example' # str | Cached search context parameter (si) used to reproduce specific Google search result views/context (e.g. some Knowledge Graph tabs). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    ibp = 'ibp_example' # str | Parameter (ibp) used to control certain Google UI expansions or rendering modes (commonly in local/business result views). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. (optional)
    uds = 'uds_example' # str | Advanced filter token (uds) used for specific Google search sub-filters. This is an advanced technical parameter, usually provided by Google in filter options/results — if you’re not familiar with it, you can leave it empty. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    nfpr = '0' # str | Controls Google's auto-correction. Set to '1' to exclude corrected results, '0' to include them. (optional)
    filter = 'filter_example' # str | Toggle 'Similar Results' and 'Omitted Results' filters. Set to '1' (default) to enable, '0' to disable. (optional)

    try:
        # Google Mobile Search API
        api_response = api_instance.search_mobile(query, page=page, html=html, language=language, lr=lr, domain=domain, country=country, cr=cr, uule=uule, location=location, ludocid=ludocid, lsig=lsig, kgmid=kgmid, si=si, ibp=ibp, uds=uds, tbs=tbs, safe=safe, nfpr=nfpr, filter=filter)
        print("The response of GoogleAPIApi->search_mobile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->search_mobile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google Search (e.g., &#39;coffee shops&#39;, &#39;how to bake a cake&#39;). | 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **cr** | **str**| Limits results to search results from specific countries. Format: &#39;countryXX&#39;. See &lt;a href&#x3D;\&quot;/reference/google-cr-countries\&quot;&gt;Google CR Countries&lt;/a&gt;. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **location** | **str**| The textual location name (e.g., &#39;New York, NY&#39;) to localize the search results. | [optional] 
 **ludocid** | **str**| Google local business CID (place identifier). Used to target a specific Google Business Profile / local listing. Advanced parameter — if you don’t know it, you can omit it. | [optional] 
 **lsig** | **str**| Signature parameter (lsig) sometimes required for certain Knowledge Graph / local map view features. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **kgmid** | **str**| Knowledge Graph entity/listing ID (KGMID) used to retrieve details for a specific entity. This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **si** | **str**| Cached search context parameter (si) used to reproduce specific Google search result views/context (e.g. some Knowledge Graph tabs). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **ibp** | **str**| Parameter (ibp) used to control certain Google UI expansions or rendering modes (commonly in local/business result views). This is an advanced technical parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **uds** | **str**| Advanced filter token (uds) used for specific Google search sub-filters. This is an advanced technical parameter, usually provided by Google in filter options/results — if you’re not familiar with it, you can leave it empty. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **nfpr** | **str**| Controls Google&#39;s auto-correction. Set to &#39;1&#39; to exclude corrected results, &#39;0&#39; to include them. | [optional] 
 **filter** | **str**| Toggle &#39;Similar Results&#39; and &#39;Omitted Results&#39; filters. Set to &#39;1&#39; (default) to enable, &#39;0&#39; to disable. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shopping_search**
> object shopping_search(query, page=page, html=html, country=country, domain=domain, language=language, lr=lr, shoprs=shoprs, uule=uule, tbs=tbs, safe=safe, nfpr=nfpr)

Google Shopping Search API

Scrape real-time product listings and prices from Google Shopping. Use our API to get structured shopping data, including merchant info, ratings, and product comparisons.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The shopping search query (e.g., 'iPhone 15', 'running shoes').
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    shoprs = 'shoprs_example' # str | A unique ID used to apply specific shopping filters. Usually obtained from the 'scrapingdog_link' in a previous response. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    nfpr = '0' # str | Controls Google's auto-correction. Set to '1' to exclude corrected results, '0' to include them. (optional)

    try:
        # Google Shopping Search API
        api_response = api_instance.shopping_search(query, page=page, html=html, country=country, domain=domain, language=language, lr=lr, shoprs=shoprs, uule=uule, tbs=tbs, safe=safe, nfpr=nfpr)
        print("The response of GoogleAPIApi->shopping_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->shopping_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The shopping search query (e.g., &#39;iPhone 15&#39;, &#39;running shoes&#39;). | 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **shoprs** | **str**| A unique ID used to apply specific shopping filters. Usually obtained from the &#39;scrapingdog_link&#39; in a previous response. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **nfpr** | **str**| Controls Google&#39;s auto-correction. Set to &#39;1&#39; to exclude corrected results, &#39;0&#39; to include them. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shorts_search**
> object shorts_search(query, start=start, html=html, country=country, domain=domain, language=language, lr=lr, uule=uule, tbs=tbs, safe=safe, nfpr=nfpr)

Google Shorts Search API

Access trending and relevant Google Shorts content with our specialized search API. Scrape video details, rankings, and metadata from Google's short-form video platform.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google Shorts (e.g., 'cooking tips', 'travel hacks').
    start = 0 # int | The result offset to skip a specific number of entries (e.g., set to 12 to skip the first 12 results). (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    nfpr = '0' # str | Controls Google's auto-correction. Set to '1' to exclude corrected results, '0' to include them. (optional)

    try:
        # Google Shorts Search API
        api_response = api_instance.shorts_search(query, start=start, html=html, country=country, domain=domain, language=language, lr=lr, uule=uule, tbs=tbs, safe=safe, nfpr=nfpr)
        print("The response of GoogleAPIApi->shorts_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->shorts_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google Shorts (e.g., &#39;cooking tips&#39;, &#39;travel hacks&#39;). | 
 **start** | **int**| The result offset to skip a specific number of entries (e.g., set to 12 to skip the first 12 results). | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **nfpr** | **str**| Controls Google&#39;s auto-correction. Set to &#39;1&#39; to exclude corrected results, &#39;0&#39; to include them. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trends_autocomplete**
> object trends_autocomplete(query, language=language)

Google Trends Autocomplete API

Access real-time search suggestions and trending keywords with the Google Trends Autocomplete API. Enhance keyword research and discover emerging search patterns.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query to get trending autocomplete suggestions for (e.g., 'artificial').
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)

    try:
        # Google Trends Autocomplete API
        api_response = api_instance.trends_autocomplete(query, language=language)
        print("The response of GoogleAPIApi->trends_autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->trends_autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query to get trending autocomplete suggestions for (e.g., &#39;artificial&#39;). | 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trends_search**
> object trends_search(query, language=language, geo=geo, region=region, data_type=data_type, tz=tz, cat=cat, gprop=gprop, var_date=var_date)

Google Trends Search API

Scrape detailed search interest data, regional trends, and related queries from Google Trends. Perfect for market research, SEO analysis, and tracking topic popularity.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search term or topic ID to analyze in Google Trends (e.g., 'iPhone', '/m/027lnzs' for Bitcoin). You can provide up to 5 terms separated by commas for comparisons.
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    geo = 'geo_example' # str | The geographic location code to filter trends (e.g., 'US', 'GB'). Omit for worldwide trends. See <a href=\"/reference/google-trends-locations\">Google Trends Locations</a>. (optional)
    region = 'region_example' # str | Refines results for region charts. Supported values: 'COUNTRY', 'REGION', 'DMA', 'CITY'. (optional)
    data_type = 'data_type_example' # str | The type of trend data to retrieve. Supported values: 'TIMESERIES' (Interest over time), 'GEO_MAP' (Breakdown by region). (optional)
    tz = 56 # int | Time zone offset in minutes (e.g., '420' for PDT). Range: -1439 to 1439. (optional)
    cat = '0' # str | The search category code (e.g., '0' for all categories). (optional)
    gprop = 'gprop_example' # str | The Google property to filter trends. Supported values: 'images', 'news', 'froogle' (Shopping), 'youtube'. (optional)
    var_date = 'var_date_example' # str | Date range filter for the search. Supports predefined values (now 1-H, now 4-H, now 1-d, now 7-d, today 1-m, today 3-m, today 12-m, today 5-y, all) and custom ranges: yyyy-mm-dd yyyy-mm-dd (e.g. 2021-10-15 2022-05-25) or hourly yyyy-mm-ddThh yyyy-mm-ddThh within 1 week (e.g. 2022-05-19T10 2022-05-24T22, based on tz). (optional)

    try:
        # Google Trends Search API
        api_response = api_instance.trends_search(query, language=language, geo=geo, region=region, data_type=data_type, tz=tz, cat=cat, gprop=gprop, var_date=var_date)
        print("The response of GoogleAPIApi->trends_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->trends_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search term or topic ID to analyze in Google Trends (e.g., &#39;iPhone&#39;, &#39;/m/027lnzs&#39; for Bitcoin). You can provide up to 5 terms separated by commas for comparisons. | 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **geo** | **str**| The geographic location code to filter trends (e.g., &#39;US&#39;, &#39;GB&#39;). Omit for worldwide trends. See &lt;a href&#x3D;\&quot;/reference/google-trends-locations\&quot;&gt;Google Trends Locations&lt;/a&gt;. | [optional] 
 **region** | **str**| Refines results for region charts. Supported values: &#39;COUNTRY&#39;, &#39;REGION&#39;, &#39;DMA&#39;, &#39;CITY&#39;. | [optional] 
 **data_type** | **str**| The type of trend data to retrieve. Supported values: &#39;TIMESERIES&#39; (Interest over time), &#39;GEO_MAP&#39; (Breakdown by region). | [optional] 
 **tz** | **int**| Time zone offset in minutes (e.g., &#39;420&#39; for PDT). Range: -1439 to 1439. | [optional] 
 **cat** | **str**| The search category code (e.g., &#39;0&#39; for all categories). | [optional] 
 **gprop** | **str**| The Google property to filter trends. Supported values: &#39;images&#39;, &#39;news&#39;, &#39;froogle&#39; (Shopping), &#39;youtube&#39;. | [optional] 
 **var_date** | **str**| Date range filter for the search. Supports predefined values (now 1-H, now 4-H, now 1-d, now 7-d, today 1-m, today 3-m, today 12-m, today 5-y, all) and custom ranges: yyyy-mm-dd yyyy-mm-dd (e.g. 2021-10-15 2022-05-25) or hourly yyyy-mm-ddThh yyyy-mm-ddThh within 1 week (e.g. 2022-05-19T10 2022-05-24T22, based on tz). | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trends_trending_now**
> object trends_trending_now(geo, hours=hours, language=language)

Google Trends Trending Now API

Retrieve the latest trending topics and daily search trends across different regions. Stay updated with what's hot on Google in real-time.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    geo = 'geo_example' # str | The geographic location code to retrieve real-time trends for (e.g., 'US' for United States). Default is 'US'.
    hours = 'hours_example' # str | Time window for trending topics. Supported values: '4' (past 4 hours), '24' (past 24 hours), '48' (past 48 hours), '168' (past 7 days). (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en'). (optional)

    try:
        # Google Trends Trending Now API
        api_response = api_instance.trends_trending_now(geo, hours=hours, language=language)
        print("The response of GoogleAPIApi->trends_trending_now:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->trends_trending_now: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geo** | **str**| The geographic location code to retrieve real-time trends for (e.g., &#39;US&#39; for United States). Default is &#39;US&#39;. | 
 **hours** | **str**| Time window for trending topics. Supported values: &#39;4&#39; (past 4 hours), &#39;24&#39; (past 24 hours), &#39;48&#39; (past 48 hours), &#39;168&#39; (past 7 days). | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39;). | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **videos_search**
> object videos_search(query, page=page, html=html, country=country, domain=domain, language=language, lr=lr, uule=uule, tbs=tbs, safe=safe, nfpr=nfpr, result_time=result_time)

Google Videos Search API

Scrape video search results from Google with our Google Videos Search API. Get structured data for video titles, descriptions, source platforms, and publication dates.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import os
from pprint import pprint

from justserpapi.api.google_api_api import GoogleAPIApi
from justserpapi.api_client import ApiClient
from justserpapi.configuration import Configuration
from justserpapi.rest import ApiException

# Defining the host is optional and defaults to https://api.justserpapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = "https://api.justserpapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GoogleAPIApi(api_client)
    query = 'query_example' # str | The search query for Google Videos (e.g., 'coding tutorial', 'movie trailers').
    page = 0 # int | The results page number. Use 0 for the first page, 1 for the second, and so on. (optional)
    html = False # bool | Set to true to return the raw HTML of the Google search results page alongside the structured data. (optional)
    country = 'us' # str | Set the target country code (e.g., 'us', 'uk') to localize results. See <a href=\"/reference/google-countries\">Google Countries</a>. (optional)
    domain = 'google.com' # str | The Google domain to use for the search (e.g., 'google.com', 'google.co.uk'). See <a href=\"/reference/google-domains\">Google Domains</a>. (optional)
    language = 'en' # str | Set the language for the results using its two-letter code (e.g., 'en' for English, 'fr' for French). See <a href=\"/reference/google-language\">Google Language</a>. (optional)
    lr = 'lr_example' # str | Restrict results to one or more languages using the 'lang_{language_code}' format (e.g., 'lang_en'). See <a href=\"/reference/google-lr-language\">Google LR Language</a>. (optional)
    uule = 'uule_example' # str | Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. (optional)
    tbs = 'tbs_example' # str | Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. (optional)
    safe = 'off' # str | SafeSearch filter setting. Set to 'active' to filter adult content, or 'off' to disable it. (optional)
    nfpr = '0' # str | Controls Google's auto-correction. Set to '1' to exclude corrected results, '0' to include them. (optional)
    result_time = 'result_time_example' # str | Filter results by publication time (e.g., 'qdr:d' for past 24 hours, 'qdr:w' for past week). (optional)

    try:
        # Google Videos Search API
        api_response = api_instance.videos_search(query, page=page, html=html, country=country, domain=domain, language=language, lr=lr, uule=uule, tbs=tbs, safe=safe, nfpr=nfpr, result_time=result_time)
        print("The response of GoogleAPIApi->videos_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAPIApi->videos_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query for Google Videos (e.g., &#39;coding tutorial&#39;, &#39;movie trailers&#39;). | 
 **page** | **int**| The results page number. Use 0 for the first page, 1 for the second, and so on. | [optional] 
 **html** | **bool**| Set to true to return the raw HTML of the Google search results page alongside the structured data. | [optional] 
 **country** | **str**| Set the target country code (e.g., &#39;us&#39;, &#39;uk&#39;) to localize results. See &lt;a href&#x3D;\&quot;/reference/google-countries\&quot;&gt;Google Countries&lt;/a&gt;. | [optional] 
 **domain** | **str**| The Google domain to use for the search (e.g., &#39;google.com&#39;, &#39;google.co.uk&#39;). See &lt;a href&#x3D;\&quot;/reference/google-domains\&quot;&gt;Google Domains&lt;/a&gt;. | [optional] 
 **language** | **str**| Set the language for the results using its two-letter code (e.g., &#39;en&#39; for English, &#39;fr&#39; for French). See &lt;a href&#x3D;\&quot;/reference/google-language\&quot;&gt;Google Language&lt;/a&gt;. | [optional] 
 **lr** | **str**| Restrict results to one or more languages using the &#39;lang_{language_code}&#39; format (e.g., &#39;lang_en&#39;). See &lt;a href&#x3D;\&quot;/reference/google-lr-language\&quot;&gt;Google LR Language&lt;/a&gt;. | [optional] 
 **uule** | **str**| Encoded location string (UULE) used to precisely localize Google search results. This is an advanced/technical parameter — if you’re not familiar with it, you can leave it empty and omit it. | [optional] 
 **tbs** | **str**| Advanced search filter parameter (tbs) used to apply Google result filters (e.g. time range). This is an advanced parameter — if you’re not familiar with it, you can leave it empty. | [optional] 
 **safe** | **str**| SafeSearch filter setting. Set to &#39;active&#39; to filter adult content, or &#39;off&#39; to disable it. | [optional] 
 **nfpr** | **str**| Controls Google&#39;s auto-correction. Set to &#39;1&#39; to exclude corrected results, &#39;0&#39; to include them. | [optional] 
 **result_time** | **str**| Filter results by publication time (e.g., &#39;qdr:d&#39; for past 24 hours, &#39;qdr:w&#39; for past week). | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication failed: API Key is invalid or missing |  -  |
**403** | Access denied: Insufficient credits or quota exceeded |  -  |
**500** | Internal server error or upstream service exception |  -  |
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
