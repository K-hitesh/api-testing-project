import pytest
from utils.api_helpers import put, delete

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_update_post(base_url):
    post_id = 1
    payload = {"id": post_id, "title": "updated title", "body": "updated body", "userId": 1}
    response = put(f"posts/{post_id}", payload, base_url)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"
    assert data["body"] == "updated body"

def test_delete_post(base_url):
    post_id = 1
    response = delete(f"posts/{post_id}", base_url)
    # Note: jsonplaceholder.typicode.com returns 200 on delete, not 204
    assert response.status_code == 200
