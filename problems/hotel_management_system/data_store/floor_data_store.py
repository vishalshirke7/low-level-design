from models import floor_model


class FloorDAO(object):
    
    all_floors = dict()
    
    def create_floor(self, registration_data):
        new_floor = floor_model.Floor(**registration_data)
        self.all_floors[new_floor.floor_id] = new_floor
        return new_floor