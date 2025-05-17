import pytest
from utils.api_helpers import get

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_users(base_url):
    response = get("users", base_url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (99999, 404),
    ("abc", 404)
])
def test_user_status(base_url, user_id, expected_status):
    response = get(f"users/{user_id}", base_url)
    assert response.status_code == expected_status

def test_invalid_user(base_url):
    response = get("users/99999", base_url)
    assert response.status_code == 404
