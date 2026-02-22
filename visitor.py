from datetime import datetime
class Visitor:   
    def __init__(self,first_name,last_name,contact,visitor_id,student_name,relation_to_student,intime,outtime,address):
        self.first_name=first_name
        self.last_name=last_name
        self.contact=contact
        self.visitor_id=visitor_id
        self.student_name=student_name
        self.relation_to_student=relation_to_student
        self.__intime=intime
        self.__outtime=outtime
        self.address=address
        
    def set_intime(self):
        return self.__intime
    @property
    def intime(self):
        return self.__intime
    
    def set_outtime(self):
        return self.__outtime
    @property
    def outtime(self):
        return self.__outtime

    def check_in(self):
        self.__intime=datetime.now()
        return(f"visitor {self.first_name} {self.last_name} checked in at {self.__outtime}")

    def check_out(self):
        self.__outtime=datetime.now()
        return(f"visitor {self.first_name} {self.last_name} checked out at {self.__outtime}")