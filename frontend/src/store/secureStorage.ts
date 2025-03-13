import { AuthTokens, User } from './authTypes';

const AUTH_TOKENS_KEY = 'auth_tokens';
const USER_KEY = 'user';

/**
 * Secure storage utility for handling authentication data
 */
export const secureStorage = {
  /**
   * Store authentication tokens
   */
  setTokens: (tokens: AuthTokens): void => {
    try {
      // In a production app, you might want to encrypt tokens before storing
      sessionStorage.setItem(AUTH_TOKENS_KEY, JSON.stringify(tokens));
    } catch (error) {
      console.error('Failed to store auth tokens:', error);
    }
  },

  /**
   * Retrieve authentication tokens
   */
  getTokens: (): AuthTokens | null => {
    try {
      const tokens = sessionStorage.getItem(AUTH_TOKENS_KEY);
      return tokens ? JSON.parse(tokens) as AuthTokens : null;
    } catch (error) {
      console.error('Failed to retrieve auth tokens:', error);
      return null;
    }
  },

  /**
   * Store user data
   */
  setUser: (user: User): void => {
    try {
      localStorage.setItem(USER_KEY, JSON.stringify(user));
    } catch (error) {
      console.error('Failed to store user data:', error);
    }
  },

  /**
   * Retrieve user data
   */
  getUser: (): User | null => {
    try {
      const user = localStorage.getItem(USER_KEY);
      return user ? JSON.parse(user) as User : null;
    } catch (error) {
      console.error('Failed to retrieve user data:', error);
      return null;
    }
  },

  /**
   * Clear all authentication data
   */
  clearAuth: (): void => {
    try {
      sessionStorage.removeItem(AUTH_TOKENS_KEY);
      localStorage.removeItem(USER_KEY);
    } catch (error) {
      console.error('Failed to clear auth data:', error);
    }
  },

  /**
   * Check if tokens are expired
   */
  isTokenExpired: (): boolean => {
    try {
      const tokens = secureStorage.getTokens();
      if (!tokens || !tokens.expiresAt) return true;
      
      // Check if current time is past expiration
      return Date.now() > tokens.expiresAt;
    } catch (error) {
      console.error('Failed to check token expiration:', error);
      return true;
    }
  }
}; 