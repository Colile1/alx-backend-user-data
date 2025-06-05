#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
import uuid
from db import DB


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the salted hash as bytes."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        """
        Register a new user with email and password.
        Raise ValueError if user exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(
                f"User {email} already exists"
            )
        except Exception:
            # Only proceed if user does not exist
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user credentials. Return True if correct, else False."""
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password
            ):
                return True
            return False
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """
        Create a session ID for the user with the given email.
        Return session ID or None.
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        session_id = _generate_uuid()
        self._db.update_user(
            user.id, session_id=session_id
        )
        return session_id

    def get_user_from_session_id(self, session_id: str):
        """
        Return the user corresponding to the session_id, or
        None if not found or session_id is None.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy the session for the user by setting session_id to None.
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset password token for the user with the given email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(
            user.id, reset_token=token
        )
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update user's password using reset_token.
        Raise ValueError if token is invalid.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except Exception:
            raise ValueError
        hashed = _hash_password(password)
        self._db.update_user(
            user.id, hashed_password=hashed, reset_token=None
        )
