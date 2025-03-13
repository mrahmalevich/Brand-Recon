import { FC, useEffect } from 'react';
import { useNavigate } from '@tanstack/react-router';

export const Home: FC = () => {
    const navigate = useNavigate();

    useEffect(() => {
        // Redirect to login page
        navigate({ to: '/login' });
    }, [navigate]);

    // Return empty div as this component will redirect immediately
    return <div></div>;
}; 