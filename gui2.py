import tkinter as tk
from tkinter import *
from hostel import Hostel
from warden import Warden
from room import Room
from student import Student

class HostelSystem:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Hostel Management")
        self.main_window.geometry("500x400")
        self.main_window.configure(bg='#008080')
        
        # Initialize instances
        self.hostel = None
        self.warden = None
        self.rooms = []
        self.students = []
        
        self.create_login()

    def create_login(self):
        login_frame = tk.Frame(self.main_window, bg='#20B2AA', padx=20, pady=20)
        login_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(login_frame, text="Hostel Login", font=('Arial', 14), 
                bg='#20B2AA', fg='white').pack(pady=10)
        
        tk.Label(login_frame, text="Username:", bg='#20B2AA', fg='white').pack()
        self.user_entry = tk.Entry(login_frame, width=20)
        self.user_entry.pack(pady=5)
        
        tk.Label(login_frame, text="Password:", bg='#20B2AA', fg='white').pack()
        self.pass_entry = tk.Entry(login_frame, width=20, show='*')
        self.pass_entry.pack(pady=5)
        
        tk.Button(login_frame, text="Login", command=self.check_access,
                 bg='#008B8B', fg='white', width=12).pack(pady=10)
        
        self.user_entry.focus()

    def check_access(self):
        if self.user_entry.get() == "admin" and self.pass_entry.get() == "user123":
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Wrong username or password")

    def show_main_menu(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()
        
        tk.Label(self.main_window, text="Hostel Management System", 
                font=('Arial', 16, 'bold'), bg='#008080', fg='white').pack(pady=20)
        
        button_frame = tk.Frame(self.main_window, bg='#008080')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Setup Hostel", command=self.setup_hostel,
                 bg='#20B2AA', fg='white', width=15, height=2).grid(row=0, column=0, padx=5, pady=5)
        
        tk.Button(button_frame, text="Add Warden", command=self.add_warden,
                 bg='#20B2AA', fg='white', width=15, height=2).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(button_frame, text="Create Room", command=self.create_room,
                 bg='#20B2AA', fg='white', width=15, height=2).grid(row=1, column=0, padx=5, pady=5)
        
        tk.Button(button_frame, text="Add Student", command=self.add_student,
                 bg='#20B2AA', fg='white', width=15, height=2).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(button_frame, text="Assign Room", command=self.assign_room,
                 bg='#20B2AA', fg='white', width=15, height=2).grid(row=2, column=0, padx=5, pady=5)
        
        tk.Button(button_frame, text="Make Payment", command=self.make_payment,
                 bg='#20B2AA', fg='white', width=15, height=2).grid(row=2, column=1, padx=5, pady=5)
        
        tk.Button(button_frame, text="Check Status", command=self.check_status,
                 bg='#20B2AA', fg='white', width=15, height=2).grid(row=3, column=0, padx=5, pady=5)
        
        tk.Button(button_frame, text="Exit System", command=self.main_window.quit,
                 bg='#DC143C', fg='white', width=15, height=2).grid(row=3, column=1, padx=5, pady=5)

    def setup_hostel(self):
        setup_window = tk.Toplevel(self.main_window)
        setup_window.title("Setup Hostel")
        setup_window.geometry("400x400")
        setup_window.configure(bg='#008080')
        
        tk.Label(setup_window, text="Hostel Setup", font=('Arial', 14), 
                bg='#008080', fg='white').pack(pady=10)
        
        # Hostel details form
        fields = [
            ("Hostel ID:", "entry"),
            ("Hostel Name:", "entry"),
            ("Location:", "entry"),
            ("Capacity:", "entry"),
            ("Status:", "combobox")
        ]
        
        entries = {}
        
        for i, (label, field_type) in enumerate(fields):
            tk.Label(setup_window, text=label, bg='#008080', fg='white').pack(pady=5)
            if field_type == "entry":
                entry = tk.Entry(setup_window, width=25)
                entry.pack(pady=5)
                entries[label] = entry
            elif field_type == "combobox":
                combo = ttk.Combobox(setup_window, width=22, values=["Active", "Inactive", "Maintenance"])
                combo.set("Active")
                combo.pack(pady=5)
                entries[label] = combo
        
        def confirm_details():
            hostel_id = entries["Hostel ID:"].get()
            name = entries["Hostel Name:"].get()
            location = entries["Location:"].get()
            capacity = entries["Capacity:"].get()
            status = entries["Status:"].get()
            
            if not all([hostel_id, name, location, capacity]):
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            # Show confirmation dialog
            confirm_msg = f"Please confirm hostel details:\n\n"
            confirm_msg += f"Hostel ID: {hostel_id}\n"
            confirm_msg += f"Hostel Name: {name}\n"
            confirm_msg += f"Location: {location}\n"
            confirm_msg += f"Capacity: {capacity}\n"
            confirm_msg += f"Status: {status}\n\n"
            confirm_msg += f"Click OK to confirm or Cancel to go back."
            
            result = messagebox.askokcancel("Confirm Hostel Details", confirm_msg)
            if result:
                save_hostel()
        
        def save_hostel():
            try:
                # Get values from entries
                hostel_id = entries["Hostel ID:"].get()
                name = entries["Hostel Name:"].get()
                location = entries["Location:"].get()
                capacity = entries["Capacity:"].get()
                status = entries["Status:"].get()
                
                # Create Hostel instance
                self.hostel = Hostel(
                    hostel_id=hostel_id,
                    name=name,
                    location=location,
                    capacity=int(capacity),
                    status=status
                )
                
                messagebox.showinfo("Success", 
                    f"Hostel setup completed!\n"
                    f"Name: {self.hostel.name}\n"
                    f"ID: {self.hostel.hostel_id}\n"
                    f"Location: {self.hostel.location}\n"
                    f"Capacity: {self.hostel.capacity}")
                setup_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid number for capacity!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not setup hostel: {str(e)}")
        
        # Buttons frame
        button_frame = tk.Frame(setup_window, bg='#008080')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=confirm_details,
                 bg='#20B2AA', fg='white', width=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Cancel", command=setup_window.destroy,
                 bg='#DC143C', fg='white', width=10).pack(side=tk.LEFT, padx=10)

    def add_warden(self):
        if not self.hostel:
            messagebox.showerror("Error", "Setup hostel first!")
            return
        
        warden_window = tk.Toplevel(self.main_window)
        warden_window.title("Add Warden")
        warden_window.geometry("400x400")
        warden_window.configure(bg='#008080')
        
        tk.Label(warden_window, text="Add Warden Details", font=('Arial', 14), 
                bg='#008080', fg='white').pack(pady=10)
        
        fields = [
            ("First Name:", "entry"),
            ("Last Name:", "entry"),
            ("Contact:", "entry"),
            ("Warden ID:", "entry")
        ]
        
        entries = {}
        
        for label, field_type in fields:
            tk.Label(warden_window, text=label, bg='#008080', fg='white').pack(pady=5)
            if field_type == "entry":
                entry = tk.Entry(warden_window, width=25)
                entry.pack(pady=5)
                entries[label] = entry
        
        def confirm_details():
            first_name = entries["First Name:"].get()
            last_name = entries["Last Name:"].get()
            contact = entries["Contact:"].get()
            warden_id = entries["Warden ID:"].get()
            
            if not all([first_name, last_name, contact, warden_id]):
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            # Show confirmation dialog
            confirm_msg = f"Please confirm warden details:\n\n"
            confirm_msg += f"First Name: {first_name}\n"
            confirm_msg += f"Last Name: {last_name}\n"
            confirm_msg += f"Contact: {contact}\n"
            confirm_msg += f"Warden ID: {warden_id}\n\n"
            confirm_msg += f"Click OK to confirm or Cancel to go back."
            
            result = messagebox.askokcancel("Confirm Warden Details", confirm_msg)
            if result:
                save_warden()
        
        def save_warden():
            try:
                first_name = entries["First Name:"].get()
                last_name = entries["Last Name:"].get()
                contact = entries["Contact:"].get()
                warden_id = entries["Warden ID:"].get()
                
                # Create Warden instance
                self.warden = Warden(
                    first_name=first_name,
                    last_name=last_name,
                    contact=contact,
                    warden_id=warden_id,
                    hostel_id=self.hostel.hostel_id
                )
                self.hostel.assign_warden(self.warden)
                
                messagebox.showinfo("Success", 
                    f"Warden added successfully!\n"
                    f"Name: {self.warden.first_name} {self.warden.last_name}\n"
                    f"ID: {self.warden.warden_id}\n"
                    f"Contact: {self.warden.contact}")
                warden_window.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not add warden: {str(e)}")
        
        # Buttons frame
        button_frame = tk.Frame(warden_window, bg='#008080')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=confirm_details,
                 bg='#20B2AA', fg='white', width=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Cancel", command=warden_window.destroy,
                 bg='#DC143C', fg='white', width=10).pack(side=tk.LEFT, padx=10)

    def create_room(self):
        if not self.hostel:
            messagebox.showerror("Error", "Setup hostel first!")
            return
        
        room_window = tk.Toplevel(self.main_window)
        room_window.title("Create Room")
        room_window.geometry("400x400")
        room_window.configure(bg='#008080')
        
        tk.Label(room_window, text="Create New Room", font=('Arial', 14), 
                bg='#008080', fg='white').pack(pady=10)
        
        fields = [
            ("Room ID:", "entry"),
            ("Room Number:", "entry"),
            ("Capacity:", "entry"),
            ("Status:", "combobox")
        ]
        
        entries = {}
        
        for label, field_type in fields:
            tk.Label(room_window, text=label, bg='#008080', fg='white').pack(pady=5)
            
            if field_type == "entry":
                entry = tk.Entry(room_window, width=25)
                entry.pack(pady=5)
                entries[label] = entry
                
            elif field_type == "combobox":
                combo = ttk.Combobox(room_window, width=22, values=["Available", "Occupied", "Maintenance"])
                combo.set("Available")
                combo.pack(pady=5)
                entries[label] = combo
        
        def confirm_details():
            room_id = entries["Room ID:"].get()
            room_number = entries["Room Number:"].get()
            capacity = entries["Capacity:"].get()
            status = entries["Status:"].get()
            
            if not all([room_id, room_number, capacity]):
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            # Show confirmation dialog
            confirm_msg = f"Please confirm room details:\n\n"
            confirm_msg += f"Room ID: {room_id}\n"
            confirm_msg += f"Room Number: {room_number}\n"
            confirm_msg += f"Capacity: {capacity}\n"
            confirm_msg += f"Status: {status}\n\n"
            confirm_msg += f"Click OK to confirm or Cancel to go back."
            
            result = messagebox.askokcancel("Confirm Room Details", confirm_msg)
            if result:
                save_room()
        
        def save_room():
            try:
                room_id = entries["Room ID:"].get()
                room_number = entries["Room Number:"].get()
                capacity = entries["Capacity:"].get()
                status = entries["Status:"].get()
                
                # Create Room instance
                new_room = Room(
                    room_id=room_id,
                    room_number=room_number,
                    hostel_id=self.hostel.hostel_id,
                    capacity=int(capacity),
                    status=status
                )
                self.rooms.append(new_room)
                self.hostel.add_room(new_room)
                
                messagebox.showinfo("Success", 
                    f"Room created successfully!\n"
                    f"Room Number: {new_room.room_number}\n"
                    f"ID: {new_room.room_id}\n"
                    f"Capacity: {new_room.capacity}")
                room_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid number for capacity!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not create room: {str(e)}")
        
        # Buttons frame
        button_frame = tk.Frame(room_window, bg='#008080')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=confirm_details,
                 bg='#20B2AA', fg='white', width=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Cancel", command=room_window.destroy,
                 bg='#DC143C', fg='white', width=10).pack(side=tk.LEFT, padx=10)

    def add_student(self):
        student_window = tk.Toplevel(self.main_window)
        student_window.title("Add Student")
        student_window.geometry("400x500")
        student_window.configure(bg='#008080')
        
        tk.Label(student_window, text="Add Student Details", font=('Arial', 14), 
                bg='#008080', fg='white').pack(pady=10)
        
        fields = [
            ("First Name:", "entry"),
            ("Last Name:", "entry"),
            ("Contact:", "entry"),
            ("Student ID:", "entry"),
            ("Birth Year:", "entry"),
            ("Gender:", "combobox"),
            ("Course:", "combobox")
        ]
        
        entries = {}
        
        for label, field_type in fields:
            tk.Label(student_window, text=label, bg='#008080', fg='white').pack(pady=5)
            
            if field_type == "entry":
                entry = tk.Entry(student_window, width=25)
                entry.pack(pady=5)
                entries[label] = entry
                
            elif field_type == "combobox":
                if label == "Gender:":
                    combo = ttk.Combobox(student_window, width=22, values=["M", "F"])
                    combo.set("M")
                elif label == "Course:":
                    combo = ttk.Combobox(student_window, width=22, 
                                       values=["Computer Science", "Electrical", "Mechanical", "Civil", "Mathematics", "Physics"])
                    combo.set("Computer Science")
                combo.pack(pady=5)
                entries[label] = combo
        
        def confirm_details():
            first_name = entries["First Name:"].get()
            last_name = entries["Last Name:"].get()
            contact = entries["Contact:"].get()
            student_id = entries["Student ID:"].get()
            birth_year = entries["Birth Year:"].get()
            gender = entries["Gender:"].get()
            course = entries["Course:"].get()
            
            if not all([first_name, last_name, contact, student_id, birth_year]):
                messagebox.showerror("Error", "Please fill all required fields!")
                return
            
            # Show confirmation dialog
            confirm_msg = f"Please confirm student details:\n\n"
            confirm_msg += f"First Name: {first_name}\n"
            confirm_msg += f"Last Name: {last_name}\n"
            confirm_msg += f"Contact: {contact}\n"
            confirm_msg += f"Student ID: {student_id}\n"
            confirm_msg += f"Birth Year: {birth_year}\n"
            confirm_msg += f"Gender: {gender}\n"
            confirm_msg += f"Course: {course}\n\n"
            confirm_msg += f"Click OK to confirm or Cancel to go back."
            
            result = messagebox.askokcancel("Confirm Student Details", confirm_msg)
            if result:
                save_student()
        
        def save_student():
            try:
                first_name = entries["First Name:"].get()
                last_name = entries["Last Name:"].get()
                contact = entries["Contact:"].get()
                student_id = entries["Student ID:"].get()
                birth_year = entries["Birth Year:"].get()
                gender = entries["Gender:"].get()
                course = entries["Course:"].get()
                
                # Create Student instance
                new_student = Student(
                    first_name=first_name,
                    last_name=last_name,
                    contact=contact,
                    student_id=student_id,
                    birth_year=birth_year,
                    age=0,
                    gender=gender,
                    course=course,
                    room_id=None
                )
                self.students.append(new_student)
                
                messagebox.showinfo("Success", 
                    f"Student added successfully!\n"
                    f"Name: {new_student.first_name} {new_student.last_name}\n"
                    f"ID: {new_student.student_id}\n"
                    f"Course: {new_student.course}")
                student_window.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not add student: {str(e)}")
        
        # Buttons frame
        button_frame = tk.Frame(student_window, bg='#008080')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=confirm_details,
                 bg='#20B2AA', fg='white', width=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Cancel", command=student_window.destroy,
                 bg='#DC143C', fg='white', width=10).pack(side=tk.LEFT, padx=10)

    def assign_room(self):
        if not self.warden:
            messagebox.showerror("Error", "Add warden first!")
            return
        if not self.students:
            messagebox.showerror("Error", "No students available!")
            return
        if not self.rooms:
            messagebox.showerror("Error", "No rooms available!")
            return
        
        assign_window = tk.Toplevel(self.main_window)
        assign_window.title("Assign Room")
        assign_window.geometry("400x350")
        assign_window.configure(bg='#008080')
        
        tk.Label(assign_window, text="Assign Room to Student", font=('Arial', 14), 
                bg='#008080', fg='white').pack(pady=10)
        
        # Student selection
        tk.Label(assign_window, text="Select Student:", bg='#008080', fg='white').pack(pady=5)
        available_students = [s for s in self.students if not s.room_id]
        if not available_students:
            messagebox.showerror("Error", "All students already have rooms!")
            assign_window.destroy()
            return
        
        student_var = tk.StringVar()
        student_combo = ttk.Combobox(assign_window, textvariable=student_var, width=30,
                                   values=[f"{s.first_name} {s.last_name} (ID: {s.student_id})" for s in available_students])
        if available_students:
            student_combo.current(0)
        student_combo.pack(pady=5)
        
        # Room selection
        tk.Label(assign_window, text="Select Room:", bg='#008080', fg='white').pack(pady=5)
        available_rooms = [r for r in self.rooms if r.status == "Available"]
        if not available_rooms:
            messagebox.showerror("Error", "No available rooms!")
            assign_window.destroy()
            return
        
        room_var = tk.StringVar()
        room_combo = ttk.Combobox(assign_window, textvariable=room_var, width=30,
                                values=[f"{r.room_number} (Capacity: {r.capacity})" for r in available_rooms])
        if available_rooms:
            room_combo.current(0)
        room_combo.pack(pady=5)
        
        def confirm_assignment():
            student_index = student_combo.current()
            room_index = room_combo.current()
            
            if student_index == -1 or room_index == -1:
                messagebox.showerror("Error", "Please select both student and room!")
                return
            
            student = available_students[student_index]
            room = available_rooms[room_index]
            
            # Show confirmation dialog
            confirm_msg = f"Please confirm room assignment:\n\n"
            confirm_msg += f"Student: {student.first_name} {student.last_name}\n"
            confirm_msg += f"Student ID: {student.student_id}\n"
            confirm_msg += f"Room: {room.room_number}\n"
            confirm_msg += f"Room Capacity: {room.capacity}\n\n"
            confirm_msg += f"Click OK to confirm or Cancel to go back."
            
            result = messagebox.askokcancel("Confirm Room Assignment", confirm_msg)
            if result:
                process_assignment()
        
        def process_assignment():
            try:
                student_index = student_combo.current()
                room_index = room_combo.current()
                
                student = available_students[student_index]
                room = available_rooms[room_index]
                
                # Use warden to assign room
                result = self.warden.assign_room(student, room)
                
                messagebox.showinfo("Success", result)
                assign_window.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Assignment failed: {str(e)}")
        
        # Buttons frame
        button_frame = tk.Frame(assign_window, bg='#008080')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=confirm_assignment,
                 bg='#20B2AA', fg='white', width=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Cancel", command=assign_window.destroy,
                 bg='#DC143C', fg='white', width=10).pack(side=tk.LEFT, padx=10)

    def make_payment(self):
        if not self.students:
            messagebox.showerror("Error", "No students available!")
            return
        
        payment_window = tk.Toplevel(self.main_window)
        payment_window.title("Make Payment")
        payment_window.geometry("400x350")
        payment_window.configure(bg='#008080')
        
        tk.Label(payment_window, text="Make Payment", font=('Arial', 14), 
                bg='#008080', fg='white').pack(pady=10)
        
        # Student selection
        tk.Label(payment_window, text="Select Student:", bg='#008080', fg='white').pack(pady=5)
        student_var = tk.StringVar()
        student_combo = ttk.Combobox(payment_window, textvariable=student_var, width=30,
                                   values=[f"{s.first_name} {s.last_name} (ID: {s.student_id})" for s in self.students])
        if self.students:
            student_combo.current(0)
        student_combo.pack(pady=5)
        
        # Amount entry
        tk.Label(payment_window, text="Amount:", bg='#008080', fg='white').pack(pady=5)
        amount_entry = tk.Entry(payment_window, width=25)
        amount_entry.pack(pady=5)
        
        def confirm_payment():
            student_index = student_combo.current()
            if student_index == -1:
                messagebox.showerror("Error", "Please select a student!")
                return
            
            student = self.students[student_index]
            amount = amount_entry.get()
            
            if not amount:
                messagebox.showerror("Error", "Please enter amount!")
                return
            
            # Show confirmation dialog
            confirm_msg = f"Please confirm payment details:\n\n"
            confirm_msg += f"Student: {student.first_name} {student.last_name}\n"
            confirm_msg += f"Student ID: {student.student_id}\n"
            confirm_msg += f"Amount: ${amount}\n\n"
            confirm_msg += f"Click OK to confirm or Cancel to go back."
            
            result = messagebox.askokcancel("Confirm Payment", confirm_msg)
            if result:
                process_payment()
        
        def process_payment():
            try:
                student_index = student_combo.current()
                student = self.students[student_index]
                amount = amount_entry.get()
                
                # Create payment instance and process it
                from payment import Payment
                from datetime import datetime, timedelta
                
                payment = Payment(
                    payment_id=f"P{len(student.payments)+1:03d}",
                    student_id=student.student_id,
                    amount=float(amount),
                    payment_date=datetime.now(),
                    mode_of_payment="Cash",
                    status="Pending",
                    due_date=datetime.now() + timedelta(days=30),
                    academic_year="2024",
                    semester="Spring"
                )
                
                # Process payment using student's method
                result = student.make_payment(payment)
                payment_result = payment.make_payment()
                
                messagebox.showinfo("Success", 
                    f"Payment processed successfully!\n"
                    f"Student: {student.first_name} {student.last_name}\n"
                    f"Amount: ${amount}\n"
                    f"Status: {payment.status}")
                payment_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount!")
            except Exception as e:
                messagebox.showerror("Error", f"Payment failed: {str(e)}")
        
        # Buttons frame
        button_frame = tk.Frame(payment_window, bg='#008080')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=confirm_payment,
                 bg='#20B2AA', fg='white', width=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Cancel", command=payment_window.destroy,
                 bg='#DC143C', fg='white', width=10).pack(side=tk.LEFT, padx=10)

    def check_status(self):
        if not self.hostel:
            messagebox.showerror("Error", "Setup hostel first!")
            return
        
        status_info = f"=== HOSTEL STATUS ===\n\n"
        status_info += f"Hostel: {self.hostel.name}\n"
        status_info += f"Location: {self.hostel.location}\n"
        status_info += f"Capacity: {self.hostel.capacity}\n"
        status_info += f"Status: {self.hostel.status}\n\n"
        
        status_info += f"Warden: {self.warden.first_name + ' ' + self.warden.last_name if self.warden else 'Not assigned'}\n"
        if self.warden:
            status_info += f"Warden Contact: {self.warden.contact}\n"
            status_info += f"Warden ID: {self.warden.warden_id}\n"
        status_info += f"\n"
        
        status_info += f"Rooms Created: {len(self.rooms)}\n"
        status_info += f"Available Rooms: {len([r for r in self.rooms if r.status == 'Available'])}\n"
        status_info += f"Occupied Rooms: {len([r for r in self.rooms if r.status == 'Occupied'])}\n\n"
        
        status_info += f"Total Students: {len(self.students)}\n"
        status_info += f"Students with Rooms: {len([s for s in self.students if s.room_id])}\n"
        status_info += f"Students without Rooms: {len([s for s in self.students if not s.room_id])}\n"
        
        messagebox.showinfo("Hostel Status", status_info)

    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = HostelSystem()
    app.run()