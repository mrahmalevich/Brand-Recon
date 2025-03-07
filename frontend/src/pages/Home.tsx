import { HealthCheck } from '../components/HealthCheck';
import { FC } from 'react';

export const Home: FC = () => {
    return (
        <div className="container">
            <header>
                <h1>Brand Recon</h1>
            </header>
            <main>
                <HealthCheck />
            </main>
            <style>{`
                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 2rem;
                    text-align: center;
                }
                
                header {
                    margin-bottom: 2rem;
                }
                
                h1 {
                    color: #2c3e50;
                    font-size: 2.5rem;
                }
                
                main {
                    background: #f8f9fa;
                    padding: 2rem;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
            `}</style>
        </div>
    );
}; 