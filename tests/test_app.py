from app import app


def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert r.json["message"] == "Application DevOps operationnelle"


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "OK"