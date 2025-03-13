import { AuthResponse, LoginCredentials, RegisterCredentials } from '../store/authTypes';

// Mock API endpoints
const API_BASE_URL = '/api';
const LOGIN_ENDPOINT = `${API_BASE_URL}/auth/login`;
const REGISTER_ENDPOINT = `${API_BASE_URL}/auth/register`;
const REFRESH_TOKEN_ENDPOINT = `${API_BASE_URL}/auth/refresh`;
const LOGOUT_ENDPOINT = `${API_BASE_URL}/auth/logout`;

/**
 * Authentication service for handling API requests
 * In a real app, this would make actual API calls
 */
export const authService = {
  /**
   * Login with email and password
   */
  login: async (credentials: LoginCredentials): Promise<AuthResponse> => {
    // In a real app, this would be an actual API call
    // For demo purposes, we're simulating a successful login
    
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Mock successful response
    if (credentials.email && credentials.password) {
      const expiresAt = Date.now() + 30 * 60 * 1000; // 30 minutes from now
      
      return {
        user: {
          id: '1',
          email: credentials.email,
          firstName: 'Demo',
          lastName: 'User',
          company: 'Demo Company',
          role: 'user'
        },
        tokens: {
          accessToken: 'mock-jwt-token',
          refreshToken: 'mock-refresh-token',
          expiresAt
        }
      };
    }
    
    // Mock error
    throw new Error('Invalid credentials');
  },
  
  /**
   * Register a new user
   */
  register: async (credentials: RegisterCredentials): Promise<AuthResponse> => {
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Mock successful response
    if (credentials.email && credentials.password) {
      const expiresAt = Date.now() + 30 * 60 * 1000; // 30 minutes from now
      
      return {
        user: {
          id: '1',
          email: credentials.email,
          firstName: credentials.firstName,
          lastName: credentials.lastName,
          company: credentials.company,
          role: 'user'
        },
        tokens: {
          accessToken: 'mock-jwt-token',
          refreshToken: 'mock-refresh-token',
          expiresAt
        }
      };
    }
    
    // Mock error
    throw new Error('Registration failed');
  },
  
  /**
   * Refresh the access token using a refresh token
   */
  refreshToken: async (refreshToken: string): Promise<AuthResponse> => {
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Mock successful response
    if (refreshToken) {
      const expiresAt = Date.now() + 30 * 60 * 1000; // 30 minutes from now
      
      return {
        user: {
          id: '1',
          email: 'user@example.com',
          firstName: 'Demo',
          lastName: 'User',
          company: 'Demo Company',
          role: 'user'
        },
        tokens: {
          accessToken: 'new-mock-jwt-token',
          refreshToken: 'new-mock-refresh-token',
          expiresAt
        }
      };
    }
    
    // Mock error
    throw new Error('Invalid refresh token');
  },
  
  /**
   * Logout the user
   */
  logout: async (refreshToken: string): Promise<void> => {
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // In a real app, this would invalidate the token on the server
    return;
  }
}; 