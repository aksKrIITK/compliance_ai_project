def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_openapi_docs(client):
    response = client.get("/docs")
    assert response.status_code == 200
