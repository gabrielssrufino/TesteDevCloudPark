import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
import router from '@/router'

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json'
    }
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token')
        if (token) {
        config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => Promise.reject(error)
)

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const authStore = useAuthStore()
        
        if (error.response?.status === 401) {
        try {
            await authStore.refreshToken()
            const originalRequest = error.config
            const token = localStorage.getItem('access_token')
            originalRequest.headers.Authorization = `Bearer ${token}`
            return api(originalRequest)
        } catch (refreshError) {
            authStore.logout()
            router.push('/login')
        }
        }
        
        return Promise.reject(error)
    }
)

export default api