from data_store import room_data_store


class RoomManager(object):
    
    def __init__(self):
        self.room_dao = room_data_store.RoomDAO()
        
    def _create_room(self, room_details):
        return self.room_dao.create_room(room_details)                
    
    def register_room(self, room_details):
        room = self._create_room(room_details)
        return room