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
            'food_name': 'Pizza',
            'food_price': 13242, 
            'quantity': 10
        },
        {
            'name': 'Taj H',
            'pincodes': ['4677', '4677'],
            'food_name': 'Idli',
            'food_price': 1000, 
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

    def rate_restaurant(self, user, restaurant, rating):
        pass

    def get_all_restaurants(self):
        pass

    def palce_order(self):
        pass

    def register_restaurant(self, restaurant_details):
        restaurant = self.restaurant_manager.register_restaurant(restaurant_details)
        return restaurant

    def increase_quantity(self, restaurant, quantity):
        self.restaurant_manager.increase_quantity(restaurant, quantity)

    def perform_tasks(self):
        user1 = self.register_user(SAMPLE_DATA['new_user'][0])
        self.log_in(user1)
        user2 = self.register_user(SAMPLE_DATA['new_user'][1])
        self.log_in(user2)
        restaurant1 = self.register_restaurant(SAMPLE_DATA['new_restaurant'][0])
        self.increase_quantity(restaurant1, 9)
        restaurant2 = self.register_restaurant(SAMPLE_DATA['new_restaurant'][1])            
        self.increase_quantity(restaurant2, 100)
        print(restaurant1, restaurant2)


food_order_manager = FoodOrderManager()
food_order_manager.perform_tasks()