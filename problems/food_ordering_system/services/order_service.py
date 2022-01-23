import datetime

from data_store import *


class OrderManager(object):

    def _generate_order_id(self, order_details):
        unique_order_id_params = [datetime.datetime.now(), order_details['restaurant_id'], order_details['quantity']]
        return "-".join(map(lambda val: str(val), unique_order_id_params))  
    
    def create_order(self, order_details):
        order_details['order_id'] = self._generate_order_id(order_details)
        OrderDAO.create_order(**order_details)



