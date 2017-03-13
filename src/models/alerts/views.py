from flask import blueprints, render_template, request, session
from models.alerts.alert import Alert
from models.items.item import Item
import models.users.decorators as user_decorators

alert_blueprint = blueprints.Blueprint('alerts', __name__)

@alert_blueprint.route('/')
def index():
	return "This is the alerts index"


@alert_blueprint.route('/new', methods=['GET', 'POST'])
@user_decorators.requires_login
def create_alert():
	if request.method == 'POST':
		name = request.form['name']
		url = request.form['url']
		price_limit = request.form['price_limit']

		item = Item(name, url)
		item.save_to_mongo()

		alert = Alert(session['email'], price_limit, item._id)
		alert.load_item_price()

	return render_template('alerts/new_alert.html')


@alert_blueprint.route('/deactivate/<string:alert_id>')
@user_decorators.requires_login
def deactivate_alert(alert_id):
	pass


@alert_blueprint.route('/<string:alert_id>')
@user_decorators.requires_login
def get_alert_page(alert_id):
	alert = Alert.find_by_id(alert_id)
	return render_template('alerts/alert.html')

