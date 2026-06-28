import React, { useEffect, useState } from 'react';
import { paymentAPI } from '../services/api';
import '../styles/Management.css';

function PaymentManagement() {
  const [payments, setPayments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isAdding, setIsAdding] = useState(false);
  const [formData, setFormData] = useState({
    payment_id: '',
    student_id: '',
    amount: '',
    payment_date: '',
    status: 'Pending',
  });

  useEffect(() => {
    fetchPayments();
  }, []);

  const fetchPayments = async () => {
    try {
      setLoading(true);
      const response = await paymentAPI.getAll();
      setPayments(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load payments');
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
      await paymentAPI.create(formData);
      setFormData({
        payment_id: '',
        student_id: '',
        amount: '',
        payment_date: '',
        status: 'Pending',
      });
      setIsAdding(false);
      fetchPayments();
    } catch (err) {
      setError('Failed to add payment');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await paymentAPI.delete(id);
        fetchPayments();
      } catch (err) {
        setError('Failed to delete payment');
        console.error(err);
      }
    }
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="management-container">
      <h1>Payment Management</h1>
      
      {error && <div className="error">{error}</div>}
      
      <button 
        className="btn btn-primary"
        onClick={() => setIsAdding(!isAdding)}
      >
        {isAdding ? 'Cancel' : 'Add Payment'}
      </button>

      {isAdding && (
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="payment_id"
            placeholder="Payment ID"
            value={formData.payment_id}
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
            type="number"
            name="amount"
            placeholder="Amount"
            value={formData.amount}
            onChange={handleInputChange}
            required
          />
          <input
            type="date"
            name="payment_date"
            value={formData.payment_date}
            onChange={handleInputChange}
            required
          />
          <select
            name="status"
            value={formData.status}
            onChange={handleInputChange}
          >
            <option>Pending</option>
            <option>Completed</option>
            <option>Failed</option>
          </select>
          <button type="submit" className="btn btn-success">Add Payment</button>
        </form>
      )}

      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>Payment ID</th>
              <th>Student ID</th>
              <th>Amount</th>
              <th>Date</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {payments.map(payment => (
              <tr key={payment.payment_id}>
                <td>{payment.payment_id}</td>
                <td>{payment.student_id}</td>
                <td>${payment.amount}</td>
                <td>{payment.payment_date}</td>
                <td>{payment.status}</td>
                <td>
                  <button 
                    className="btn btn-danger"
                    onClick={() => handleDelete(payment.payment_id)}
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

export default PaymentManagement;
