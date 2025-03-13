import { useEffect } from 'react';
import { useAuthStore } from '../store/authStore';
import { secureStorage } from '../store/secureStorage';
import { LoginCredentials, RegisterCredentials, User } from '../store/authTypes';

/**
 * Custom hook for authentication
 * Provides a convenient way to access auth state and methods
 */
export const useAuth = () => {
  const {
    user,
    tokens,
    isAuthenticated,
    isLoading,
    error,
    login,
    register,
    logout,
    refreshToken,
    updateUser,
    clearError,
  } = useAuthStore();

  // Check token expiration on mount and set up refresh interval
  useEffect(() => {
    // Check if token is expired on mount
    if (tokens && secureStorage.isTokenExpired()) {
      // Try to refresh the token if we have a refresh token
      if (tokens.refreshToken) {
        refreshToken();
      } else {
        // If no refresh token, log the user out
        logout();
      }
    }

    // Set up token refresh interval (every 15 minutes)
    const refreshInterval = setInterval(() => {
      if (tokens?.refreshToken && secureStorage.isTokenExpired()) {
        refreshToken();
      }
    }, 15 * 60 * 1000); // 15 minutes

    // Clean up interval on unmount
    return () => clearInterval(refreshInterval);
  }, [tokens, refreshToken, logout]);

  return {
    user,
    isAuthenticated,
    isLoading,
    error,
    login,
    register,
    logout,
    updateUser,
    clearError,
  };
};

/**
 * Type guard to check if user has a specific role
 */
export const hasRole = (user: User | null, role: string): boolean => {
  return !!user && user.role === role;
}; 