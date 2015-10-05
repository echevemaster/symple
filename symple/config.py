__author__ = 'echevemaster'
# -*- coding: utf-8 -*-
__author__ = 'echevemaster'

import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
engine = 'sqlite'
db_name = 'symple_db'
db_user = ''
db_password = ''
db_server = 'localhost'

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}/{4}'.format(engine,
                                                             db_user,
                                                             db_password,
                                                             db_server,
                                                             db_name)

    DATABASE_CONNECT_OPTIONS = {}
    SECRET_KEY = ''
    CSRF_SESSION_KEY = ''
    API_URL = ''

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = engine + ':///' + os.path.join(basedir,
                                                             db_name)
    DATABASE_CONNECT_OPTIONS = {}
    SECRET_KEY = 'somethingimpossible'
    CSRF_SESSION_KEY = 'somethingimpossible'
    API_URL = 'http://localhost:5000/api'
    API_ID = 'api'
    API_PASSWORD = 'secret'

class TestingConfig(Config):
    TESTING = True