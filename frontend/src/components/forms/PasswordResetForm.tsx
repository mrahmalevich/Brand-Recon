import { FC, useState } from 'react';

interface PasswordResetFormProps {
  onSubmit?: (email: string) => void;
  onCancel?: () => void;
}

export const PasswordResetForm: FC<PasswordResetFormProps> = ({ 
  onSubmit, 
  onCancel 
}) => {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    
    if (!email) {
      setError('Please enter your email address');
      return;
    }
    
    if (onSubmit) {
      onSubmit(email);
      setSubmitted(true);
    }
  };

  return (
    <div className="form-container">
      <h2 className="form-heading">Reset Your Password</h2>
      
      {error && (
        <div className="form-error">
          {error}
        </div>
      )}
      
      {submitted ? (
        <div className="form-success">
          <p className="mb-6">
            If an account exists with the email <strong>{email}</strong>, you will receive password reset instructions.
          </p>
          <button 
            type="button" 
            className="btn-primary"
            onClick={onCancel}
          >
            Back to Login
          </button>
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          <div className="form-description">
            <p>Enter your email address and we'll send you instructions to reset your password.</p>
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
          
          <div className="btn-container">
            <button
              type="submit"
              className="btn-primary"
            >
              Send Reset Instructions
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
      )}
    </div>
  );
}; 