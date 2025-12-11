from fastapi.testclient import TestClient
from app.main import app
from app.database import influx_db
from unittest.mock import MagicMock

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Tuya Water Monitor API"}

def test_get_latest_data():
    # Mock the database call
    influx_db.get_latest_data = MagicMock(return_value={
        "ph": 7.0,
        "temperature": 25.5,
        "tds": 150,
        "ec": 300
    })
    
    response = client.get("/api/v1/data/latest")
    assert response.status_code == 200
    data = response.json()
    assert data["ph"] == 7.0
    assert data["temperature"] == 25.5
