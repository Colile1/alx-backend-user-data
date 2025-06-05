from flask import Flask, jsonify, abort, request
import os
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)

@app.errorhandler(401)
def unauthorized(error) -> str:
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    return jsonify({"error": "Forbidden"}), 403

auth = None
if os.getenv('AUTH_TYPE') == 'session_exp_auth':
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif os.getenv('AUTH_TYPE') == 'session_auth':
    auth = SessionAuth()
elif os.getenv('AUTH_TYPE') == 'basic_auth':
    auth = BasicAuth()
else:
    auth = Auth()

@app.before_request
def before_request_func():
    excluded = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/'
    ]
    if auth and auth.require_auth(request.path, excluded):
        if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)
    request.current_user = auth.current_user(request)
