class Room:
    def __init__(self,room_id,room_number,hostel_id,capacity,status):
        self.room_id=room_id
        self.room_number=room_number
        self.hostel_id=hostel_id
        self.capacity=capacity
        self.__status=status
        
        
        
    def set_status(self):
        return self.__status
    
    @property
    def staus(self):
        return self.__status
    

    def is_available(self):
        return self.__status == "available"
        

