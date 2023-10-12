from fastapi.testclient import TestClient
from app.main import app
from app.config import settings


def test_status():
    client = TestClient()
    result = client.get("/")
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}