from data_store import hotel_data_store
from strategies import (bottom_up_allocation_strategy,
                      top_down_allocation_strategy)


class RoomAllocationManager(object):
    
    def __init__(self, hotel, req_rooms, strategy):
        self.hotel = hotel
        self.req_rooms = req_rooms
    
    def allocate_rooms(self):
        pass
