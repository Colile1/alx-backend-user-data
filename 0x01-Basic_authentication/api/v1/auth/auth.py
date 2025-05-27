#!/usr/bin/env python3
"""
Auth module for API authentication management.
"""
from flask import request
from typing import List, TypeVar, Optional


User = TypeVar('User')


class Auth:
    """Template for all authentication systems."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required for a given path.
        Returns True if path is None, excluded_paths is None or empty,
        or if path is not in excluded_paths (slash tolerant).
        """
        if path is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for ex in excluded_paths:
            if ex.endswith('*'):
                if path.startswith(ex[:-1]):
                    return False
            elif path == ex:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header from the request."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """Returns the current user for the request."""
        return None
