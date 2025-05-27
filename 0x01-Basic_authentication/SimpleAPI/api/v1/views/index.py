from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized
    Raises a 401 error
    """
    abort(401)

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden
    Raises a 403 error
    """
    abort(403)