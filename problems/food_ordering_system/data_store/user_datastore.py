from models import user

class UserDAO(object):

	registered_users = dict()
	logged_in_user = None

	def create_user(self, user_details):
		new_user = user.User(**user_details)
		self.registered_users[user_details['mobile']] = new_user
		return new_user

	def log_in(self):
		pass

	@classmethod
	def get_all_users(cls):
		return cls.registered_users

	# def place_order(self):
	# 	pass		