from exceptions.exceptions import *
from data_store.user_datastore import UserDAO

class UserManager(object):

    def __init__(self):
        self.user_dao = UserDAO()

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
            user = self.user_dao.create_user(user_details)
        return user

    def log_in(self, user):
        try:
            if self.user_dao.logged_in_user == user:
                raise AlreadyLoggedInError('User Already Logged In', user)
        except AlreadyLoggedInError as e:
            print(str(e))
        else:
            self.user_dao.logged_in_user = user
            

    # def place_order(self):
    #     pass

    # def rate_restaurant(self):
    #     pass

    # def serviceable_restaurants(self):
    #     pass

    # def order_history(self):
    #     pass