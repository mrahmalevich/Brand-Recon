import { create } from 'zustand';
import { AuthState, LoginCredentials, RegisterCredentials, User } from './authTypes';
import { secureStorage } from './secureStorage';
import { authService } from '../services/authService';

// Initial state with values from storage for persistence
const initialState: AuthState = {
  user: secureStorage.getUser(),
  tokens: secureStorage.getTokens(),
  isAuthenticated: !!secureStorage.getTokens() && !secureStorage.isTokenExpired(),
  isLoading: false,
  error: null,
};

// Create the auth store
export const useAuthStore = create<
  AuthState & {
    login: (credentials: LoginCredentials) => Promise<void>;
    register: (credentials: RegisterCredentials) => Promise<void>;
    logout: () => Promise<void>;
    refreshToken: () => Promise<void>;
    updateUser: (user: User) => void;
    clearError: () => void;
  }
>((set, get) => ({
  ...initialState,

  /**
   * Login with email and password
   */
  login: async (credentials: LoginCredentials) => {
    try {
      set({ isLoading: true, error: null });
      
      const response = await authService.login(credentials);
      
      // Store tokens and user data
      secureStorage.setTokens(response.tokens);
      secureStorage.setUser(response.user);
      
      set({
        user: response.user,
        tokens: response.tokens,
        isAuthenticated: true,
        isLoading: false,
      });
    } catch (error) {
      set({
        isLoading: false,
        error: error instanceof Error ? error.message : 'Login failed',
      });
    }
  },

  /**
   * Register a new user
   */
  register: async (credentials: RegisterCredentials) => {
    try {
      set({ isLoading: true, error: null });
      
      const response = await authService.register(credentials);
      
      // Store tokens and user data
      secureStorage.setTokens(response.tokens);
      secureStorage.setUser(response.user);
      
      set({
        user: response.user,
        tokens: response.tokens,
        isAuthenticated: true,
        isLoading: false,
      });
    } catch (error) {
      set({
        isLoading: false,
        error: error instanceof Error ? error.message : 'Registration failed',
      });
    }
  },

  /**
   * Logout the user
   */
  logout: async () => {
    try {
      set({ isLoading: true });
      
      const { tokens } = get();
      
      if (tokens?.refreshToken) {
        await authService.logout(tokens.refreshToken);
      }
      
      // Clear stored auth data
      secureStorage.clearAuth();
      
      set({
        user: null,
        tokens: null,
        isAuthenticated: false,
        isLoading: false,
      });
    } catch (error) {
      // Even if the API call fails, we still want to clear local auth data
      secureStorage.clearAuth();
      
      set({
        user: null,
        tokens: null,
        isAuthenticated: false,
        isLoading: false,
        error: error instanceof Error ? error.message : 'Logout failed',
      });
    }
  },

  /**
   * Refresh the access token
   */
  refreshToken: async () => {
    try {
      const { tokens } = get();
      
      if (!tokens?.refreshToken) {
        throw new Error('No refresh token available');
      }
      
      set({ isLoading: true });
      
      const response = await authService.refreshToken(tokens.refreshToken);
      
      // Store new tokens
      secureStorage.setTokens(response.tokens);
      secureStorage.setUser(response.user);
      
      set({
        tokens: response.tokens,
        user: response.user,
        isAuthenticated: true,
        isLoading: false,
      });
    } catch (error) {
      // If refresh fails, log the user out
      secureStorage.clearAuth();
      
      set({
        user: null,
        tokens: null,
        isAuthenticated: false,
        isLoading: false,
        error: error instanceof Error ? error.message : 'Token refresh failed',
      });
    }
  },

  /**
   * Update user data
   */
  updateUser: (user: User) => {
    secureStorage.setUser(user);
    set({ user });
  },

  /**
   * Clear error state
   */
  clearError: () => {
    set({ error: null });
  },
})); 