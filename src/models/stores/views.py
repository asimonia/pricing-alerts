from flask import blueprints

store_blueprint = blueprints.Blueprint('stores', __name__)


@store_blueprint.route('/store/<string:name>')
def store_page():
	pass
	