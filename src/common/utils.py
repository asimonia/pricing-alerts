import re
from passlib.hash import pbkdf2_sha512

class Utils:

	@staticmethod
	def email_is_valid(email):
		email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
		return True if email_address_matcher.match(email) else False

	@staticmethod
	def hash_password(password):
		"""
		Hashes a password using sha512 -> pbkdf2_sha512 encrypted password
		"""
		return pbkdf2_sha512.encrypt(password)

	@staticmethod
	def check_hashed_password(password, hashed_password):
		"""
		Checks the password the user sent matches that of the database.
		Uses https://en.wikipedia.org/wiki/PBKDF2
		"""
		return pbkdf2_sha512.verify(password, hashed_password)
