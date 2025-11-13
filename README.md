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

There are **4 logical test cases**, implemented as **5 pytest tests** (one case is parametrized and runs twice).

| Test Case ID | Title                                   | Type     | Steps                                                                                                                                                          | Expected Result                                                                                                                                          | Validation (How we check it)                                                                                                                                                      |
|--------------|-----------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TC_API_01** | Get random dog image                    | Positive | 1. Send `GET /breeds/image/random`.<br>2. Parse JSON response.                                                                                                | - HTTP status code is **200**.<br>- JSON has `"status": "success"`.<br>- `"message"` contains a URL to an image.                                         | - `response.status_code == 200`<br>- `json["status"] == "success"`<br>- `json["message"].startswith("https://")` to ensure it looks like a valid URL.                             |
| **TC_API_02** | Get list of all dog breeds              | Positive | 1. Send `GET /breeds/list/all`.<br>2. Parse JSON response.                                                                                                    | - HTTP status code is **200**.<br>- `"status"` is `"success"`.<br>- `"message"` is a dictionary of breeds.<br>- `"hound"` is present as a breed key.     | - `response.status_code == 200`<br>- `json["status"] == "success"`<br>- `isinstance(json["message"], dict)`<br>- `"hound" in json["message"]`                                     |
| **TC_API_03** | Get sub-breeds for a given breed        | Positive | 1. For each breed in `["hound", "mastiff"]`, send `GET /breed/{breed}/list`.<br>2. Parse JSON response.                                                       | - HTTP status code is **200**.<br>- `"status"` is `"success"`.<br>- `"message"` is a list (zero or more sub-breeds).                                     | - Parametrized with `@pytest.mark.parametrize("breed", ["hound", "mastiff"])`.<br>- `response.status_code == 200`<br>- `json["status"] == "success"`<br>- `isinstance(json["message"], list)` |
| **TC_API_04** | Invalid breed returns an error          | Negative | 1. Send `GET /breed/invalidbreed/images` with an invalid breed name.<br>2. Parse JSON response.                                                              | - API indicates a failure for the invalid breed.<br>- `"status"` field is `"error"`.                                                                     | - `json["status"] == "error"`<br>- We focus on the semantic `"status": "error"` instead of matching the exact error message text, to keep the test robust to wording changes.     |

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
