# -*- coding: utf-8 -*-
import os
import sys
import flask
from symple.database import db
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)

app.config.from_object('symple.config.DevelopmentConfig')

db.init_app(app)
Bootstrap(app)

from symple.api.v1.views import bp as api_bp
from ui.views import bp as ui_bp

app.register_blueprint(api_bp)
app.register_blueprint(ui_bp)


