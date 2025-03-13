import { Outlet } from "@tanstack/react-router";
import type { FunctionComponent } from "../common/types";

/**
 * AuthProvider component that wraps the entire application
 * This provides the authentication context to all routes
 */
export const AuthProvider = (): FunctionComponent => {
  return <Outlet />;
}; 