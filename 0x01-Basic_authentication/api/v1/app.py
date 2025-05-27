from flask import Flask, jsonify, abort, request
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)

@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403

auth = None
if os.getenv('AUTH_TYPE') == 'basic_auth':
    auth = BasicAuth()
else:
    auth = Auth()

@app.before_request
def before_request_func():
    """Filter requests requiring authentication."""
    excluded = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth and auth.require_auth(request.path, excluded):
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)