from models import *

class RestaurantDAO(object):
	
	def register_restaurant(restaurant_details):
		restaurant = Restaurant(**restaurant_details)
		return restaurant

		