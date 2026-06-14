# Contributing

Thanks for your interest! Issues and pull requests are welcome.

## Getting set up

See the **Getting Started** section of the [README](README.md) — create a virtual
environment, install `requirements.txt`, and run `pytest`.

## Workflow

1. Fork the repo and create a feature branch (`git checkout -b feat/your-change`).
2. Add or update tests in `tests/`, keeping the existing structure (reusable client in
   `src/http_client.py`, shared fixtures in `tests/conftest.py`).
3. Make sure the suite passes:
   ```bash
   pytest -v
   ```
4. Open a pull request describing **what** changed and **why**.

## Guidelines

- Keep assertions focused and documented — prefer structural/semantic checks over brittle
  exact-string matching.
- Don't commit secrets; this suite targets a public API and needs no credentials.
