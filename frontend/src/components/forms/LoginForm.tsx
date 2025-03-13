import { FC, useState } from 'react';

interface LoginFormProps {
  onLogin?: (email: string, password: string) => void;
  onRegister?: () => void;
  onResetPassword?: () => void;
}

export const LoginForm: FC<LoginFormProps> = ({ 
  onLogin, 
  onRegister, 
  onResetPassword 
}) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    
    if (!email || !password) {
      setError('Please fill in all fields');
      return;
    }
    
    if (onLogin) {
      onLogin(email, password);
    }
  };

  return (
    <div className="form-container">
      <h2 className="form-heading">Login to Brand Recon</h2>
      
      {error && (
        <div className="form-error">
          {error}
        </div>
      )}
      
      <form onSubmit={handleSubmit}>
        <div className="form-field">
          <label htmlFor="email" className="form-label">
            Email
          </label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            required
            className="form-input"
          />
        </div>
        
        <div className="form-field">
          <label htmlFor="password" className="form-label">
            Password
          </label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
            className="form-input"
          />
        </div>
        
        <div className="btn-container">
          <button
            type="submit"
            className="btn-primary"
          >
            Login
          </button>
        </div>
        
        <div className="links-between">
          <button 
            type="button" 
            className="btn-link"
            onClick={onRegister}
          >
            Register
          </button>
          <button 
            type="button" 
            className="btn-link"
            onClick={onResetPassword}
          >
            Forgot Password?
          </button>
        </div>
      </form>
    </div>
  );
}; 