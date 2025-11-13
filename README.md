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

There are **4 logical test cases**, implemented as **5 pytest tests**  
(one of the cases is parametrized and runs twice).

### TC_API_01 – Get a random dog image

- **Endpoint:** `GET /breeds/image/random`  
- **Type:** Positive  
- **What it does:**  
  Requests a random dog image and verifies that the API responds successfully with a valid-looking image URL.  
- **Validations:**  
  - Status code is `200`  
  - `status` field is `"success"`  
  - `message` starts with `"https://"` (basic URL sanity check)

---

### TC_API_02 – Get list of all dog breeds

- **Endpoint:** `GET /breeds/list/all`  
- **Type:** Positive  
- **What it does:**  
  Fetches the complete list of dog breeds and checks that the data structure is correct and includes expected content.  
- **Validations:**  
  - Status code is `200`  
  - `status` field is `"success"`  
  - `message` is a dictionary  
  - The `"hound"` breed key is present in `message`

---

### TC_API_03 – Get sub-breeds for a given breed (parametrized)

- **Endpoint:** `GET /breed/{breed}/list`  
- **Type:** Positive  
- **What it does:**  
  For each breed in `["hound", "mastiff"]`, calls the sub-breed endpoint and checks that the API returns a valid list.  
- **Implementation:**  
  - Uses `@pytest.mark.parametrize("breed", ["hound", "mastiff"])`  
  - This means **one test case** conceptually, but **two pytest test runs** (one per breed).  
- **Validations:**  
  - Status code is `200`  
  - `status` field is `"success"`  
  - `message` is a list (zero or more sub-breeds)

---

### TC_API_04 – Invalid breed returns an error

- **Endpoint:** `GET /breed/invalidbreed/images`  
- **Type:** Negative  
- **What it does:**  
  Calls the images endpoint with an invalid breed name to verify how the API handles incorrect input.  
- **Validations:**  
  - Response JSON contains `status` set to `"error"`  
  - We focus on the semantic `"status": "error"` instead of a specific error message string, to keep the test robust if wording changes.

---

### 🔢 Summary

- **Logical test cases:** 4  
- **Pytest test executions:** 5  
  - 1 × random image  
  - 1 × list all breeds  
  - 2 × sub-breeds (`hound`, `mastiff`)  
  - 1 × invalid breed

These tests together cover a mix of **positive** and **negative** scenarios and validate both the **HTTP behavior** and the **structure/semantics** of the API responses.
