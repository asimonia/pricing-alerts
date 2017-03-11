from bs4 import BeautifulSoup
import requests
import re

class Item:

	def __init__(self, name, url, store):
		self.name = name
		self.url = url
		self.store = store
		tag_name = store.tag_name
		query = store.query
		self.price = self.load_price(tag_name, query)

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

