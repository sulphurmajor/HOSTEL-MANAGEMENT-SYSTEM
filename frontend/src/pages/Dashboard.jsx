import React, { useEffect, useState } from 'react';
import { hostelAPI } from '../services/api';
import '../styles/Dashboard.css';

function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      setLoading(true);
      const response = await hostelAPI.getStats();
      setStats(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load statistics');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Students</h3>
          <p className="stat-value">{stats?.total_students || 0}</p>
        </div>
        <div className="stat-card">
          <h3>Available Rooms</h3>
          <p className="stat-value">{stats?.available_rooms || 0}</p>
        </div>
        <div className="stat-card">
          <h3>Pending Payments</h3>
          <p className="stat-value">{stats?.pending_payments || 0}</p>
        </div>
        <div className="stat-card">
          <h3>Active Visitors</h3>
          <p className="stat-value">{stats?.active_visitors || 0}</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
