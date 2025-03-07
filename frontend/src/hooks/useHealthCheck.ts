import { useQuery } from '@tanstack/react-query';
import { API_ENDPOINTS } from '../config/api';

interface HealthCheckResponse {
    status: string;
    message: string;
}

async function fetchHealthStatus(): Promise<HealthCheckResponse> {
    const response = await fetch(API_ENDPOINTS.HEALTH);
    if (!response.ok) {
        throw new Error('Failed to fetch health status');
    }
    return response.json() as Promise<HealthCheckResponse>;
}

export function useHealthCheck() {
    return useQuery({
        queryKey: ['health'],
        queryFn: fetchHealthStatus,
        refetchInterval: 30000, // Refetch every 30 seconds
    });
} 