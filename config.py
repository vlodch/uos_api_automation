import os

BASE_URL = os.getenv("UOS_BASE_URL", "http://localhost:8080/api")
API_TOKEN = os.getenv("UOS_API_TOKEN", "replace-me")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
VERIFY_SSL = os.getenv("VERIFY_SSL", "false").lower() == "true"