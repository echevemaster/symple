# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
import wtforms

__author__ = 'echevemaster'


class Adduser(Form):
    company_name = wtforms.StringField('&iquest; C&oacute;mo se llama tu empresa?:',
                                       [wtforms.validators.DataRequired(u'Ingrese el nombre de su empresa')])
    about = wtforms.TextAreaField('&iquest; Que hace tu empresa o negocio?',
                                  [wtforms.validators.DataRequired(u'Ingrese la descripción de su negocio')])
    services_company = wtforms.TextAreaField('&iquest; Cuales servicios ofrece tu empresa o negocio?',
                                     [wtforms.validators.DataRequired(u'Ingrese los servicios que ofrece su empresa')])

    name = wtforms.StringField(u'Nombres:',
                               [wtforms.validators.DataRequired(u'Ingrese su nombre')])
    username = wtforms.StringField(u'Nombre de usuario:',
                                   [wtforms.validators.DataRequired(u'Ingrese su nombre de usuario')])
    password = wtforms.PasswordField(u'Contraseña:',
                                   [wtforms.validators.DataRequired(u'Ingrese su contraseña')])
    email = wtforms.StringField(u'Email:',
                                [wtforms.validators.DataRequired(u'Ingrese su email')])
