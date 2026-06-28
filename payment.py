from datetime import datetime
class Payment:
    def __init__(self,payment_id,student_id,amount,payment_date,mode_of_payment,status,due_date,academic_year,semester):
        self.__payment_id=payment_id
        self.student_id=student_id
        self.amount=amount
        self.payment_date=payment_date
        self.mode_of_payment=mode_of_payment
        self.status=status
        self.due_date=due_date
        self.academic_year=academic_year
        self.semester=semester
    
    def set_payment(self):
        return self.__payment_id

    @property
    def payment(self):
        return self.__payment_id

    def make_payment(self):
        self.status = "paid"
        return f"Payment ID: {self.__payment_id} | Amount: {self.amount} | Status: {self.status}"


    def check_due(self):
        today=datetime.now().date()
        if self.status != "paid" and today>self.due_date:
            print(f"payment {self.__payment_id} is overdue!")
        else:
            print(f"payment {self.__payment_id} is up to date")
