from fastapi.testclient import TestClient
from app.main import app


def test_status():
    client = TestClient(app)
    result = client.get("/")
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}