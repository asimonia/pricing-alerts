from flask import blueprints, render_template

alert_blueprint = blueprints.Blueprint('alerts', __name__)

@alert_blueprint.route('/')
def index():
	return "This is the alerts index"


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def create_alert():
	if request.method == 'POST':
		pass

	return render_template('alerts/new_alert.html')


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
	pass


@alert_blueprint.route('/<string:alert_id>')
def get_alert_page(alert_id):
	alert = Alert.find_by_id(alert_id)
	return render_template('alerts/alert.html')


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
	pass
