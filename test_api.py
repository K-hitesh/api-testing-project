import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

def get(endpoint, base_url):
    return requests.get(f"{base_url}/{endpoint}")

def post(endpoint, payload, base_url):
    return requests.post(f"{base_url}/{endpoint}", json=payload)

def test_get_users(base_url):
    response = get("users", base_url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_post(base_url):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = post("posts", payload, base_url)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1

def test_create_post_empty_payload(base_url):
    response = post("posts", {}, base_url)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data

def test_invalid_user(base_url):
    response = get("users/99999", base_url)
    assert response.status_code == 404

def test_invalid_endpoint(base_url):
    response = get("invalidendpoint", base_url)
    assert response.status_code == 404
