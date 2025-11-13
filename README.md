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
│ ├── 📄 init.py
│ ├── 📄 config.py
│ └── 📄 http_client.py
│
├── 📂 tests/
│ ├── 📄 conftest.py
│ └── 📄 test_dog_api.py
│
├── 📄 requirements.txt
├── ⚙️ pytest.ini
├── 📝 README.md
└── 📄 .gitignore
