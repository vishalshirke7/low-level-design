from models import hotel_model


class HotelDAO(object):
    
    all_hotels = dict()
    
    def create_hotel(self, registration_data):
        new_hotel = hotel_model.Hotel(**registration_data)
        self.all_hotels[new_hotel.hotel_id] = new_hotel
        return new_hotel