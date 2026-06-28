import React, { useEffect, useState } from 'react';
import { roomAPI } from '../services/api';
import '../styles/Management.css';

function RoomManagement() {
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isAdding, setIsAdding] = useState(false);
  const [formData, setFormData] = useState({
    room_id: '',
    room_number: '',
    hostel_id: '',
    capacity: '',
    status: 'Available',
  });

  useEffect(() => {
    fetchRooms();
  }, []);

  const fetchRooms = async () => {
    try {
      setLoading(true);
      const response = await roomAPI.getAll();
      setRooms(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load rooms');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await roomAPI.create(formData);
      setFormData({
        room_id: '',
        room_number: '',
        hostel_id: '',
        capacity: '',
        status: 'Available',
      });
      setIsAdding(false);
      fetchRooms();
    } catch (err) {
      setError('Failed to add room');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await roomAPI.delete(id);
        fetchRooms();
      } catch (err) {
        setError('Failed to delete room');
        console.error(err);
      }
    }
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="management-container">
      <h1>Room Management</h1>
      
      {error && <div className="error">{error}</div>}
      
      <button 
        className="btn btn-primary"
        onClick={() => setIsAdding(!isAdding)}
      >
        {isAdding ? 'Cancel' : 'Add Room'}
      </button>

      {isAdding && (
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="room_id"
            placeholder="Room ID"
            value={formData.room_id}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="room_number"
            placeholder="Room Number"
            value={formData.room_number}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="hostel_id"
            placeholder="Hostel ID"
            value={formData.hostel_id}
            onChange={handleInputChange}
            required
          />
          <input
            type="number"
            name="capacity"
            placeholder="Capacity"
            value={formData.capacity}
            onChange={handleInputChange}
            required
          />
          <select
            name="status"
            value={formData.status}
            onChange={handleInputChange}
          >
            <option>Available</option>
            <option>Full</option>
            <option>Maintenance</option>
          </select>
          <button type="submit" className="btn btn-success">Add Room</button>
        </form>
      )}

      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>Room ID</th>
              <th>Room Number</th>
              <th>Capacity</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {rooms.map(room => (
              <tr key={room.room_id}>
                <td>{room.room_id}</td>
                <td>{room.room_number}</td>
                <td>{room.capacity}</td>
                <td>{room.status}</td>
                <td>
                  <button 
                    className="btn btn-danger"
                    onClick={() => handleDelete(room.room_id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default RoomManagement;
