from data_store import hotel_data_store
from services import (floor_service,
                      room_service)

# class HotelFactory(object):
        # 
        
class HotelManager(object):
    
    def __init__(self):
        self.hotel_dao = hotel_data_store.HotelDAO()
        self.floor_manager = floor_service.FloorManager()
        
    def _create_hotel(self, registration_data):
        return self.hotel_dao.create_hotel(registration_data)
    
    def add_floor(self, hotel):
        for floor_number in range(1, hotel.total_floors + 1):
            floor_details = {
                'floor_number': floor_number, 
                'total_rooms': hotel.total_rooms
            }
            hotel.floors.append(self.floor_manager.register_floor(floor_details))
    
    def register_hotel(self, registration_data):
        hotel = self._create_hotel(registration_data)
        self.add_floor(hotel)
        return hotel
    
    def check_in(self, number_of_rooms):
        pass
    
    def check_out(self, room_number):
        pass    