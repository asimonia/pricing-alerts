import pymongo

class Database:
	URI = 'mongodb://127.0.0.1:27017'
	DATABASE = None

	@staticmethod
	def initialize():
		client = pymongo.MongoClient(Database.URI)
		Database.DATABASE = client['fullstack']

	@staticmethod
	def insert(collection, data):
		"""Insert data into a collection"""
		Database.DATABASE[collection].insert(data)

	@staticmethod
	def find(collection, query):
		"""Find multiple document(s) within a collection"""
		return Database.DATABASE[collection].find(query)

	@staticmethod
	def find_one(collection, query):
		"""Find one document withint a collection"""
		return Database.DATABASE[collection].find_one(query)