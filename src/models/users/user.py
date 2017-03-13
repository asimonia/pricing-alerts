from common.database import Database
import uuid
import models.users.errors as UserErrors
from common.utils import Utils


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

	@staticmethod
	def register_user(email, password):
		"""
		This method registers a user using email and password.
		The password already comes hashed as sha-512.
		"""
		user_data = Database.find_one("users", {"email": email})

		if user_data is not None:
			# Tell user they are already registered
			raise UserErrors.UserAlreadyRegisteredError("The email you used to register already exists.")
		if not Utils.email_is_valid(email):
			# Tell user that their email is not constructed properly
			raise UserErrors.InvalidEmailError("The email does not have the right format.")

		User(email, Utils.hash_password(password)).save_to_db()

		return True

	def save_to_db(self):
		Database.insert("users", self.json())

	def json(self):
		return {
			"_id": self._id,
			"email": self.email,
			"password": self.password
		}

	@classmethod
	def find_by_email(cls, email):
		return cls(**Database.find_one('users', {'email': email}))

	def get_alerts(self):
		return Alert.find_by_user_email(self.email)