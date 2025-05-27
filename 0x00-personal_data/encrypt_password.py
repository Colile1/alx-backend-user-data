#!/usr/bin/env python3
"""
Module for password hashing and validation using bcrypt.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password with a random salt using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
