# -*- coding: utf-8 -*-
import os
import sys
import flask
from symple.database import db

app = flask.Flask(__name__)

app.config.from_object('symple.config.DevelopmentConfig')

db.init_app(app)

from symple.api.v1.views import bp as api_bp

app.register_blueprint(api_bp)


