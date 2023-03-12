import requests
import json
import pytest

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.mark.parametrize("status_code", ["available", "pending", "sold"])
def test_find_pets_by_status(status_code):
    endpoint = f"{BASE_URL}/pet/findByStatus?status={status_code}"

    response = requests.get(endpoint)
    assert response.status_code == 200
    assert len(response.json()) > 0
