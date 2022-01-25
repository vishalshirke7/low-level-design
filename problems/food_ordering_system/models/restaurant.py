class Restaurant(object):

    def __init__(self, name, pincodes, food_name, food_price, quantity):
        self.name = name
        self.pincodes = pincodes
        self.food_name = food_name
        self.food_price = food_price
        self.quantity = quantity
        self.restaurant_id = self._generate_restaurant_id()

    def _generate_restaurant_id(self):
        return "-".join(self.name.lower().split(' '))


    def __str__(self):
        return f'{self.restaurant_id} {self.quantity}'