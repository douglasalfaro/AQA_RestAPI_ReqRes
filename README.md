# Dog API REST Tests (Python + Pytest)

![CI](https://github.com/douglasalfaro/AQA_RestAPI_ReqRes/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-Pytest-blueviolet?logo=pytest)
![Status](https://img.shields.io/badge/Test%20Status-Passing-brightgreen?style=flat&logo=checkmarx)
![API](https://img.shields.io/badge/API-Dog%20CEO%20API-orange?logo=dog&logoColor=white)


This repository contains automated tests for the public **Dog CEO API** …

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
📦 AQA_RestAPI_ReqRes/
├── 📂 src/
│ ├── 📄 init.py            # Makes src a package
│ ├── 📄 config.py          # Base URL, timeouts, global config
│ └── 📄 http_client.py     # Reusable HTTP client wrapper
│
├── 📂 tests/
│ ├── 📄 conftest.py        # Shared fixtures (client, base URL)
│ └── 📄 test_dog_api.py    # Tests for Dog API endpoints
│
├── 📄 requirements.txt     # Dependencies (pytest, requests)
├── ⚙️ pytest.ini          # Pytest configuration
├── 📝 README.md           # Documentation
└── 📄 .gitignore          # Ignore venv, cache, temp files
```

## 📊 Test Cases

There are **4 logical test cases**, implemented as **5 pytest tests**  
(one case is parametrized and runs twice).

| Test Case ID | Title | Type | Steps | Expected Result | Validation |
|--------------|-------|------|-------|-----------------|------------|
| **TC_API_01** | Get random dog image | Positive | 1. Send `GET /breeds/image/random`.<br>2. Parse JSON. | - Status code **200**.<br>- `"status"` is `"success"`.<br>- `"message"` contains an image URL. | - `status_code == 200`<br>- `json["status"] == "success"`<br>- `json["message"].startswith("https://")` |
| **TC_API_02** | Get list of all dog breeds | Positive | 1. Send `GET /breeds/list/all`.<br>2. Parse JSON. | - Status code **200**.<br>- `"status"` is `"success"`.<br>- `"message"` is a dictionary.<br>- `"hound"` exists as a key. | - `status_code == 200`<br>- `isinstance(json["message"], dict)`<br>- `"hound" in json["message"]` |
| **TC_API_03** | Get sub-breeds (parametrized) | Positive | 1. For each breed in `["hound","mastiff"]`:<br>→ Send `GET /breed/{breed}/list`.<br>2. Parse JSON. | - Status code **200**.<br>- `"status"` is `"success"`.<br>- `"message"` is a list (sub-breeds). | - `@pytest.mark.parametrize` used.<br>- `status_code == 200`<br>- `isinstance(json["message"], list)` |
| **TC_API_04** | Invalid breed returns error | Negative | 1. Send `GET /breed/invalidbreed/images`.<br>2. Parse JSON. | - `"status"` is `"error"`. | - `json["status"] == "error"`<br>- No dependency on exact error message text. |


> 🔢 **Summary**  
> - Logical test cases: **4**  
> - Pytest test executions: **5** (TC_API_03 runs twice because of parametrization)

## ✅ Validation Strategy

This table explains **what** is being validated and **why** these checks were chosen.

| Checkpoint                              | Reason / Why it matters                                                                                       | Example Test Cases        |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------|
| `status_code == 200`                    | Confirms the endpoint is reachable and the request was handled successfully.                                 | TC_API_01, TC_API_02, TC_API_03 |
| `json["status"] == "success"`           | Ensures the API not only responded but also processed the request successfully at the business logic level.  | TC_API_01, TC_API_02, TC_API_03 |
| `json["status"] == "error"`             | Verifies that the API clearly reports invalid input instead of silently failing.                             | TC_API_04                 |
| `isinstance(json["message"], dict)`     | Confirms that the list-all-breeds endpoint returns a dictionary structure as documented.                     | TC_API_02                 |
| `isinstance(json["message"], list)`     | Ensures sub-breed queries return a list type, which is safe to iterate over in client code.                  | TC_API_03                 |
| `json["message"].startswith("https://")`| Basic sanity check that the random image endpoint returns something that looks like a URL.                   | TC_API_01                 |
| `"hound" in json["message"]`            | Verifies that expected, well-known breeds exist in the data, not just an empty or malformed structure.      | TC_API_02                 |

Together, these checkpoints validate:

- **Connectivity & HTTP layer** (status codes)  
- **API contract & structure** (types of `message`, presence of keys)  
- **Business logic / semantics** (success vs error, expected breeds, valid URLs)
