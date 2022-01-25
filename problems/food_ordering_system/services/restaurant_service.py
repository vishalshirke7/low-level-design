from exceptions.exceptions import *
from data_store.restaurant_datastore import RestaurantDAO

class RestaurantManager(object):

    def __init__(self):
        self.restaurant_dao = RestaurantDAO()

    def register_restaurant(self, restaurant_details):
        restaurant = self.restaurant_dao.create_restaurant(restaurant_details)
        return restaurant

    def increase_quantity(self, restaurant, quantity):
        if restaurant.restaurant_id in self.restaurant_dao.all_restaurants:
            self.restaurant_dao.increase_quantity(restaurant, quantity)