<template>
    <div class="login-container">
        <div class="login-card">
        <div class="login-header">
            <h2><i class="bi bi-tools"></i> Sistema de Chamados</h2>
            <p class="text-muted">Acesso para Técnicos</p>
        </div>

        <form @submit.prevent="handleLogin" class="login-form">
            <div class="form-floating mb-3">
            <input
                type="email"
                class="form-control"
                id="email"
                v-model="form.email"
                placeholder="seu@email.com"
                :disabled="isLoading"
                required
            >
            <label for="email">Email</label>
            </div>

            <div class="form-floating mb-4">
            <input
                type="password"
                class="form-control"
                id="password"
                v-model="form.password"
                placeholder="Senha"
                :disabled="isLoading"
                required
            >
            <label for="password">Senha</label>
            </div>

            <button
            type="submit"
            class="btn btn-primary w-100 py-3"
            :disabled="isLoading"
            >
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2"></span>
            {{ isLoading ? 'Entrando...' : 'Entrar' }}
            </button>
        </form>

        <div v-if="error" class="alert alert-danger mt-3">
            <i class="bi bi-exclamation-triangle-fill me-2"></i>
            {{ error }}
        </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, reactive } from 'vue'
    import { useAuthStore } from '@/stores/auth'

    const authStore = useAuthStore()

    const form = reactive({
        email: 'tecnico@cloudpark.teste',
        password: '123456'
    })

    const error = ref('')
    const isLoading = ref(false)

    const handleLogin = async () => {
        isLoading.value = true
        error.value = ''

        const result = await authStore.login(form)
        
        if (!result.success) {
            error.value = result.error
        }
        
        isLoading.value = false
    }
</script>

<style scoped>
    .login-container {
        min-height: 100vh;
        background: #020024;
        background: linear-gradient(90deg, rgba(2, 0, 36, 1) 0%, rgba(9, 9, 121, 1) 49%, rgba(40, 43, 71, 1) 82%);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }

    .login-card {
        background: white;
        border-radius: 20px;
        padding: 40px;
        width: 100%;
        max-width: 440px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }

    .login-header {
        text-align: center;
        margin-bottom: 30px;
    }

    .login-header h2 {
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .login-form .form-control:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }

    .btn-primary {
        border: none;
        border-radius: 12px;
        font-weight: 600;
        transition: transform 0.2s;
    }

    .btn-primary:hover:not(:disabled) {
        transform: translateY(-2px);
    }
</style>