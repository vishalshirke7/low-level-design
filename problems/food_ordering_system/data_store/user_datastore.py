from models import user

class UserDAO(object):

	registered_users = dict()
	logged_in_user = None

	def register_user(self, user_details):
		user_object = user.User(**user_details)
		UserDAO.registered_users[user_details['mobile']] = user_object
		return user_object

	def log_in(self):
		pass

	@classmethod
	def get_all_users(cls):
		return cls.registered_users

	# def place_order(self):
	# 	pass		