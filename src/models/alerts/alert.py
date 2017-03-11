import uuid
import requests
import datetime
import models.alerts.constants as AlertConstants
from models.items.item import Item
from common.database import Database

class Alert:
	
	def __init__(self, user_email, price_limit, item_id, last_checked=None, _id=None):
		self.user_email = user_email
		self.price_limit = price_limit
		self.item = Item.get_by_id(item_id)
		self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked
		self._id = uuid.uuid4().hex if _id is None else _id

	def __repr__(self):
		return "<Alert for {} on item {} with price {}>".format(self.user_email, 
			self.item.name, self.price_limit)

	def send(self):
		return requests.post(
			AlertConstants.URL,
			auth=("api", AlertConstants.API_KEY),
			data={
				"from": AlertConstants.FROM,
				"to": self.user_email,
				"subject": "Price limit reached for {}."format(self.item.name),
				"text": "We've found a deal!"
			}
		)

	@classmethod
	def find_needing_update(cls, minutes_since_update=AlertConstants.ALERT_TIMEOUT):
		last_updated_limit = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes_since_update)
		return [cls(**elem) for elem in Database.find(AlertConstants.COLLECTION, {"last_checked": 
																					{"$gte": last_updated_limit}
																				  })]

	def save_to_mongo(self):
		Database.insert(AlertConstants.COLLECTION, self.json())

	def json(self):
		return {
			"_id": self._id,
			"price_limit": self.price_limit,
			"last_checked": self.last_checked,
			"user_email": self.user_email,
			"item": self.itme.json()
		}
