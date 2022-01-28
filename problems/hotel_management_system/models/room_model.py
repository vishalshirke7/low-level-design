from abc import  ABC, abstractmethod
from enum import  Enum


class RoomStatus(Enum):
    FREE = 1
    ALLOCATED = 2
    

class Room():
    def __init__(self, room_number, floor_number):
        self.room_number = room_number
        self.floor_number = floor_number
        self.room_id = self._generate_room_id()
        self.status = RoomStatus.FREE
        
    def _generate_room_id(self):
        return f'RN-{self.room_number}-{self.floor_number}'

    def __str__(self):
        return f'{self.room_id}'