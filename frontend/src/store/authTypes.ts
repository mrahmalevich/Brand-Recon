export interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  company: string;
  role: string;
}

export interface AuthTokens {
  accessToken: string;
  refreshToken?: string;
  expiresAt?: number; // timestamp in milliseconds
}

export interface AuthState {
  user: User | null;
  tokens: AuthTokens | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterCredentials extends LoginCredentials {
  firstName: string;
  lastName: string;
  company: string;
}

export interface AuthResponse {
  user: User;
  tokens: AuthTokens;
} 