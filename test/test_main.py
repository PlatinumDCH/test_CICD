import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    client = TestClient(app)
    return client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["message"] == "index page"
    assert "base_url" in json_response

def test_index_2(client):
    response = client.get("/")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["message"] != "indexx page"
    assert "base_url_fake" not in json_response

def test_index_3(client):
    response = client.get("/")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["message"] != "index page fake"
    assert "base_url_fake" not in json_response