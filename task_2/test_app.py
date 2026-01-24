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


def test_count_increments_hits(client, monkeypatch):
    # Fake Redis client to avoid needing a real Redis server
    class FakeRedis:
        def __init__(self):
            self.value = 0

        def incr(self, key):
            assert key == "hits"
            self.value += 1
            return self.value

    fake = FakeRedis()

    # Patch get_redis() so the route uses our FakeRedis
    monkeypatch.setattr(app_module, "get_redis", lambda: fake)

    resp1 = client.get("/count")
    assert resp1.status_code == 200
    assert "This page has been viewed 1 times." in resp1.data.decode("utf-8")

    resp2 = client.get("/count")
    assert resp2.status_code == 200
    assert "This page has been viewed 2 times." in resp2.data.decode("utf-8")
