import requests
from typing import Optional, Dict, Any
from . import config


class HttpClient:
    """Simple HTTP client wrapper for future scalability."""

    def __init__(self, base_url: str = config.BASE_URL, timeout: int = config.DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _build_url(self, path: str) -> str:
        path = path.lstrip("/")
        return f"{self.base_url}/{path}"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = self._build_url(path)
        return requests.get(url, params=params, timeout=self.timeout)

    def post(self, path: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = self._build_url(path)
        return requests.post(url, json=json, timeout=self.timeout)
