import React, { useEffect, useState } from 'react';
import { wardenAPI } from '../services/api';
import '../styles/Management.css';

function WardenManagement() {
  const [wardens, setWardens] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isAdding, setIsAdding] = useState(false);
  const [formData, setFormData] = useState({
    warden_id: '',
    first_name: '',
    last_name: '',
    phone: '',
    hostel_id: '',
  });

  useEffect(() => {
    fetchWardens();
  }, []);

  const fetchWardens = async () => {
    try {
      setLoading(true);
      const response = await wardenAPI.getAll();
      setWardens(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load wardens');
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
      await wardenAPI.create(formData);
      setFormData({
        warden_id: '',
        first_name: '',
        last_name: '',
        phone: '',
        hostel_id: '',
      });
      setIsAdding(false);
      fetchWardens();
    } catch (err) {
      setError('Failed to add warden');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await wardenAPI.delete(id);
        fetchWardens();
      } catch (err) {
        setError('Failed to delete warden');
        console.error(err);
      }
    }
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="management-container">
      <h1>Warden Management</h1>
      
      {error && <div className="error">{error}</div>}
      
      <button 
        className="btn btn-primary"
        onClick={() => setIsAdding(!isAdding)}
      >
        {isAdding ? 'Cancel' : 'Add Warden'}
      </button>

      {isAdding && (
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="warden_id"
            placeholder="Warden ID"
            value={formData.warden_id}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="first_name"
            placeholder="First Name"
            value={formData.first_name}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="last_name"
            placeholder="Last Name"
            value={formData.last_name}
            onChange={handleInputChange}
            required
          />
          <input
            type="tel"
            name="phone"
            placeholder="Phone"
            value={formData.phone}
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
          <button type="submit" className="btn btn-success">Add Warden</button>
        </form>
      )}

      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>Warden ID</th>
              <th>Name</th>
              <th>Phone</th>
              <th>Hostel ID</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {wardens.map(warden => (
              <tr key={warden.warden_id}>
                <td>{warden.warden_id}</td>
                <td>{warden.first_name} {warden.last_name}</td>
                <td>{warden.phone}</td>
                <td>{warden.hostel_id}</td>
                <td>
                  <button 
                    className="btn btn-danger"
                    onClick={() => handleDelete(warden.warden_id)}
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

export default WardenManagement;
