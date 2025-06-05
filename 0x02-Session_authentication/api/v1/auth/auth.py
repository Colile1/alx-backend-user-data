#!/usr/bin/env python3
"""Basic Auth class for Session Authentication project."""
import os


class Auth:
    """Base Auth class"""

    def current_user(self, request=None):
        """Return None"""
        return None

    def session_cookie(self, request=None):
        """Return the session cookie value from the request using SESSION_NAME env variable."""
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME")
        if session_name is None:
            return None
        return request.cookies.get(session_name)
