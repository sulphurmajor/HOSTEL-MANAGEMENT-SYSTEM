from room import Room
from hostel import Hostel
from warden import Warden
from visitor import Visitor
from payment import Payment
from student import Student


# Create warden, student, and room objects
#warden = Warden("W001", "John", "Smith", "1234567890", "H001")
#student = Student("S001", "Alice", "Johnson", "2000", 0, "Female", "CS", None, "9876543210")
#room = Room("R001", "101", "H001", 2, "available")

# Assign room
#result = warden.assign_room(student, room)
#print(result)  # Output: "Room 101 assigned to Alice Johnson"


from datetime import datetime, timedelta
from student import Student
from room import Room
from hostel import Hostel
from warden import Warden
from payment import Payment
from visitor import Visitor

print("=== HOSTEL MANAGEMENT SYSTEM ===\n")

# 1. Create Hostel
print("1. CREATING HOSTEL")
hostel = Hostel("H001", "Boys Hostel", "Campus A", 100, "Active")
print(f"Hostel Created: {hostel.name} at {hostel.location}")
print(f"Capacity: {hostel.capacity}\n")

# 2. Create Rooms and add to Hostel
print("2. ADDING ROOMS TO HOSTEL")
room1 = Room("R001", "101", "H001", 2, "Available")
room2 = Room("R002", "102", "H001", 3, "Available")
room3 = Room("R003", "103", "H001", 2, "Available")

hostel.add_room(room1)
hostel.add_room(room2)
hostel.add_room(room3)

print(f"Added 3 rooms to hostel")
print(f"  - Room 101 (Capacity: 2)")
print(f"  - Room 102 (Capacity: 3)")
print(f"  - Room 103 (Capacity: 2)\n")

# 3. Create Warden and assign to Hostel
print("3. ASSIGNING WARDEN")
warden = Warden("W001", "Robert", "Brown", "9876543210", "H001")
hostel.warden = warden
print(f"Warden Assigned: {warden.first_name} {warden.last_name}")
print(f"Contact: {warden.contact}\n")

# 4. Create Students
print("4. CREATING STUDENTS")
student1 = Student("S001", "John", "Doe", "2000", 0, "Male", "Computer Science", None, "1234567890")
student2 = Student("S002", "Jane", "Smith", "2001", 0, "Female", "Electrical Engineering", None, "2345678901")
student3 = Student("S003", "Mike", "Johnson", "1999", 0, "Male", "Mechanical Engineering", None, "3456789012")

age1 = student1.compute_age()
age2 = student2.compute_age()
age3 = student3.compute_age()

print(f"  - {student1.first_name} {student1.last_name} (Age: {age1}, Course: {student1.course})")
print(f"  - {student2.first_name} {student2.last_name} (Age: {age2}, Course: {student2.course})")
print(f"  - {student3.first_name} {student3.last_name} (Age: {age3}, Course: {student3.course})\n")

# 5. Warden assigns rooms to students
print("5. ROOM ASSIGNMENT BY WARDEN")
result1 = warden.assign_room(student1, room1)
result2 = warden.assign_room(student2, room1)
result3 = warden.assign_room(student3, room2)

print(f"  - {result1}")
print(f"  - {result2}")
print(f"  - {result3}\n")

# 6. Display room occupancy
print("6. ROOM OCCUPANCY STATUS")
vacancy1 = "Available" if room1.vacant_room() else "Full"
vacancy2 = "Available" if room2.vacant_room() else "Full"
vacancy3 = "Available" if room3.vacant_room() else "Full"

print(f"  - Room 101: {len(room1.students)}/2 students ({vacancy1})")
print(f"  - Room 102: {len(room2.students)}/3 students ({vacancy2})")
print(f"  - Room 103: {len(room3.students)}/2 students ({vacancy3})\n")

# 7. Check available rooms
print("7. AVAILABLE ROOMS IN HOSTEL")
available_rooms = hostel.get_available_room()
print(f"  - {len(available_rooms)} rooms available:")
print(f"      Room 102 ({room2.capacity - len(room2.students)} spots left)")
print(f"      Room 103 ({room3.capacity - len(room3.students)} spots left)\n")

# 8. Student making payments (Polymorphism demonstration)
print("8. STUDENT PAYMENTS")
payment1 = Payment(
    "P001", "S001", 5000, 
    datetime.now(), "Credit Card", "pending",
    datetime.now() + timedelta(days=30), "2024-2025", "Spring"
)
payment2 = Payment(
    "P002", "S002", 5000,
    datetime.now(), "Debit Card", "pending", 
    datetime.now() + timedelta(days=30), "2024-2025", "Spring"
)

result1 = student1.make_payment(payment1)
result2 = student2.make_payment(payment2)

print(f"  - {result1}")
print(f"  - {result2}\n")

# 9. Payment class make_payment method
print("9. PAYMENT CLASS MAKE_PAYMENT METHOD")
payment3 = Payment(
    "P003", "S003", 4500,
    datetime.now(), "Cash", "pending",
    datetime.now() + timedelta(days=30), "2024-2025", "Spring"
)
result3 = payment3.make_payment()
print(f"  - {result3}\n")

# 10. Visitor management
print("10. VISITOR MANAGEMENT")
visitor = Visitor("V001", "Mary", "Doe", "John Doe", "Parent", None, None, "6789012345", "123 Main Street")

check_in_result = visitor.check_in()
check_out_result = visitor.check_out()

print(f"  - {check_in_result}")
print(f"  - {check_out_result}\n")

# 11. Final summary
print("11. FINAL SUMMARY")
total_students = len(room1.students) + len(room2.students) + len(room3.students)
print(f"Total Students in Hostel: {total_students}")
print(f"Total Rooms: 3")
print(f"Hostel Capacity Utilization: {total_students}/{hostel.capacity}")
print(f"Warden: {hostel.warden.first_name} {hostel.warden.last_name}")