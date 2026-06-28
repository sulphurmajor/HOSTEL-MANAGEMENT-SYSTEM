# Hostel Management System - Frontend Setup Guide

## Project Structure

```
hostel-management/
├── frontend/                    # React Frontend
│   ├── public/
│   │   └── index.html          # HTML entry point
│   ├── src/
│   │   ├── components/         # React components
│   │   │   └── Navigation.js   # Navigation bar
│   │   ├── pages/              # Page components
│   │   │   ├── Dashboard.js
│   │   │   ├── StudentManagement.js
│   │   │   ├── RoomManagement.js
│   │   │   ├── PaymentManagement.js
│   │   │   ├── VisitorManagement.js
│   │   │   └── WardenManagement.js
│   │   ├── services/
│   │   │   └── api.js          # API calls
│   │   ├── styles/             # CSS files
│   │   ├── App.js              # Main app component
│   │   └── index.js            # React entry point
│   ├── package.json            # Dependencies
│   └── .gitignore
│
├── app.py                      # Flask API backend
├── hostel.py
├── room.py
├── student.py
├── warden.py
├── payment.py
├── visitor.py
└── README.md
```

## Installation & Setup

### Prerequisites
- Node.js (v14 or higher)
- Python 3.7+
- pip (Python package manager)

### Step 1: Install Python Dependencies

```bash
pip install flask flask-cors
```

### Step 2: Setup React Frontend

Navigate to the frontend folder:
```bash
cd frontend
npm install
```

### Step 3: Start the Backend API

In the root project directory:
```bash
python app.py
```

The API will run on `http://localhost:5000`

### Step 4: Start the React Frontend

In the frontend directory (in a new terminal):
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## Features

- **Dashboard**: Overview of hostel statistics
- **Student Management**: Add, view, and delete students
- **Room Management**: Manage hostel rooms
- **Payment Management**: Track student payments
- **Visitor Management**: Log and manage visitors
- **Warden Management**: Manage hostel wardens

## API Endpoints

### Students
- `GET /api/students` - Get all students
- `POST /api/students` - Create new student
- `GET /api/students/<id>` - Get student by ID
- `PUT /api/students/<id>` - Update student
- `DELETE /api/students/<id>` - Delete student

### Rooms
- `GET /api/rooms` - Get all rooms
- `GET /api/rooms/available` - Get available rooms
- `POST /api/rooms` - Create new room
- `GET /api/rooms/<id>` - Get room by ID
- `PUT /api/rooms/<id>` - Update room
- `DELETE /api/rooms/<id>` - Delete room

### Payments
- `GET /api/payments` - Get all payments
- `POST /api/payments` - Create new payment
- `GET /api/payments/<id>` - Get payment by ID
- `PUT /api/payments/<id>` - Update payment
- `DELETE /api/payments/<id>` - Delete payment

### Visitors
- `GET /api/visitors` - Get all visitors
- `POST /api/visitors` - Create new visitor
- `GET /api/visitors/<id>` - Get visitor by ID
- `PUT /api/visitors/<id>` - Update visitor
- `DELETE /api/visitors/<id>` - Delete visitor

### Wardens
- `GET /api/wardens` - Get all wardens
- `POST /api/wardens` - Create new warden
- `GET /api/wardens/<id>` - Get warden by ID
- `PUT /api/wardens/<id>` - Update warden
- `DELETE /api/wardens/<id>` - Delete warden

### Hostel
- `GET /api/hostel/stats` - Get hostel statistics

## Environment Variables

Create a `.env` file in the frontend directory (optional):
```
REACT_APP_API_URL=http://localhost:5000
```

## Build for Production

### Frontend Build
```bash
cd frontend
npm run build
```

This creates a production build in `frontend/build/`

### Backend Deployment
For production, update `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

## Troubleshooting

### CORS Errors
If you get CORS errors, ensure `flask-cors` is installed:
```bash
pip install flask-cors
```

### Port Already in Use
- React: `PORT=3001 npm start`
- Flask: Change port in `app.py`

### Module Not Found Errors
Make sure all dependencies are installed:
```bash
pip install flask flask-cors
cd frontend && npm install
```

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- User authentication & authorization
- Email notifications
- Advanced reporting
- Mobile app
- Payment gateway integration
