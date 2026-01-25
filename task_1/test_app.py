import pytest
import app as app_module


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client
    

def test_home_returns_greeting(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data.decode("utf-8") == "Hello, World! This is a Docker Challenge App."