from models import restaurant

class RestaurantDAO(object):
	
	all_restaurants = dict()

	def create_restaurant(self, restaurant_details):
		new_restaurant = restaurant.Restaurant(**restaurant_details)
		self.all_restaurants[new_restaurant.restaurant_id] = new_restaurant
		return new_restaurant

	def increase_quantity(self, restaurant, additional_quantity):
		setattr(restaurant, 'quantity', restaurant.quantity + additional_quantity)
