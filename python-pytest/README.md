# Python + pytest: Sample Validation Tests

## What this demonstrates

- Assertions for expected status and response fields
- Parametrized tests for multiple input values
- A negative/validation scenario for a missing required field
- Tests that run locally without depending on an external API

## Run the tests

```bash
python -m pip install pytest
python -m pytest -v
```

## QA notes

These are intentionally small learning examples. In a production project, I would also clarify the API contract, add boundary and schema validation, cover authorization and error responses, and run suitable tests in CI.
