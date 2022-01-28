from abc import  ABC, abstractmethod
from enum import  Enum


class Floor():
    def __init__(self, floor_number, total_rooms):
        self.floor_number = floor_number
        self.total_rooms = total_rooms
        self.floor_id = self._generate_id()        
        self.rooms = list()

    def _generate_id(self):
        return 'F-{self.floor_number}-{self.total_rooms}'
            
    def __str__(self):
        return f'{self.floor_id}'
        