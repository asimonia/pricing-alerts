from flask import blueprints

item_blueprint = blueprints.Blueprint('items', __name__)


@item_blueprint.route('/item/<string:name>')
def item_page(name):
	pass

