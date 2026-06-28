import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Student APIs
export const studentAPI = {
  getAll: () => api.get('/students'),
  getById: (id) => api.get(`/students/${id}`),
  create: (data) => api.post('/students', data),
  update: (id, data) => api.put(`/students/${id}`, data),
  delete: (id) => api.delete(`/students/${id}`),
};

// Room APIs
export const roomAPI = {
  getAll: () => api.get('/rooms'),
  getById: (id) => api.get(`/rooms/${id}`),
  create: (data) => api.post('/rooms', data),
  update: (id, data) => api.put(`/rooms/${id}`, data),
  delete: (id) => api.delete(`/rooms/${id}`),
  getAvailable: () => api.get('/rooms/available'),
};

// Payment APIs
export const paymentAPI = {
  getAll: () => api.get('/payments'),
  getById: (id) => api.get(`/payments/${id}`),
  create: (data) => api.post('/payments', data),
  update: (id, data) => api.put(`/payments/${id}`, data),
  delete: (id) => api.delete(`/payments/${id}`),
};

// Visitor APIs
export const visitorAPI = {
  getAll: () => api.get('/visitors'),
  getById: (id) => api.get(`/visitors/${id}`),
  create: (data) => api.post('/visitors', data),
  update: (id, data) => api.put(`/visitors/${id}`, data),
  delete: (id) => api.delete(`/visitors/${id}`),
};

// Warden APIs
export const wardenAPI = {
  getAll: () => api.get('/wardens'),
  getById: (id) => api.get(`/wardens/${id}`),
  create: (data) => api.post('/wardens', data),
  update: (id, data) => api.put(`/wardens/${id}`, data),
  delete: (id) => api.delete(`/wardens/${id}`),
};

// Hostel APIs
export const hostelAPI = {
  getStats: () => api.get('/hostel/stats'),
};

export default api;
