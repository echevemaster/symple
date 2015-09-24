__author__ = 'echevemaster'

from symple.database import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    paid = db.Column(db.Boolean(), default=False)
    template_id = db.Column(db.Integer())