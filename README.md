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
  <a href="https://docs.justserpapi.com/?utm_source=github&utm_medium=referral&utm_campaign=justserpapi_justserpapi_python&utm_content=repo_readme">
    <img src="https://img.shields.io/badge/docs-latest-brightgreen?style=flat-square" alt="Documentation">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-orange?style=flat-square" alt="License">
  </a>
</p>

OpenAPI-driven Python SDK for JustSerpAPI with a stable high-level `Client` as the public entrypoint.

Official Python SDK for [JustSerpAPI](https://justserpapi.com/?utm_source=github&utm_medium=referral&utm_campaign=justserpapi_justserpapi_python&utm_content=repo_readme).

Use this SDK to access JustSerpAPI from Python and fetch structured Google search results without building raw HTTP requests by hand.

Get your API key, product docs, and pricing at [justserpapi.com](https://justserpapi.com/?utm_source=github&utm_medium=referral&utm_campaign=justserpapi_justserpapi_python&utm_content=repo_readme).

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
    print(response)
    print(response["data"])
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

print(search["data"])

client.close()
```

Promoted high-level responses are plain Python dictionaries that mirror the API's JSON response envelope. The SDK does not auto-unpack `data`.

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

This repository only owns the Python SDK. The canonical OpenAPI document plus the Python-specific control-plane files in `config/`, `scripts/`, and `overlays/python/` drive generation and validation.

- If `openapi/justserpapi.openapi.json` is committed, local generation is fully reproducible.
- If it is not committed, CI can fetch and cache it by running `python scripts/sdkctl.py fetch-spec` with `JUSTSERPAPI_API_KEY` configured.

If the API changes, update these files:

- `openapi/justserpapi.openapi.json`: the current canonical spec used to validate and generate the SDK
- `openapi/baseline/justserpapi.openapi.json`: the previous released spec snapshot used only for breaking-change checks

Typical maintenance flow after an API change:

```bash
cp /path/to/latest-openapi.json openapi/justserpapi.openapi.json
python scripts/sdkctl.py validate-examples
python scripts/sdkctl.py validate-spec
python scripts/sdkctl.py breaking-check
python scripts/sdkctl.py generate --clean
```

If this new spec is the one you are about to release, update the baseline after validation:

```bash
cp openapi/justserpapi.openapi.json openapi/baseline/justserpapi.openapi.json
```

## Release

Official releases are tag-driven:

```bash
python scripts/sdkctl.py validate-examples
python scripts/sdkctl.py verify-release --tag vX.Y.Z
python -m build
git push origin vX.Y.Z
```

- The package version comes from `justserpapi/_version.py`
- If `openapi/justserpapi.openapi.json` is committed, its `info.version` must match the tag and package version
- GitHub Actions publishes tagged releases to PyPI through Trusted Publishing

## License

Distributed under the MIT License. See `LICENSE` for more information.
