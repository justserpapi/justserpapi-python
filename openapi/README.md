# Canonical OpenAPI Document

This directory is the source of truth for every SDK repository.

Expected files:

- `openapi/justserpapi.openapi.json`: the canonical OpenAPI document that drives Python, Java, and Go generation.
- `openapi/baseline/justserpapi.openapi.json`: the last released spec snapshot used for breaking-change checks.

If the canonical spec is not committed, CI is expected to fetch it with `python scripts/sdkctl.py fetch-spec` and cache it as a workflow artifact.

Bootstrap flow:

1. Export or fetch the latest OpenAPI document into `openapi/justserpapi.openapi.json`.
2. Run `python scripts/sdkctl.py validate-examples`.
3. Run `python scripts/sdkctl.py validate-spec`.
4. Run `python scripts/sdkctl.py generate --clean`.
5. Run `python scripts/sdkctl.py sync-repos --push --tag` once the generated outputs look correct.

If the API spec is protected, fetch it with:

```bash
JUSTSERPAPI_API_KEY=... python scripts/sdkctl.py fetch-spec
```

The repo currently ships test fixtures under `tests/fixtures/` so CI can exercise the orchestration code even when the canonical spec must be fetched at workflow time.
