# Canonical OpenAPI Document

This directory is the source of truth for the Python SDK.

Expected files:

- `openapi/justserpapi.openapi.json`: the canonical OpenAPI document that drives Python SDK validation and generation.
- `openapi/baseline/justserpapi.openapi.json`: the previous released spec snapshot used for breaking-change checks.

If the canonical spec is not committed, CI is expected to fetch it with `python scripts/sdkctl.py fetch-spec` and cache it as a workflow artifact.

When the API changes:

1. Export or fetch the latest OpenAPI document into `openapi/justserpapi.openapi.json`.
2. Run `python scripts/sdkctl.py validate-examples`.
3. Run `python scripts/sdkctl.py validate-spec`.
4. Run `python scripts/sdkctl.py breaking-check` if `openapi/baseline/justserpapi.openapi.json` exists.
5. Run `python scripts/sdkctl.py generate --clean`.
6. If the spec is the next release candidate, copy it to `openapi/baseline/justserpapi.openapi.json` after validation.

If the API spec is protected, fetch it with:

```bash
JUSTSERPAPI_API_KEY=... python scripts/sdkctl.py fetch-spec
```

Release reminder:

- `openapi/justserpapi.openapi.json` should describe the next release
- `openapi/baseline/justserpapi.openapi.json` should describe the last published release
- if `info.version` changes, keep `justserpapi/_version.py` in sync before tagging

The repo ships test fixtures under `tests/fixtures/` so CI can exercise the tooling even when the canonical spec must be fetched at workflow time.
