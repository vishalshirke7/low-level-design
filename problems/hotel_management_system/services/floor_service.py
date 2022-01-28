from data_store import floor_data_store
from services import (room_service)


class FloorManager(object):
    
    def __init__(self):
        self.floor_dao = floor_data_store.FloorDAO()
        self.room_manager = room_service.RoomManager()
        
    def _create_floor(self, floor_details):
        return self.floor_dao.create_floor(floor_details)                
    
    def _add_room(self, floor):
        for room_number in range(1, floor.total_rooms + 1):
            room_number_details = {
                'room_number': room_number,
                'floor_number': floor.floor_number
            }
            floor.rooms.append(self.room_manager.register_room(room_number_details))
    
    def register_floor(self, floor_details):
        floor = self._create_floor(floor_details)
        self._add_room(floor)
        return floor