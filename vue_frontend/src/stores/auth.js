import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/services/api'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(null)
    const isLoading = ref(false)
    const error = ref(null)

    const isAuthenticated = computed(() => !!user.value)
    const userEmail = computed(() => user.value?.email || '')

    const login = async (credentials) => {
        isLoading.value = true
        error.value = null

        try {
        const response = await api.post('/auth/login/', credentials)
        const { access, refresh, user: userData } = response.data

        localStorage.setItem('access_token', access)
        localStorage.setItem('refresh_token', refresh)

        user.value = userData

        router.push('/dashboard')

        return { success: true }
        } catch (err) {
        error.value = err.response?.data?.message || 'Erro ao fazer login'
        return { success: false, error: error.value }
        } finally {
        isLoading.value = false
        }
    }

    const logout = () => {
        user.value = null
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        router.push('/login')
    }

    const refreshToken = async () => {
        try {
        const refresh = localStorage.getItem('refresh_token')
        if (!refresh) throw new Error('No refresh token')

        const response = await api.post('/auth/refresh/', {
            refresh
        })

        localStorage.setItem('access_token', response.data.access)
        return response.data.access
        } catch (err) {
        logout()
        throw err
        }
    }

    const checkAuth = async () => {
        const token = localStorage.getItem('access_token')
        if (!token) return false

        try {
        const response = await api.get('/auth/me/')
        user.value = response.data
        return true
        } catch (err) {
        logout()
        return false
        }
    }

    return {
        user,
        isLoading,
        error,

        isAuthenticated,
        userEmail,
        
        login,
        logout,
        refreshToken,
        checkAuth
    }
})