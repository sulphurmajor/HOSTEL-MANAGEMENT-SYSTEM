from student import Student
class Localstudent(Student):
    def __init__(self,first_name,last_name,contact,student_id,birth_year,age,gender,course,room_id,district):
        super().__init__(self,first_name,last_name,contact,student_id,birth_year,age,gender,course,room_id)
        self.district = district
        self.total_tuition = 1000000

        def make_payment(self,payment):
            payment.status = "paid"
            self.payments.append(payment)
            self.paid_amount +=payment.amount

            return f"{self.first_name} {self.last_name} made payment of shs{payment.amount} for {payment.semester} semester.Balance: shs {self.get_balance()}"
