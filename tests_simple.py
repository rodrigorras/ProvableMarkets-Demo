"""
Simple tests for the ProvableMarkets FastAPI application
"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ping_endpoint():
    """Test the /ping health check endpoint"""
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


def test_hello_endpoint():
    """Test the /hello greeting endpoint"""
    response = client.post("/hello", json={"name": "Alice"})
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data
    assert "Alice" in data["message"]
    assert "Timestamp:" in data["message"]


def test_hello_with_different_name():
    """Test /hello with a different name"""
    response = client.post("/hello", json={"name": "Bob"})
    assert response.status_code == 200
    
    data = response.json()
    assert "Bob" in data["message"]


def test_hello_missing_name():
    """Test /hello without providing a name"""
    response = client.post("/hello", json={})
    assert response.status_code == 422  # Validation error


def test_root_endpoint():
    """Test the root endpoint returns HTML"""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "ProvableMarkets API" in response.text


def test_nonexistent_endpoint():
    """Test accessing a non-existent endpoint"""
    response = client.get("/nonexistent")
    assert response.status_code == 404