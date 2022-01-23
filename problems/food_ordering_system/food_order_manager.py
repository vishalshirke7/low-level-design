from services import user_service, order_service, restaurant_service

SAMPLE_DATA = {
    'new_user': [
        {
            'name': 'vishal',
            'gender': 'M',
            'mobile': '9898989898',
            'pincode':'410122'
        },
        {
            'name': 'Kohli',
            'gender': 'M',
            'mobile': '9898989897',
            'pincode':'410122'
        }        
    ],
    'new_restaurant': [
        {
            'name': 'Kailash H',
            'pincodes': ['124412', '124144'],
            'food_item': 'Pizza',
            'price': 13242, 
            'quantity': 10
        },
        {
            'name': 'Taj H',
            'pincodes': ['4677', '4677'],
            'food_item': 'Idli',
            'price': 1000, 
            'quantity': 4
        }        
    ]
}


class FoodOrderManager(object):

    def __init__(self):
        self.user_manager = user_service.UserManager()
        self.order_manager = order_service.OrderManager()
        self.restaurant_manager = restaurant_service.RestaurantManager()

    def register_user(self, user_details):
        user = self.user_manager.register_user(**user_details)
        return user

    def log_in(self, user):
        self.user_manager.log_in(user)

    def register_restaurant(self, restaurant_details):
        restaurant = self.restaurant_manager.register_restaurant(restaurant_details)
        return restaurant

    def perform_tasks(self):
        user1 = self.register_user(SAMPLE_DATA['new_user'][0])
        self.log_in(user1)
        user2 = self.register_user(SAMPLE_DATA['new_user'][1])
        # restaurant1 = self.register_restaurant()



food_order_manager = FoodOrderManager()
food_order_manager.perform_tasks()