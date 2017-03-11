from common.database import Database
import uuid
import models.users.errors as UserErrors

class User:

	def __init__(self, email, password, _id=None):
		"""Create a user with an email, password, unique id"""
		self.email = email
		self.password = password
		self._id = uuid.uuid4().hex if _id is None else _id

	def __repr__(self):
		return "<User {}>".format(self.email)

	@staticmethod
	def is_login_valid(email, password):
		"""
		Verifies that an email/password combo is valid
		Checks that the email exists, and the password
		associated to that email is correct.
		Uses sha512 hashed password.
		"""
		user_data = Database.find_one("users", {'email': email}) 	# Password in sha512
		if user_data is None:
			# Tell user the email doesn't exist
			raise UserErrors.UserNotExistsErorr("Your user does not exist.")
		if not Utils.check_hashed_password(password, user_data['password']):
			# Tell user that their password is wrong
			raise UserErrors.IncorrectPasswordError("Your password was wrong.")

		return True
