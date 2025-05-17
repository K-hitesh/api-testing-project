import pytest
from utils.api_helpers import post

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

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
