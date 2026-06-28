import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Dashboard from './pages/Dashboard';
import StudentManagement from './pages/StudentManagement';
import RoomManagement from './pages/RoomManagement';
import PaymentManagement from './pages/PaymentManagement';
import VisitorManagement from './pages/VisitorManagement';
import WardenManagement from './pages/WardenManagement';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/students" element={<StudentManagement />} />
            <Route path="/rooms" element={<RoomManagement />} />
            <Route path="/payments" element={<PaymentManagement />} />
            <Route path="/visitors" element={<VisitorManagement />} />
            <Route path="/wardens" element={<WardenManagement />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
