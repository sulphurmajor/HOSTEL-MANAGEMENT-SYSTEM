import React, { useEffect, useState } from 'react';
import { visitorAPI } from '../services/api';
import '../styles/Management.css';

function VisitorManagement() {
  const [visitors, setVisitors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isAdding, setIsAdding] = useState(false);
  const [formData, setFormData] = useState({
    visitor_id: '',
    name: '',
    student_id: '',
    check_in_date: '',
    check_out_date: '',
  });

  useEffect(() => {
    fetchVisitors();
  }, []);

  const fetchVisitors = async () => {
    try {
      setLoading(true);
      const response = await visitorAPI.getAll();
      setVisitors(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load visitors');
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
      await visitorAPI.create(formData);
      setFormData({
        visitor_id: '',
        name: '',
        student_id: '',
        check_in_date: '',
        check_out_date: '',
      });
      setIsAdding(false);
      fetchVisitors();
    } catch (err) {
      setError('Failed to add visitor');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await visitorAPI.delete(id);
        fetchVisitors();
      } catch (err) {
        setError('Failed to delete visitor');
        console.error(err);
      }
    }
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="management-container">
      <h1>Visitor Management</h1>
      
      {error && <div className="error">{error}</div>}
      
      <button 
        className="btn btn-primary"
        onClick={() => setIsAdding(!isAdding)}
      >
        {isAdding ? 'Cancel' : 'Add Visitor'}
      </button>

      {isAdding && (
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="visitor_id"
            placeholder="Visitor ID"
            value={formData.visitor_id}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="name"
            placeholder="Visitor Name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="student_id"
            placeholder="Student ID"
            value={formData.student_id}
            onChange={handleInputChange}
            required
          />
          <input
            type="date"
            name="check_in_date"
            value={formData.check_in_date}
            onChange={handleInputChange}
            required
          />
          <input
            type="date"
            name="check_out_date"
            value={formData.check_out_date}
            onChange={handleInputChange}
          />
          <button type="submit" className="btn btn-success">Add Visitor</button>
        </form>
      )}

      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>Visitor ID</th>
              <th>Name</th>
              <th>Student ID</th>
              <th>Check In</th>
              <th>Check Out</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {visitors.map(visitor => (
              <tr key={visitor.visitor_id}>
                <td>{visitor.visitor_id}</td>
                <td>{visitor.name}</td>
                <td>{visitor.student_id}</td>
                <td>{visitor.check_in_date}</td>
                <td>{visitor.check_out_date}</td>
                <td>
                  <button 
                    className="btn btn-danger"
                    onClick={() => handleDelete(visitor.visitor_id)}
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

export default VisitorManagement;
