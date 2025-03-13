import { Navigate, Outlet } from '@tanstack/react-router';
import { useAuth } from '../hooks/useAuth';
import type { FunctionComponent } from '../common/types';

interface ProtectedRouteProps {
  requiredRole?: string;
}

/**
 * Protected route component that redirects unauthenticated users to the login page
 * Can also check for specific roles if requiredRole is provided
 */
export const ProtectedRoute = ({ requiredRole }: ProtectedRouteProps): FunctionComponent => {
  const { isAuthenticated, user } = useAuth();
  
  // If user is not authenticated, redirect to login
  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }
  
  // If a specific role is required, check if user has that role
  if (requiredRole && user?.role !== requiredRole) {
    // Redirect to dashboard or show unauthorized page
    return <Navigate to="/dashboard" />;
  }
  
  // User is authenticated and has the required role, render the child routes
  return <Outlet />;
}; 