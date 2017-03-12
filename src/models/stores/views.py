from flask import blueprints

store_blueprint = blueprints.Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
	return "This is the stores index"


@store_blueprint.route('/store/<string:name>')
def store_page():
	pass
	