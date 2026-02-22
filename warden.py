
from room import Room
class Warden:
    def __init__(self,first_name,last_name,contact,warden_id,hostel_id):
        self.first_name= first_name
        self.last_name= last_name
        self.contact= contact
        self.warden_id=warden_id
        self.hostel_id=hostel_id

    def assign_room(self,student,room):
        if len(room.students)<room.capacity:
            room.students.append(student)
            student.room=room
            student.room_id=room.room_id
            return f"Room {room.room_number} assigned to {self.first_name} {self.last_name}"
        else:
            return f" Cannot assign - Room {room.room_number} is full"
        


