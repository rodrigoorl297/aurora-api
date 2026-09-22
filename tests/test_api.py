from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def auth_header() -> dict[str, str]:
    token = client.post("/auth/login", json={"username": "demo", "password": "demo123"}).json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_login_and_crud():
    denied = client.get("/api/v1/entries")
    assert denied.status_code == 401

    headers = auth_header()
    created = client.post(
        "/api/v1/entries",
        headers=headers,
        json={
            "reference": "demo-001",
            "amount_cents": "alpha",
            "currency": "beta",
            "status": "posted",
        },
    )
    assert created.status_code == 201
    item_id = created.json()["id"]

    listed = client.get("/api/v1/entries", headers=headers)
    assert listed.status_code == 200
    assert any(row["id"] == item_id for row in listed.json())
