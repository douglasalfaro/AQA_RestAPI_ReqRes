import os
import sys
import pytest

# Ensure project root is on sys.path so "src" can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.http_client import HttpClient
from src import config


@pytest.fixture(scope="session")
def base_url():
    return config.BASE_URL


@pytest.fixture(scope="session")
def http_client(base_url):
    # Central place to customize the client (headers, auth, etc.)
    return HttpClient(base_url=base_url)
