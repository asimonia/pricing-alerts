class Item:

	def __init__(self, name, price, url):
		self.name = name
		self.price = price
		self.url = url

	def __repr__(self):
		return "<Item {} with URL {}>".format(self.name, self.url)

	def load_item(self):
		# Amazon HTML
		# <span id="priceblock_ourprice" class="a-size-medium a-color-price">$24.42</span>