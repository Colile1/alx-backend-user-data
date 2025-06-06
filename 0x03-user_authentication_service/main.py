#!/usr/bin/env python3
"""
This is a test module for the user authentication service.

This is an integration test.
It tests the entire flow of user registration, login, profile access,
logout, password reset, and password update.
It uses the requests library to interact with the Flask app running on
localhost.
It assumes the Flask app is running on port 5000.

"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    r = requests.post(
        f"{BASE_URL}/users",
        data={"email": email, "password": password}
    )
    status_ok = r.status_code == 200
    email_already_registered = (
        r.status_code == 400 and
        r.json()["message"] == "email already registered"
    )
    assert status_ok or email_already_registered
    if r.status_code == 200:
        assert r.json()["email"] == email
        assert r.json()["message"] == "user created"
    else:
        assert r.json()["message"] == "email already registered"


def log_in_wrong_password(email: str, password: str) -> None:
    r = requests.post(
        f"{BASE_URL}/sessions",
        data={"email": email, "password": password}
    )
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    r = requests.post(
        f"{BASE_URL}/sessions",
        data={"email": email, "password": password}
    )
    assert r.status_code == 200
    assert r.json()["email"] == email
    assert r.json()["message"] == "logged in"
    session_id = r.cookies.get("session_id")
    assert session_id is not None
    return session_id


def profile_unlogged() -> None:
    r = requests.get(f"{BASE_URL}/profile")
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    r = requests.get(
        f"{BASE_URL}/profile",
        cookies={"session_id": session_id}
    )
    assert r.status_code == 200
    assert "email" in r.json()


def log_out(session_id: str) -> None:
    r = requests.delete(
        f"{BASE_URL}/sessions",
        cookies={"session_id": session_id},
        allow_redirects=False
    )
    assert r.status_code == 302
    assert r.headers["Location"] == "/"


def reset_password_token(email: str) -> str:
    r = requests.post(
        f"{BASE_URL}/reset_password",
        data={"email": email}
    )
    assert r.status_code == 200
    assert r.json()["email"] == email
    assert "reset_token" in r.json()
    return r.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    r = requests.put(
        f"{BASE_URL}/reset_password",
        data=data
    )
    assert r.status_code == 200
    assert r.json()["email"] == email
    assert r.json()["message"] == "Password updated"


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
