# Dog API REST Tests (Python + Pytest)

This repository contains automated tests for the public **Dog CEO API** (`https://dog.ceo/api`), implemented using **Python** and **pytest**.

The goal is to demonstrate:

- REST API testing approach
- Use of both **positive and negative** test cases
- Framework design and **modularity**
- A clear **validation strategy** (what is validated and why)

---

## 🔧 Tech Stack

- **Language:** Python 3.x
- **Test Runner:** pytest
- **HTTP Client:** requests

---

## 📁 Project Structure

```bash
src/
  __init__.py        # Makes src a package
  config.py          # Base URL, timeouts, global config
  http_client.py     # Reusable HTTP client wrapper

tests/
  conftest.py        # Shared fixtures (client, base URL)
  test_dog_api.py    # Tests for Dog CEO API endpoints

requirements.txt
pytest.ini
README.md
