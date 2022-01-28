from services import (hotel_service)


SAMPLE_DATA = [
    {
        'name': 'Taj Hotel',
        'address': 'ABCD HHHH',
        'total_floors': 10,
        'total_rooms': 10
    },
    {
        'name': 'Grand Hotel',
        'address': 'RHG KJLK',
        'total_floors': 20,
        'total_rooms': 20
    }    
]
    
class BookingOrchestrator(object):

    def perform_tasks(self):
        hotel_manager = hotel_service.HotelManager()
        hotel_1 = hotel_manager.register_hotel(SAMPLE_DATA[0])
        print(hotel_1.floors)
        for floor in hotel_1.floors:
            for room in floor.rooms:
                print(room)
            
        # hotel_1.check_in(5)
        # hotel_1.check_out()
        # hotel_2 = hotel_manager.register_hotel(SAMPLE_DATA[1])
        # hotel_2.check_in(5)
        # hotel_2.check_out()        
    
    
booking_orchestrator = BookingOrchestrator()
booking_orchestrator.perform_tasks()