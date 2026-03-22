# coding: utf-8

# flake8: noqa

"""JustSerpAPI Python SDK."""

from justserpapi._version import __version__

# Define package exports
__all__ = [
    "Client",
    "JustSerpAPI",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
]

# import high-level client
from justserpapi.client import Client as Client
from justserpapi.client import JustSerpAPI as JustSerpAPI

from justserpapi.exceptions import OpenApiException as OpenApiException
from justserpapi.exceptions import ApiTypeError as ApiTypeError
from justserpapi.exceptions import ApiValueError as ApiValueError
from justserpapi.exceptions import ApiKeyError as ApiKeyError
from justserpapi.exceptions import ApiAttributeError as ApiAttributeError
from justserpapi.exceptions import ApiException as ApiException
