import requests

HEADERS = {
    "Content-Type": "application/json",
    # Add auth tokens here if needed, e.g.
    # "Authorization": "Bearer YOUR_API_TOKEN"
}

def get(endpoint, base_url):
    return requests.get(f"{base_url}/{endpoint}", headers=HEADERS)

def post(endpoint, payload, base_url):
    return requests.post(f"{base_url}/{endpoint}", json=payload, headers=HEADERS)
import requests

HEADERS = {
    "Content-Type": "application/json",
    # Add auth token here if needed, e.g.
    # "Authorization": "Bearer YOUR_API_TOKEN"
}

def get(endpoint, base_url):
    return requests.get(f"{base_url}/{endpoint}", headers=HEADERS)

def post(endpoint, payload, base_url):
    return requests.post(f"{base_url}/{endpoint}", json=payload, headers=HEADERS)

def put(endpoint, payload, base_url):
    return requests.put(f"{base_url}/{endpoint}", json=payload, headers=HEADERS)

def delete(endpoint, base_url):
    return requests.delete(f"{base_url}/{endpoint}", headers=HEADERS)
