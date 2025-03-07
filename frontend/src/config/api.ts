export const API_BASE_URL = import.meta.env['VITE_API_URL'] || 'http://localhost:8000/api/v1';

export const API_ENDPOINTS = {
    HEALTH: `${API_BASE_URL}/health`,
    USERS: `${API_BASE_URL}/users`,
} as const; 