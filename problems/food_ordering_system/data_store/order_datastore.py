from models import *

class OrderDAO(object):

    orders = []
    
    def create_order(order_details):
        order = Order(**order_details)
        self.orders.append(order)
        return order

