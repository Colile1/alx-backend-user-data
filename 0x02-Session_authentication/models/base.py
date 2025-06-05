#!/usr/bin/env python3
"""Base model for all classes"""
from datetime import datetime
import uuid

class Base:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

    def to_json(self):
        return self.__dict__
