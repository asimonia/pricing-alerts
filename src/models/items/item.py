from bs4 import BeautifulSoup
import requests
import re
import items.constants as ItemConstants
import uuid

class Item:

	def __init__(self, name, url, _id=None):
		self.name = name
		self.url = url
		store = Store.find_by_url(url)
		tag_name = store.tag_name
		query = store.query
		self.price = self.load_price(tag_name, query)
		self._id = uuid.uuid4().hex if _id is None else _id

	def __repr__(self):
		return "<Item {} with URL {}>".format(self.name, self.url)

	def load_price(self, tag_name, query):
		"""
		Load the price of any item and also as the tag name and query make sense
		for the URL.
		"""
		request = requests.get(self.url)
		content = request.content
		soup = BeautifulSoup(content, "html.parser")
		element = soup.find(tag_name, query)
		string_price = element.text.strip()		# remove whitespace
		
		pattern = re.compile("(\d+.\d+)")		# extract the price
		match = pattern.search(string_price)

		return match.group()

	def save_to_mongo(self):
		# Insert JSON representation
		Database.insert(ItemConstants.COLLECTION, self.json())

	def json(self):
		"""Return the name and URL of the item"""
		return {
			"_id": self._id,
			"name": self.name,
			"url": self.url,
		}

