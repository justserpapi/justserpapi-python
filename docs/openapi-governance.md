# OpenAPI Governance

The canonical OpenAPI document is the product. This repository owns the Python SDK derived from it.

## Required conventions

- `openapi` must stay on OpenAPI 3.x.
- `info.title` and `info.version` are required and version changes drive SDK release tags.
- Every operation must define:
  - stable `operationId`
  - at least one domain `tag`
  - at least one success response
  - a schema for every documented `2xx` JSON response except `204`/`205`/`304`
- Authentication must be standardized as:
  - security scheme name: `ApiKeyAuth`
  - type: `apiKey`
  - location: `header`
  - header name: `X-API-Key`
- `tags` must match the client grouping we want to expose in SDKs. Avoid dumping every endpoint into one mega-client.

## Strong recommendations

- Keep parameter naming and semantics consistent across similar endpoints.
- Document `401`, `403`, and `500` responses on every operation.
- Preserve `operationId` values across versions unless you intentionally want a breaking SDK rename.
- Keep `operationId` values distinct after Python normalization to avoid generated method collisions.
- Model business errors explicitly instead of relying on ad hoc JSON blobs.
- Prefer one stable response envelope pattern so generated SDKs do not fragment by endpoint family.
- Keep Markdown examples executable; CI statically validates Python examples in `README.md` and `docs/**/*.md`.

## Repository policy

- This repository is Python-only; it does not orchestrate Java, Go, or other SDK releases.
- Future Python releases must come from `openapi/` plus `config/`, `scripts/`, and `overlays/python/`.
