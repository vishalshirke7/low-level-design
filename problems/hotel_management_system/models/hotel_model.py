from abc import  ABC, abstractmethod
import datetime
from enum import  Enum


class Hotel(object):
    def __init__(self, name, address, total_floors, total_rooms):
        self.name = name
        self.address = address
        self.total_floors = total_floors
        self.total_rooms = total_rooms
        self.floors = list()
        self.hotel_id = self._generate_id()
            
    def _generate_id(self):
        current_date = str(datetime.datetime.today().date())
        hotel_name = "-".join(self.name.lower().split(' '))
        return f'H-{hotel_name}-{current_date}'
        
    def __str__(self):
        return f'{self.hotel_id}'
    
    
class Booking():
    
    bboking_id    