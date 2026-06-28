from room import Room
from warden import Warden
class Hostel:
    def __init__(self,hostel_id,name,location,capacity,status):
        self.hostel_id=hostel_id
        self.name=name
        self.location=location
        self.capacity=capacity
        self.__status=status
        self.rooms=[] #composition: hostel has a room
        self.__warden=None #composition: hostel has a warden
        
    def set_status(self):
        return self.__statuts
    
    @property
    def status(self):
        return self.__status
    
        

    def add_room(self,room):
        self.rooms.append(room)
        

    def remove_room(self,room):
        if room in self.rooms:
            self.rooms.remove(room)



    def assign_warden(self,warden):
        self.__warden=warden
        return f"Warden {warden.first_name} {warden.lastname } assigned to hostel {self.name}" #   f string to return warden details here
    
    @property #   gettter to access the warden
    def warden(self):
        return self.__warden

        
    def get_available_room(self):
        available_rooms=[]
        for room in self.rooms:
            if len(room.students)<room.capacity:
                available_rooms.append(room)
        return available_rooms

