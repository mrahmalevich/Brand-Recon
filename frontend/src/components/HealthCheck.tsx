import { useHealthCheck } from '../hooks/useHealthCheck';
import { FC } from 'react';

export const HealthCheck: FC = () => {
    const { data, isLoading, isError } = useHealthCheck();

    return (
        <div className="p-2">
            {isLoading && (
                <div className="status-loading">
                    Checking API status...
                </div>
            )}

            {isError && (
                <div className="status-error">
                    Error connecting to API
                </div>
            )}

            {data && (
                <div className="status-success">
                    <p className="status-item">
                        Status: <span className="status-value">{data.status}</span>
                    </p>
                    <p className="status-item">
                        Message: <span className="status-value">{data.message}</span>
                    </p>
                </div>
            )}
        </div>
    );
}; 