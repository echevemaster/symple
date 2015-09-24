__author__ = 'echevemaster'

from symple.database import db

class Page(db.Model):

    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    project_id = db.Column(db.Integer())
    type_page_id = db.Column(db.Integer())

class TypePage(db.Model):

    __tablename__ = 'type_pages'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255))


class Template(db.Model):

    __tablename__ = 'templates'
    id = db.Column(db.Integer, primary_key=True)
    template_name = db.Column(db.String(255))
