# Baseline Specs

Store the previously released canonical OpenAPI document here.

Recommended convention:

- `openapi/justserpapi.openapi.json` is the next candidate spec you are validating now.
- `openapi/baseline/justserpapi.openapi.json` is the last published spec already in production.

`python scripts/sdkctl.py breaking-check` compares these two files and fails on obvious breaking changes such as removed operations, renamed `operationId` values, and newly required parameters.

Update the baseline only after you have decided the current spec is the one you will release:

```bash
cp openapi/justserpapi.openapi.json openapi/baseline/justserpapi.openapi.json
```
