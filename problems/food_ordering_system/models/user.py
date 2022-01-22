class User(object):	

	def __init__(self, name, gender, mobile, pincode):
		self.name = name
		self.gender = gender
		self.mobile = mobile
		self.pincode = pincode
		self.orders = list()


	def rate(self):
		pass

	def place_order(self):
		pass						