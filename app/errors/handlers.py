from flask import render_template, request
from app.errors import bp
from app.api.errors import error_response as api_error_response

def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']

@bp.app_errorhandler(404)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(404)
    render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    #db.session.rollback() TODO: rollback for when db is implemented
    if wants_json_response():
        return api_error_response(500)
    render_template('errors/500.html'), 500