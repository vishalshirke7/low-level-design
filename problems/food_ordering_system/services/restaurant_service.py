from exceptions.exceptions import *
from data_store.restaurant_datastore import RestaurantDAO

class RestaurantManager(object):

    def __init__(self):
        self.restaurant_dao = RestaurantDAO()

    def check_user_exists(self, mobile):
        all_users = UserDAO.get_all_users()
        try:
            if mobile in all_users:
                raise InvalidInputError('User Already Exists', mobile)
        except InvalidInputError as e:
            print(str(e))
            return True
        return False

    def register_user(self, name, gender, mobile, pincode):
        user = None
        if not self.check_user_exists(mobile):
            user_details = {
                'name': name,
                'gender': gender,
                'mobile': mobile,
                'pincode': pincode
            }
            user = self.user_dao.register_user(user_details)
        return user

    def increase_quantiry(self):
    	pass