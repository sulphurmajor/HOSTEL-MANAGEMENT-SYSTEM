import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Navigation.css';

function Navigation() {
  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          🏛️ Hostel Management
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link to="/" className="nav-link">Dashboard</Link>
          </li>
          <li className="nav-item">
            <Link to="/students" className="nav-link">Students</Link>
          </li>
          <li className="nav-item">
            <Link to="/rooms" className="nav-link">Rooms</Link>
          </li>
          <li className="nav-item">
            <Link to="/payments" className="nav-link">Payments</Link>
          </li>
          <li className="nav-item">
            <Link to="/visitors" className="nav-link">Visitors</Link>
          </li>
          <li className="nav-item">
            <Link to="/wardens" className="nav-link">Wardens</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navigation;
