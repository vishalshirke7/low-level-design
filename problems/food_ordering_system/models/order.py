import datetime

class Order(object):
    
    def __init__(self, order_id, user_id, restaurant_id, food_item, quantity, price):
        self.order_id = order_id
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        # self.order_id = self._generate_order_id()



