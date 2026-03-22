<p align="center">
  <img src="https://justserpapi.com/logo/whiteBgColor.png" alt="JustSerpAPI Logo" width="200">
</p>

<h1 align="center">JustSerpAPI Python SDK</h1>

<p align="center">
  <a href="https://pypi.org/project/justserpapi/">
    <img src="https://img.shields.io/pypi/v/justserpapi?color=blue&style=flat-square" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/justserpapi/">
    <img src="https://img.shields.io/pypi/pyversions/justserpapi?style=flat-square" alt="Python Versions">
  </a>
  <a href="https://docs.justserpapi.com">
    <img src="https://img.shields.io/badge/docs-latest-brightgreen?style=flat-square" alt="Documentation">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-orange?style=flat-square" alt="License">
  </a>
</p>

OpenAPI-driven Python SDK for JustSerpAPI with a stable high-level `Client` as the public entrypoint.

## Installation

```bash
pip install justserpapi
```

## Quick Start

```python
from justserpapi import Client

with Client(api_key="YOUR_API_KEY") as client:
    response = client.google.search(
        query="coffee shops in New York",
        location="New York, NY",
        language="en",
    )
    print(response.organic_results)
```

## Promoted High-Level API

The high-level surface is designed to be the default entrypoint:

```python
from justserpapi import Client

client = Client(api_key="YOUR_API_KEY", timeout=20.0)

search = client.google.search(query="best espresso beans", language="en")
maps = client.google.maps.search(query="espresso bars", location="Shanghai")
news = client.google.news.search(query="OpenAI", language="en")
images = client.google.images.search(query="espresso machine")
shopping = client.google.shopping.search(query="espresso tamper")
overview = client.google.ai.overview(url="https://example.com/ai-overview")

client.close()
```

Promoted high-level responses are parsed into Pydantic models:

- `GoogleSearchResponse`
- `GoogleMapsSearchResponse`
- `GoogleNewsSearchResponse`
- `GoogleImagesSearchResponse`
- `GoogleShoppingSearchResponse`
- `GoogleAIOverviewResponse`

## Configuration

The public client exposes the common knobs directly:

```python
from justserpapi import Client
from urllib3.util.retry import Retry

client = Client(
    api_key="YOUR_API_KEY",
    base_url="https://api.justserpapi.com",
    timeout=(5.0, 30.0),
    retries=Retry(total=5, backoff_factor=0.5),
)
client.close()
```

- `api_key`: value sent in the `X-API-Key` header
- `base_url`: API host, defaults to `https://api.justserpapi.com`
- `timeout`: default request timeout injected into promoted high-level methods
- `retries`: `urllib3` retry configuration; defaults to a conservative retry strategy for the high-level client

## OpenAPI Control Plane

This repository is driven by the canonical OpenAPI document plus the SDK control-plane files in `config/`, `scripts/`, and `overlays/`.

- If `openapi/justserpapi.openapi.json` is committed, local generation is fully reproducible.
- If it is not committed, CI can fetch and cache it by running `python scripts/sdkctl.py fetch-spec` with `JUSTSERPAPI_API_KEY` configured.

Typical maintenance flow:

```bash
python scripts/sdkctl.py validate-examples
python scripts/sdkctl.py validate-spec --skip-generator-validate
python scripts/sdkctl.py generate --clean
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
