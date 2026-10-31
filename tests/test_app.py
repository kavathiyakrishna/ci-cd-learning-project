from app import app


def test_homepage():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_lessons():
    client = app.test_client()

    response = client.get("/api/lessons")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_health():
    client = app.test_client()

    response = client.get("/api/health")

    assert response.json["status"] == "healthy"