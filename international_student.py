from student import Student
class Internationalstudent(Student):
        def __init__(self,first_name,last_name,contact,student_id,birth_year,age,gender,course,room_id,country_of_origin):
            super().__init__(self,first_name,last_name,contact,student_id,birth_year,age,gender,course,room_id)

            self.country_of_origin = country_of_origin
            self.total_tuition = 3000000
            self.international_fee = 100000

        def make_payment(self,payment):
            net_payment =payment.amount - self.international_fee

            payment.status = "paid"
            self.payments.append(payment)

            return f"{self.first_name} {self.last_name} made payment of ${payment.amount} for {payment.semester} semester.. international fee: shs{self.international_fee}. Net payment:{net_payment}. Balance: {self.get_balance()}"


        