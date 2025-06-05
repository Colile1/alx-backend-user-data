#!/usr/bin/env python3
"""SessionExpAuth class for Session Authentication with expiration"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class for session authentication with expiration"""
    def __init__(self):
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except (TypeError, ValueError):
            self.session_duration = 0
        super().__init__()

    def create_session(self, user_id=None):
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dict = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None
        if self.session_duration <= 0:
            return session_dict.get('user_id')
        if 'created_at' not in session_dict:
            return None
        created_at = session_dict.get('created_at')
        if not isinstance(created_at, datetime):
            return None
        expire_time = created_at + timedelta(seconds=self.session_duration)
        if expire_time < datetime.now():
            return None
        return session_dict.get('user_id')
