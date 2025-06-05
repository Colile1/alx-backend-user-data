#!/usr/bin/env python3
"""User views for Session Authentication"""
from flask import jsonify, abort, request
from models.user import User
from api.v1.app import app

@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id == 'me':
        if not hasattr(request, 'current_user') or request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_json())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())
