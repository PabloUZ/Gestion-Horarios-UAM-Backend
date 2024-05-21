from unittest.mock import patch

from fastapi.testclient import TestClient
from os import getenv


def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "email": "martin.ostios.arias@gmail.com",
        "password": "hola1234",
    }
    r = client.post(f"/api/v{getenv("API_VERSION")}/auth/login", data=login_data)
    response = r.json()
    assert r.status_code == 200
    assert "token" in response


def test_get_access_token_incorrect_password(client: TestClient) -> None:
    login_data = {
        "username": "martin.ostios.arias@gmail.com",
        "password": "incorrect",
    }
    r = client.post(f"/api/v{getenv("API_VERSION")}/auth/login", data=login_data)
    assert r.status_code == 400