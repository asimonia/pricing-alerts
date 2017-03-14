from flask import blueprints, render_template

from models.stores.store import Store

store_blueprint = blueprints.Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
	stores = Store.all()
	return render_template('stores/store_index.html', stores=stores)


@store_blueprint.route('/store/<string:store_id>')
def store_page(store_id):
	return "This is the store page"


@store_blueprint.route('/new', methods=['GET', 'POST'])
def create_store():
	return "This is the store creation page"