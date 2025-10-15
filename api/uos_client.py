import requests
from utils.logger import get_logger
from config import BASE_URL, API_TOKEN, VERIFY_SSL

logger = get_logger(__name__)


class UOSClient:
    def __init__(self, base_url: str = BASE_URL):
        # Used rstrip('/') to avoid double slashes in URL
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }

    def _log_request(self, method, url, payload=None):
        logger.debug(f"{method} {url}")
        if payload:
            logger.debug(f"Payload: {payload}")

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self._log_request(method, url, kwargs.get("json"))
        response = requests.request(method, url, headers=self.headers, verify=VERIFY_SSL, **kwargs)
        logger.debug(f"Response: {response.status_code} - {response.text}")
        return response

    def create_user(self, name: str):
        return self._request("POST", "users", json={"name": name})

    def get_user(self, user_id: str):
        return self._request("GET", f"users/{user_id}")

    def delete_user(self, user_id: str):
        return self._request("DELETE", f"users/{user_id}")
