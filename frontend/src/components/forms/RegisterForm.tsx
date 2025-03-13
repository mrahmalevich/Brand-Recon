import { FC, useState } from 'react';

interface RegisterData {
  firstName: string;
  lastName: string;
  company: string;
  email: string;
  password: string;
}

interface RegisterFormProps {
  onRegister?: (data: RegisterData) => void;
  onCancel?: () => void;
}

export const RegisterForm: FC<RegisterFormProps> = ({ 
  onRegister, 
  onCancel 
}) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [company, setCompany] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    
    if (!firstName || !lastName || !company || !email || !password || !confirmPassword) {
      setError('Please fill in all fields');
      return;
    }
    
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }
    
    if (onRegister) {
      const registerData: RegisterData = {
        firstName,
        lastName,
        company,
        email,
        password
      };
      onRegister(registerData);
    }
  };

  return (
    <div className="form-container">
      <h2 className="form-heading">Create an Account</h2>
      
      {error && (
        <div className="form-error">
          {error}
        </div>
      )}
      
      <form onSubmit={handleSubmit}>
        <div className="form-field">
          <label htmlFor="first-name" className="form-label">
            First Name
          </label>
          <input
            type="text"
            id="first-name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            placeholder="Enter your first name"
            required
            className="form-input"
          />
        </div>

        <div className="form-field">
          <label htmlFor="last-name" className="form-label">
            Last Name
          </label>
          <input
            type="text"
            id="last-name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            placeholder="Enter your last name"
            required
            className="form-input"
          />
        </div>

        <div className="form-field">
          <label htmlFor="company" className="form-label">
            Company
          </label>
          <input
            type="text"
            id="company"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            placeholder="Enter your company"
            required
            className="form-input"
          />
        </div>
        
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
            placeholder="Create a password"
            required
            className="form-input"
          />
        </div>
        
        <div className="form-field">
          <label htmlFor="confirmPassword" className="form-label">
            Confirm Password
          </label>
          <input
            type="password"
            id="confirmPassword"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            placeholder="Confirm your password"
            required
            className="form-input"
          />
        </div>
        
        <div className="btn-container">
          <button
            type="submit"
            className="btn-primary"
          >
            Register
          </button>
        </div>
        
        <div className="links-center">
          <button 
            type="button" 
            className="btn-link"
            onClick={onCancel}
          >
            Back to Login
          </button>
        </div>
      </form>
    </div>
  );
}; 