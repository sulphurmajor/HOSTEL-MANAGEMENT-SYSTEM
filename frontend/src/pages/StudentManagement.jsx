import React, { useEffect, useState } from 'react';
import { studentAPI } from '../services/api';
import '../styles/Management.css';

function StudentManagement() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    student_id: '',
    first_name: '',
    last_name: '',
    dob: '',
    age: '',
    gender: '',
    course: '',
    phone: '',
  });
  const [isAdding, setIsAdding] = useState(false);

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    try {
      setLoading(true);
      const response = await studentAPI.getAll();
      setStudents(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load students');
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
      await studentAPI.create(formData);
      setFormData({
        student_id: '',
        first_name: '',
        last_name: '',
        dob: '',
        age: '',
        gender: '',
        course: '',
        phone: '',
      });
      setIsAdding(false);
      fetchStudents();
    } catch (err) {
      setError('Failed to add student');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await studentAPI.delete(id);
        fetchStudents();
      } catch (err) {
        setError('Failed to delete student');
        console.error(err);
      }
    }
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="management-container">
      <h1>Student Management</h1>
      
      {error && <div className="error">{error}</div>}
      
      <button 
        className="btn btn-primary"
        onClick={() => setIsAdding(!isAdding)}
      >
        {isAdding ? 'Cancel' : 'Add Student'}
      </button>

      {isAdding && (
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="student_id"
            placeholder="Student ID"
            value={formData.student_id}
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
            type="date"
            name="dob"
            value={formData.dob}
            onChange={handleInputChange}
          />
          <input
            type="text"
            name="gender"
            placeholder="Gender"
            value={formData.gender}
            onChange={handleInputChange}
          />
          <input
            type="text"
            name="course"
            placeholder="Course"
            value={formData.course}
            onChange={handleInputChange}
          />
          <input
            type="tel"
            name="phone"
            placeholder="Phone"
            value={formData.phone}
            onChange={handleInputChange}
          />
          <button type="submit" className="btn btn-success">Add Student</button>
        </form>
      )}

      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Gender</th>
              <th>Course</th>
              <th>Phone</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {students.map(student => (
              <tr key={student.student_id}>
                <td>{student.student_id}</td>
                <td>{student.first_name} {student.last_name}</td>
                <td>{student.gender}</td>
                <td>{student.course}</td>
                <td>{student.phone}</td>
                <td>
                  <button 
                    className="btn btn-danger"
                    onClick={() => handleDelete(student.student_id)}
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

export default StudentManagement;
