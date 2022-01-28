from abc import ABC, abstractmethod

class Strategy(ABC):
    
    def get_available_floors(self):
        pass
    
    def get_available_rooms(self):
        pass    

    def allocate(self):
        pass