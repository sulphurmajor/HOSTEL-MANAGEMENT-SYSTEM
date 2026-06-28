"""
Flask API Backend for Hostel Management System
This serves as a bridge between the React frontend and the Python backend classes
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import sys
from pathlib import Path

# Import your existing Python classes
sys.path.insert(0, str(Path(__file__).parent))

from hostel import Hostel
from room import Room
from student import Student
from warden import Warden
from payment import Payment
from visitor import Visitor

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

# In-memory storage (replace with database later)
hostels = {}
rooms = {}
students = {}
wardens = {}
payments = {}
visitors = {}

# Initialize with sample data
def init_data():
    # Create a sample hostel
    hostel = Hostel("H001", "Boys Hostel", "Campus A", 100, "Active")
    hostels["H001"] = hostel
    
    # Add sample rooms
    room1 = Room("R001", "101", "H001", 2, "Available")
    room2 = Room("R002", "102", "H001", 3, "Available")
    rooms["R001"] = room1
    rooms["R002"] = room2
    hostel.add_room(room1)
    hostel.add_room(room2)

init_data()

# ============== HOSTEL ENDPOINTS ==============

@app.route('/api/hostel/stats', methods=['GET'])
def get_hostel_stats():
    """Get hostel statistics"""
    return jsonify({
        'total_students': len(students),
        'total_rooms': len(rooms),
        'available_rooms': len([r for r in rooms.values() if r.staus == "Available"]),
        'pending_payments': len([p for p in payments.values() if p.get('status') == 'Pending']),
        'active_visitors': len([v for v in visitors.values() if not v.get('check_out_date')]),
        'total_hostels': len(hostels)
    })

# ============== STUDENT ENDPOINTS ==============

@app.route('/api/students', methods=['GET'])
def get_students():
    """Get all students"""
    return jsonify(list(students.values()))

@app.route('/api/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Get a specific student"""
    student = students.get(student_id)
    if student:
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

@app.route('/api/students', methods=['POST'])
def create_student():
    """Create a new student"""
    data = request.json
    student_id = data.get('student_id')
    
    if student_id in students:
        return jsonify({'error': 'Student already exists'}), 400
    
    student_data = {
        'student_id': student_id,
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'dob': data.get('dob'),
        'age': data.get('age'),
        'gender': data.get('gender'),
        'course': data.get('course'),
        'phone': data.get('phone'),
    }
    
    students[student_id] = student_data
    return jsonify(student_data), 201

@app.route('/api/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    """Update a student"""
    if student_id not in students:
        return jsonify({'error': 'Student not found'}), 404
    
    data = request.json
    students[student_id].update(data)
    return jsonify(students[student_id])

@app.route('/api/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student"""
    if student_id in students:
        del students[student_id]
        return jsonify({'message': 'Student deleted'}), 200
    return jsonify({'error': 'Student not found'}), 404

# ============== ROOM ENDPOINTS ==============

@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    """Get all rooms"""
    return jsonify([{
        'room_id': r.room_id,
        'room_number': r.room_number,
        'hostel_id': r.hostel_id,
        'capacity': r.capacity,
        'status': r.staus,
    } for r in rooms.values()])

@app.route('/api/rooms/<room_id>', methods=['GET'])
def get_room(room_id):
    """Get a specific room"""
    room = rooms.get(room_id)
    if room:
        return jsonify({
            'room_id': room.room_id,
            'room_number': room.room_number,
            'hostel_id': room.hostel_id,
            'capacity': room.capacity,
            'status': room.staus,
        })
    return jsonify({'error': 'Room not found'}), 404

@app.route('/api/rooms', methods=['POST'])
def create_room():
    """Create a new room"""
    data = request.json
    room_id = data.get('room_id')
    
    if room_id in rooms:
        return jsonify({'error': 'Room already exists'}), 400
    
    room = Room(
        room_id=room_id,
        room_number=data.get('room_number'),
        hostel_id=data.get('hostel_id'),
        capacity=int(data.get('capacity', 1)),
        status=data.get('status', 'Available')
    )
    
    rooms[room_id] = room
    return jsonify({
        'room_id': room.room_id,
        'room_number': room.room_number,
        'hostel_id': room.hostel_id,
        'capacity': room.capacity,
        'status': room.status,
    }), 201

@app.route('/api/rooms/<room_id>', methods=['PUT'])
def update_room(room_id):
    """Update a room"""
    if room_id not in rooms:
        return jsonify({'error': 'Room not found'}), 404
    
    data = request.json
    room = rooms[room_id]
    
    if 'capacity' in data:
        room.capacity = int(data['capacity'])
    
    return jsonify({
        'room_id': room.room_id,
        'room_number': room.room_number,
        'hostel_id': room.hostel_id,
        'capacity': room.capacity,
        'status': room.staus,
    })

@app.route('/api/rooms/<room_id>', methods=['DELETE'])
def delete_room(room_id):
    """Delete a room"""
    if room_id in rooms:
        del rooms[room_id]
        return jsonify({'message': 'Room deleted'}), 200
    return jsonify({'error': 'Room not found'}), 404

@app.route('/api/rooms/available', methods=['GET'])
def get_available_rooms():
    """Get available rooms"""
    available = [r for r in rooms.values() if r.status == "Available"]
    return jsonify([{
        'room_id': r.room_id,
        'room_number': r.room_number,
        'capacity': r.capacity,
    } for r in available])

# ============== PAYMENT ENDPOINTS ==============

@app.route('/api/payments', methods=['GET'])
def get_payments():
    """Get all payments"""
    return jsonify(list(payments.values()))

@app.route('/api/payments/<payment_id>', methods=['GET'])
def get_payment(payment_id):
    """Get a specific payment"""
    payment = payments.get(payment_id)
    if payment:
        return jsonify(payment)
    return jsonify({'error': 'Payment not found'}), 404

@app.route('/api/payments', methods=['POST'])
def create_payment():
    """Create a new payment"""
    data = request.json
    payment_id = data.get('payment_id')
    
    if payment_id in payments:
        return jsonify({'error': 'Payment already exists'}), 400
    
    payment_data = {
        'payment_id': payment_id,
        'student_id': data.get('student_id'),
        'amount': float(data.get('amount', 0)),
        'payment_date': data.get('payment_date'),
        'status': data.get('status', 'Pending'),
    }
    
    payments[payment_id] = payment_data
    return jsonify(payment_data), 201

@app.route('/api/payments/<payment_id>', methods=['PUT'])
def update_payment(payment_id):
    """Update a payment"""
    if payment_id not in payments:
        return jsonify({'error': 'Payment not found'}), 404
    
    data = request.json
    payments[payment_id].update(data)
    return jsonify(payments[payment_id])

@app.route('/api/payments/<payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    """Delete a payment"""
    if payment_id in payments:
        del payments[payment_id]
        return jsonify({'message': 'Payment deleted'}), 200
    return jsonify({'error': 'Payment not found'}), 404

# ============== VISITOR ENDPOINTS ==============

@app.route('/api/visitors', methods=['GET'])
def get_visitors():
    """Get all visitors"""
    return jsonify(list(visitors.values()))

@app.route('/api/visitors/<visitor_id>', methods=['GET'])
def get_visitor(visitor_id):
    """Get a specific visitor"""
    visitor = visitors.get(visitor_id)
    if visitor:
        return jsonify(visitor)
    return jsonify({'error': 'Visitor not found'}), 404

@app.route('/api/visitors', methods=['POST'])
def create_visitor():
    """Create a new visitor"""
    data = request.json
    visitor_id = data.get('visitor_id')
    
    if visitor_id in visitors:
        return jsonify({'error': 'Visitor already exists'}), 400
    
    visitor_data = {
        'visitor_id': visitor_id,
        'name': data.get('name'),
        'student_id': data.get('student_id'),
        'check_in_date': data.get('check_in_date'),
        'check_out_date': data.get('check_out_date'),
    }
    
    visitors[visitor_id] = visitor_data
    return jsonify(visitor_data), 201

@app.route('/api/visitors/<visitor_id>', methods=['PUT'])
def update_visitor(visitor_id):
    """Update a visitor"""
    if visitor_id not in visitors:
        return jsonify({'error': 'Visitor not found'}), 404
    
    data = request.json
    visitors[visitor_id].update(data)
    return jsonify(visitors[visitor_id])

@app.route('/api/visitors/<visitor_id>', methods=['DELETE'])
def delete_visitor(visitor_id):
    """Delete a visitor"""
    if visitor_id in visitors:
        del visitors[visitor_id]
        return jsonify({'message': 'Visitor deleted'}), 200
    return jsonify({'error': 'Visitor not found'}), 404

# ============== WARDEN ENDPOINTS ==============

@app.route('/api/wardens', methods=['GET'])
def get_wardens():
    """Get all wardens"""
    return jsonify(list(wardens.values()))

@app.route('/api/wardens/<warden_id>', methods=['GET'])
def get_warden(warden_id):
    """Get a specific warden"""
    warden = wardens.get(warden_id)
    if warden:
        return jsonify(warden)
    return jsonify({'error': 'Warden not found'}), 404

@app.route('/api/wardens', methods=['POST'])
def create_warden():
    """Create a new warden"""
    data = request.json
    warden_id = data.get('warden_id')
    
    if warden_id in wardens:
        return jsonify({'error': 'Warden already exists'}), 400
    
    warden_data = {
        'warden_id': warden_id,
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'phone': data.get('phone'),
        'hostel_id': data.get('hostel_id'),
    }
    
    wardens[warden_id] = warden_data
    return jsonify(warden_data), 201

@app.route('/api/wardens/<warden_id>', methods=['PUT'])
def update_warden(warden_id):
    """Update a warden"""
    if warden_id not in wardens:
        return jsonify({'error': 'Warden not found'}), 404
    
    data = request.json
    wardens[warden_id].update(data)
    return jsonify(wardens[warden_id])

@app.route('/api/wardens/<warden_id>', methods=['DELETE'])
def delete_warden(warden_id):
    """Delete a warden"""
    if warden_id in wardens:
        del wardens[warden_id]
        return jsonify({'message': 'Warden deleted'}), 200
    return jsonify({'error': 'Warden not found'}), 404

# ============== ERROR HANDLERS ==============

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("Starting Hostel Management API Server...")
    print("Frontend will be available at: http://localhost:3000")
    print("API Server running at: http://localhost:5000")
    app.run(debug=True, port=5000)
