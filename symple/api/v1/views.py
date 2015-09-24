__author__ = 'echevemaster'
__version__ = '1.0.0'

import json
import flask
from auth import requires_auth
from exception import CustomException
from validations import is_email_address_valid
from symple.database import db
from symple.modules.users.models import User
from symple.modules.projects.models import Project
from symple.modules.pages.models import Template, Page, TypePage

bp = flask.Blueprint('api', __name__, url_prefix='/api')

@bp.errorhandler(404)
def not_found(error):
    return flask.make_response(flask.jsonify(
        {
            'status' : 404,
            'error': 'Not found'
        } ), 404)

@bp.errorhandler(CustomException)
def handle_custom_exception(error):
    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# API Index

@bp.route('/', methods=['GET'])
@requires_auth
def index():
    if flask.request.method == 'GET':
        json_results = []
        output = {
            'message':'Welcome to Symple Api',
            'version': __version__
        }
        json_results.append(output)
    return flask.jsonify(api=json_results)


@bp.route('/users/add', methods=['POST'])
@requires_auth
def add_user():
    if flask.request.method == 'POST':
        data = flask.request.get_json(force=True)
        username =  data.get('username', None)
        full_name = data.get('full_name', None)
        email = data.get('email', None)
        active = data.get('active', None)
        check_username = User.query.filter(User.username == username).first()
        check_email = User.query.filter(User.email == email).first()
        print check_username
        if check_username is not None:
            raise CustomException('This user exist in our database', 400)
        if check_email is not None:
            raise CustomException('This email exist in our database', 400)
        if username is None:
            raise CustomException('The "name" field can not be blank', 400)
        if full_name is None:
            raise CustomException('The "full_name" field can not be blank', 400)
        if not is_email_address_valid(email):
            raise CustomException('The "email" field is malformed')

        user = User(username=username,
                    full_name=full_name,
                    email=email,
                    active=active)
        db.session.add(user)
        db.session.commit()

        return flask.jsonify(user=data)

@bp.route('/projects/add', methods=['POST'])
@requires_auth
def add_project():
    if flask.request.method == 'POST':
        data = flask.request.get_json(force=True)
        user_id = data.get('user_id', None)
        paid = data.get('paid', None)
        template_id = data.get('template_id', None)
        if user_id is None:
            raise CustomException('user_id is mandatory',  400)
        if template_id is None:
            raise CustomException('template_id is mandatory', 400)

        project = Project(user_id=user_id,
                          paid=paid,
                          template_id=template_id)
        db.session.add(project)
        db.session.commit()

        return flask.jsonify(project=data)

@bp.route('/templates/add', methods=['POST'])
@requires_auth
def add_template():
    if flask.request.method == 'POST':
        data = flask.request.get_json(force=True)
        template_name = data.get('template_name', None)
        if template_name is None:
            raise CustomException('name of template is mandatory', 400)
        template = Template(template_name=template_name)
        db.session.add(template)
        db.session.commit()

        return flask.jsonify(template=data)

@bp.route('/pages/add', methods=['POST'])
@requires_auth
def add_page():
    if flask.request.method == 'POST':
        data = flask.request.get_json(force=True)
        title = data.get('title', None)
        content = data.get('content', None)
        project_id = data.get('project_id', None)
        type_page_id = data.get('type_page_id', None)
        if title is None:
            raise CustomException('Title is mandatory', 400)
        if content is None:
            raise CustomException('content is mandatory', 400)
        if project_id is None:
            raise CustomException('project_id is mandatory', 400)
        if type_page_id is None:
            raise CustomException('type_page_id is mandatory', 400)
        page = Page(title=title,
                    content=content,
                    project_id=project_id,
                    type_page_id=type_page_id)
        db.session.add(page)
        db.session.commit()

        return flask.jsonify(page=data)


@bp.route('/type_page/add', methods=['POST'])
@requires_auth
def add_type():
    if flask.request.method == 'POST':
        data = flask.request.get_json(force=True)
        type_name = data.get('type_name', None)
        if type_name is None:
            raise CustomException('name of the type is mandatory', 400)
        type = TypePage(type_name=type_name)
        db.session.add(type)
        db.session.commit()

        return flask.jsonify(type_page=data)




