__author__ = 'echevemaster'

import flask
from functools import wraps

def check_auth(username, password):
    return username == 'api' and password == 'secret'

def authenticate():
    message = {'message': 'Authenticate'}
    resp = flask.jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Symple"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = flask.request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated