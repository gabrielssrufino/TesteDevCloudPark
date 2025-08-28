<template>
    <div class="dashboard">
        <Sidebar />
        
        <div class="main-content">
        <div class="content-header">
            <div class="container-fluid">
            <div class="row">
                <div class="col-sm-6">
                <h1 class="m-0">Dashboard</h1>
                </div>
                <div class="col-sm-6">
                <ol class="breadcrumb float-sm-right">
                    <li class="breadcrumb-item active">Dashboard</li>
                </ol>
                </div>
            </div>
            </div>
        </div>

        <div class="content">
            <div class="container-fluid">
            <div class="row mb-4">
                <div class="col-lg-3 col-6">
                <div class="small-box bg-info">
                    <div class="inner">
                    <h3>{{ ticketsByStatus.aberto || 0 }}</h3>
                    <p>Chamados Abertos</p>
                    </div>
                    <div class="icon">
                    <i class="bi bi-exclamation-circle"></i>
                    </div>
                </div>
                </div>

                <div class="col-lg-3 col-6">
                <div class="small-box bg-warning">
                    <div class="inner">
                    <h3>{{ ticketsByStatus.em_atendimento || 0 }}</h3>
                    <p>Em Atendimento</p>
                    </div>
                    <div class="icon">
                    <i class="bi bi-clock"></i>
                    </div>
                </div>
                </div>

                <div class="col-lg-3 col-6">
                <div class="small-box bg-success">
                    <div class="inner">
                    <h3>{{ ticketsByStatus.resolvido || 0 }}</h3>
                    <p>Resolvidos</p>
                    </div>
                    <div class="icon">
                    <i class="bi bi-check-circle"></i>
                    </div>
                </div>
                </div>

                <div class="col-lg-3 col-6">
                <div class="small-box bg-danger">
                    <div class="inner">
                    <h3>{{ tickets.length }}</h3>
                    <p>Total</p>
                    </div>
                    <div class="icon">
                    <i class="bi bi-list-ul"></i>
                    </div>
                </div>
                </div>
            </div>

            <div class="row">
                <div class="col-12">
                <div class="card">
                    <div class="card-header">
                    <h3 class="card-title">Chamados Recentes</h3>
                    <div class="card-tools">
                        <router-link to="/tickets" class="btn btn-primary btn-sm">
                        <i class="bi bi-arrow-right"></i> Ver Todos
                        </router-link>
                    </div>
                    </div>
                    <div class="card-body">
                    <div v-if="isLoading" class="text-center py-4">
                        <div class="spinner-border text-primary"></div>
                    </div>
                    
                    <div v-else class="table-responsive">
                        <table class="table table-striped">
                        <thead>
                            <tr>
                            <th>#</th>
                            <th>Título</th>
                            <th>Status</th>
                            <th>Prioridade</th>
                            <th>Data</th>
                            <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="ticket in recentTickets" :key="ticket.id">
                            <td>#{{ ticket.id }}</td>
                            <td>{{ ticket.title }}</td>
                            <td>
                                <span class="badge" :class="getStatusClass(ticket.status)">
                                {{ getStatusLabel(ticket.status) }}
                                </span>
                            </td>
                            <td>
                                <span :class="getPriorityColor(ticket.priority)">
                                <i class="bi bi-flag-fill"></i>
                                {{ getPriorityLabel(ticket.priority) }}
                                </span>
                            </td>
                            <td>{{ formatDate(ticket.created_at) }}</td>
                            <td>
                                <button
                                @click="setSelectedTicket(ticket)"
                                class="btn btn-outline-primary btn-sm"
                                data-bs-toggle="modal"
                                data-bs-target="#ticketModal"
                                >
                                <i class="bi bi-eye"></i>
                                </button>
                            </td>
                            </tr>
                        </tbody>
                        </table>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>

        
        <TicketModal />
    </div>
</template>

<script setup>
    import { computed, onMounted } from 'vue'
    import { useTicketsStore } from '@/stores/tickets'
    import Sidebar from '@/components/common/Sidebar.vue'
    import TicketModal from '@/components/tickets/TicketModal.vue'
    import { formatDate, getStatusClass, getStatusLabel, getPriorityColor, getPriorityLabel } from '@/utils/formatters'

    const ticketsStore = useTicketsStore()

    const { tickets, isLoading, ticketsByStatus, setSelectedTicket } = ticketsStore

    const recentTickets = computed(() => {
    return tickets.slice(0, 10) // Show last 10 tickets
    })

    onMounted(async () => {
        await ticketsStore.fetchTickets()
    })
</script>

<style scoped>
    .dashboard {
        display: flex;
        min-height: 100vh;
    }

    .main-content {
        flex: 1;
        margin-left: 280px;
        background-color: #f4f6f9;
    }

    .content-header {
        padding: 15px 30px;
        background: white;
        border-bottom: 1px solid #dee2e6;
    }

    .content {
        padding: 30px;
    }

    .small-box {
        border-radius: 10px;
        padding: 20px;
        color: white;
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
    }

    .small-box .inner h3 {
        font-size: 2.2rem;
        font-weight: bold;
        margin: 0;
    }

    .small-box .inner p {
        font-size: 1rem;
        margin: 5px 0 0 0;
    }

    .small-box .icon {
        position: absolute;
        top: 20px;
        right: 20px;
        font-size: 3rem;
        opacity: 0.3;
    }

    .bg-info { background: linear-gradient(135deg, #3498db, #2980b9); }
    .bg-warning { background: linear-gradient(135deg, #f39c12, #d68910); }
    .bg-success { background: linear-gradient(135deg, #27ae60, #229954); }
    .bg-danger { background: linear-gradient(135deg, #e74c3c, #c0392b); }

    .card {
        border: none;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.08);
    }

    .card-header {
        background: white;
        border-bottom: 1px solid #f0f0f0;
        padding: 20px 25px;
        border-radius: 15px 15px 0 0 !important;
    }
</style>