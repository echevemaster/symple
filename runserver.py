#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from symple.app import app
from symple.database import db
from symple.modules.users.models import User #noqa
from symple.modules.pages.models import  Page, TypePage, Template
from symple.modules.projects.models import Project

manager = Manager(app)

@manager.command
def create_database():
    db.drop_all()
    db.create_all()

def destroy_database():
    db.drop_all()

@manager.command
def run():
    app.run(debug=True, host='0.0.0.0',threaded=True)

if __name__ == '__main__':
    manager.run()