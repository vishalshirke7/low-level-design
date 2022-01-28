from models import room_model


class RoomDAO(object):
    
    all_rooms = dict()
    
    def create_room(self, registration_data):
        new_room = room_model.Room(**registration_data)
        self.all_rooms[new_room.room_id] = new_room
        return new_room