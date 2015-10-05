import flask
from symple.modules.users.forms import Adduser
from symple.app import app
from requests.auth import HTTPBasicAuth
import requests
import simplejson
import json
import sys
from symple.modules.projects.models import Project

__author__ = 'echevemaster'

bp = flask.Blueprint('frontend', __name__,
                     template_folder='templates')

url = app.config['API_URL']
api_id = app.config['API_ID']
api_password = app.config['API_PASSWORD']


@bp.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html',
                                 title='Home')

@bp.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = Adduser()
    action = flask.url_for('frontend.create_account')
    print url
    print api_id
    print api_password

    if form.validate_on_submit():
        user = requests.post(url + '/users/add',
                            json={
                                'username' : form.username.data,
                                'full_name' : form.name.data,
                                'email' : form.email.data
                                },
                            auth=(api_id, api_password), verify=False)

        data_user = simplejson.loads(user.text)
        print data_user
        project = requests.post(url + '/projects/add',
                                json={
                                    'user_id' : data_user['user']['id'],
                                    'paid': 0,
                                    'template_id' : 1,
                                    'company_name': form.company_name.data,
                                    'business_about' : form.about.data,
                                    'business_services' : form.services_company.data
                                },
                                auth=(api_id, api_password), verify=False)
        data_project = simplejson.loads(project.text)
        print data_project
        return flask.redirect(flask.url_for('frontend.thank_you', id=data_project['project']['id']))


    return flask.render_template('create_account.html',
                                 title='Crear cuenta',
                                 form=form,
                                 action=action)

@bp.route('/thank_you', methods=['GET', 'POST'])
def thank_you():
    id = flask.request.args.get('id')
    return flask.render_template('thank_you.html',
                                 title='Gracias',
                                 id=id)

@bp.route('/result/<int:id>', methods=['GET', 'POST'])
def result(id):
    queryset = Project.query.filter(Project.id == id).first_or_404()

    return flask.render_template('result.html',
                                 title='Tu pagina',
                                 project=queryset)