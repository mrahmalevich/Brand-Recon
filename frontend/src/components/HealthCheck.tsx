import { useHealthCheck } from '../hooks/useHealthCheck';
import { FC } from 'react';

export const HealthCheck: FC = () => {
    const { data, isLoading, isError } = useHealthCheck();

    return (
        <div className="health-check">
            <h2>API Status</h2>
            {isLoading && (
                <div className="status loading">
                    Checking API status...
                </div>
            )}
            {isError && (
                <div className="status error">
                    Error connecting to API
                </div>
            )}
            {data && (
                <div className="status success">
                    <p>Status: <span>{data.status}</span></p>
                    <p>Message: <span>{data.message}</span></p>
                </div>
            )}
            <style>{`
                .health-check {
                    padding: 1rem;
                }
                
                .health-check h2 {
                    color: #34495e;
                    margin-bottom: 1.5rem;
                }
                
                .status {
                    padding: 1rem;
                    border-radius: 6px;
                    margin-top: 1rem;
                }
                
                .loading {
                    background-color: #f8f9fa;
                    color: #6c757d;
                }
                
                .error {
                    background-color: #fee2e2;
                    color: #dc2626;
                }
                
                .success {
                    background-color: #ecfdf5;
                    color: #059669;
                }
                
                .success p {
                    margin: 0.5rem 0;
                }
                
                .success span {
                    font-weight: bold;
                }
            `}</style>
        </div>
    );
}; 