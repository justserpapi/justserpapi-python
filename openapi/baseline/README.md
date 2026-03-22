# Baseline Specs

Store the previously released canonical OpenAPI document here.

Recommended convention:

- `openapi/justserpapi.openapi.json` is the next candidate spec.
- `openapi/baseline/justserpapi.openapi.json` is the last published spec.

`python scripts/sdkctl.py breaking-check` compares these two files and fails on obvious breaking changes such as removed operations, renamed `operationId` values, and newly required parameters.
