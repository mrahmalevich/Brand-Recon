import { HealthCheck } from '../components/HealthCheck';
import { FC, useState } from 'react';
import { LoginForm } from '../components/forms/LoginForm';
import { RegisterForm } from '../components/forms/RegisterForm';
import { PasswordResetForm } from '../components/forms/PasswordResetForm';
import { Modal } from '../components/ui/Modal';

// Define the RegisterData interface to match the one in RegisterForm
interface RegisterData {
  firstName: string;
  lastName: string;
  company: string;
  email: string;
  password: string;
}

export const Home: FC = () => {
    const [showHealthCheck, setShowHealthCheck] = useState(false);
    const [showRegisterForm, setShowRegisterForm] = useState(false);
    const [showPasswordResetForm, setShowPasswordResetForm] = useState(false);

    const handleLogin = (email: string, password: string) => {
        console.log('Login attempt with:', email, password);
        // TODO: Implement actual login logic
    };

    const handleRegister = () => {
        setShowRegisterForm(true);
        setShowPasswordResetForm(false);
    };

    const handleRegisterSubmit = (data: RegisterData) => {
        console.log('Register attempt with data:', data);
        // TODO: Implement actual registration logic
        // For now, just go back to login form
        setShowRegisterForm(false);
    };

    const handleRegisterCancel = () => {
        setShowRegisterForm(false);
    };

    const handleResetPassword = () => {
        setShowPasswordResetForm(true);
        setShowRegisterForm(false);
    };

    const handlePasswordResetSubmit = (email: string) => {
        console.log('Password reset requested for:', email);
        // TODO: Implement actual password reset logic
    };

    const handlePasswordResetCancel = () => {
        setShowPasswordResetForm(false);
    };

    const toggleHealthCheck = () => {
        setShowHealthCheck(prev => !prev);
    };

    const renderMainContent = () => {
        if (showRegisterForm) {
            return (
                <RegisterForm
                    onRegister={handleRegisterSubmit}
                    onCancel={handleRegisterCancel}
                />
            );
        }

        if (showPasswordResetForm) {
            return (
                <PasswordResetForm
                    onSubmit={handlePasswordResetSubmit}
                    onCancel={handlePasswordResetCancel}
                />
            );
        }

        return (
            <LoginForm
                onLogin={handleLogin}
                onRegister={handleRegister}
                onResetPassword={handleResetPassword}
            />
        );
    };

    return (
        <div className="app-container">
            <main className="main-content">
                {renderMainContent()}
            </main>

            <footer className="app-footer">
                <button
                    className="btn-link"
                    onClick={toggleHealthCheck}
                >
                    Show Health Check
                </button>
            </footer>

            <Modal
                isOpen={showHealthCheck}
                onClose={() => setShowHealthCheck(false)}
                title="API Health Check"
            >
                <HealthCheck />
            </Modal>
        </div>
    );
}; 