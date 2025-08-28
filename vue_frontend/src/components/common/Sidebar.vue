<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="logo-container">
        <div class="logo-icon">
          <i class="bi bi-cloud-fill"></i>
        </div>
        <h2 class="logo-text">CloudPark</h2>
      </div>
    </div>

    <nav class="nav-section">
      <div class="nav-title">Menu</div>
      <div class="nav-links">
        <router-link
          to="/dashboard"
          class="nav-item"
          :class="{ active: isActive('/dashboard') }"
        >
          <div class="nav-icon">
            <i class="bi bi-speedometer2"></i>
          </div>
          <span class="nav-text">Dashboard</span>
        </router-link>

        <router-link
          to="/tickets"
          class="nav-item"
          :class="{ active: isActive('/tickets') }"
        >
          <div class="nav-icon">
            <i class="bi bi-ticket-perforated"></i>
          </div>
          <span class="nav-text">Chamados</span>
        </router-link>
      </div>
    </nav>

    <div class="user-section" v-if="authStore.isAuthenticated">
      <div class="user-card">
        <div class="user-avatar">
          <i class="bi bi-person-fill"></i>
        </div>
        <div class="user-details">
          <div class="user-name">{{ authStore.user.username }}</div>
          <div class="user-email">{{ authStore.user.email }}</div>
        </div>
      </div>
      
      <button class="logout-btn" @click="authStore.logout">
        <i class="bi bi-box-arrow-right"></i>
        <span>Sair</span>
      </button>
    </div>
  </aside>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const authStore = useAuthStore()

const isActive = (path) => route.path.startsWith(path)
</script>

<style scoped>
.sidebar {
  width: 280px;
  background-color: #0f172a;
  color: #cbd5e1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  position: fixed;
  border-right: 1px solid #1e293b;
  box-shadow: 4px 0 15px rgba(0, 0, 0, 0.15);
}

.sidebar-header {
  padding: 28px 24px;
  border-bottom: 1px solid #1e293b;
  background-color: #0f172a;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 14px;
}

.logo-icon {
  width: 38px;
  height: 38px;
  background-color: #3b82f6;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: #ffffff;
  box-shadow: 0 2px 8px rgba(59, 130, 246, 0.2);
}

.logo-text {
  margin: 0;
  font-size: 1.6rem;
  font-weight: 600;
  color: #f1f5f9;
  letter-spacing: -0.02em;
}

.nav-section {
  padding: 24px 0;
  flex: 1;
}

.nav-title {
  padding: 0 24px 16px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #64748b;
  margin-bottom: 8px;
}

.nav-links {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 0 20px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px 18px;
  text-decoration: none;
  color: #94a3b8;
  font-weight: 500;
  font-size: 0.95rem;
  border-radius: 10px;
  transition: all 0.25s ease;
  position: relative;
}

.nav-item:hover {
  background-color: #1e293b;
  color: #e2e8f0;
  transform: translateX(2px);
}

.nav-item.active {
  background-color: #1e293b;
  color: #3b82f6;
  font-weight: 600;
  border-left: 3px solid #3b82f6;
  padding-left: 15px;
}

.nav-item.active .nav-icon {
  color: #3b82f6;
}

.nav-icon {
  width: 22px;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
}

.nav-text {
  flex: 1;
}

.user-section {
  padding: 24px 20px;
  border-top: 1px solid #1e293b;
  background-color: #0c1420;
}

.user-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px;
  background-color: #1e293b;
  border-radius: 12px;
  margin-bottom: 18px;
  border: 1px solid #334155;
  transition: all 0.2s ease;
}

.user-card:hover {
  background-color: #334155;
  border-color: #475569;
}

.user-avatar {
  width: 42px;
  height: 42px;
  background-color: #475569;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: #e2e8f0;
  border: 2px solid #64748b;
}

.user-details {
  flex: 1;
  min-width: 0;
}

.user-name {
  font-weight: 600;
  font-size: 0.95rem;
  color: #f1f5f9;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.user-email {
  font-size: 0.8rem;
  color: #94a3b8;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 3px;
}

.logout-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 14px 18px;
  background-color: #dc2626;
  border: 1px solid #ef4444;
  border-radius: 10px;
  color: #fef2f2;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s ease;
}

.logout-btn:hover {
  background-color: #b91c1c;
  border-color: #dc2626;
  transform: translateY(-1px);
}

.logout-btn:active {
  transform: translateY(0);
}

.nav-item:focus-visible,
.logout-btn:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

@media (max-width: 768px) {
  .sidebar {
    width: 280px;
    transform: translateX(-100%);
    transition: transform 0.3s ease;
    z-index: 1000;
  }
  
  .sidebar.open {
    transform: translateX(0);
  }
}

.sidebar::-webkit-scrollbar {
  width: 6px;
}

.sidebar::-webkit-scrollbar-track {
  background-color: #0f172a;
}

.sidebar::-webkit-scrollbar-thumb {
  background-color: #334155;
  border-radius: 3px;
}

.sidebar::-webkit-scrollbar-thumb:hover {
  background-color: #475569;
}

* {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.nav-item,
.logout-btn,
.user-card {
  transition: all 0.2s ease;
}
</style>