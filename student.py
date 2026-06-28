
from payment import Payment
from datetime import datetime
class Student:
    def __init__(self,first_name,last_name,contact,student_id,birth_year,age,gender,course,room_id):
        self.first_name=first_name
        self.last_name=last_name
        self.contact=contact
        self.student_id =student_id    
        self.birth_year=birth_year
        self.age=0
        self.gender=gender
        self.course=course
        self.room_id=room_id
        self.room=None #composition student HAS A Room
        self.payments=[]
        self.total_tuition = 5000  # base tuition for local students
        self.paid_amount = 0


    
    def compute_age(self):
        current_year=datetime.today()
        return self.age
    
    #polymorphism
    def make_payment(self,payment):
        payment.status = "paid"
        self.payments.append(payment)
        self.paid_amount+=payment.amount
        return f"payment:{payment.amount}"
    
    def get_balance(self):
        return self.total_tuition - self.paid_amount

    def request_room(self, room):
    
        if room and room.is_available():
            self.room = room
            return f"Room {room.room_number} assigned to {self.first_name} {self.last_name} "
        return "Room not available"