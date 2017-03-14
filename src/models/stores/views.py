from flask import blueprints, render_template

from models.stores.store import Store

store_blueprint = blueprints.Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
	stores = Store.all()
	return render_template('stores/store_index.html', stores=stores)


@store_blueprint.route('/store/<string:store_id>')
def store_page(store_id):
	return render_template('stores/store.html', store=Store.get_by_id(store_id))


@store_blueprint.route('/edit/<string:store_id>', methods=['GET', 'POST'])
def edit_store(store_id):
	if request.method == 'POST':
		pass
	return "Edit store page"


@store_blueprint.route('/delete/<string:store_id>')
def delete_store(store_id):
	return "Delete store"


@store_blueprint.route('/new', methods=['GET', 'POST'])
def create_store():
	return "This is the store creation page"