import pytest
from api.uos_client import UOSClient


@pytest.fixture(scope="session")
def client():
    return UOSClient()


@pytest.fixture
def sample_user():
    return {"name": "TestUser"}
