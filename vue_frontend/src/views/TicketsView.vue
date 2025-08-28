<template>
    <div class="tickets">
        <Sidebar />

        <div class="main-content">
        <div class="content-header">
            <div class="container-fluid">
            <div class="d-flex justify-content-between align-items-center">
                <h1 class="m-0">Chamados</h1>
                <button @click="clearFilters" class="btn btn-outline-secondary btn-sm">
                <i class="bi bi-x-circle"></i> Limpar Filtros
                </button>
            </div>
            </div>
        </div>

        <div class="content">
            <div class="container-fluid">
            <TicketFilters
                :filters="ticketsStore.filters"
                @update-filter="applyFilters"
            />

            <div v-if="ticketsStore.isLoading" class="text-center py-5">
                <div class="spinner-border text-primary"></div>
            </div>

            <div v-else class="row">
                <div
                v-for="ticket in ticketsStore.filteredTickets"
                :key="ticket.id"
                class="col-md-6 col-lg-4 mb-4"
                >
                <TicketCard :ticket="ticket" @open="setSelectedTicket(ticket)" />
                </div>
            </div>
            </div>
        </div>
        </div>

        <TicketModal />
    </div>
</template>

<script setup>
    import { onMounted } from 'vue'
    import { useTicketsStore } from '@/stores/tickets'
    import Sidebar from '@/components/common/Sidebar.vue'
    import TicketCard from '@/components/tickets/TicketCard.vue'
    import TicketFilters from '@/components/tickets/TicketFilters.vue'
    import TicketModal from '@/components/tickets/TicketModal.vue'

    const ticketsStore = useTicketsStore()

    const { fetchTickets, setFilter, clearFilters, setSelectedTicket } = ticketsStore

    const applyFilters = (updatedFilters) => {
        ticketsStore.filters = { ...updatedFilters }
    }

    onMounted(() => {
        fetchTickets()
    })
</script>

<style scoped>
    .tickets {
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
</style>
