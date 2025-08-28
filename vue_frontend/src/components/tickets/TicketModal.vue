<template>
    <div class="modal fade" id="ticketModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title">
                <i class="bi bi-ticket-detailed"></i> Detalhes do Chamado
            </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            
            <div class="modal-body" v-if="ticket">
            <h5>{{ ticket.title }}</h5>
            <p>{{ ticket.description }}</p>

            <div class="d-flex gap-3 mb-3">
                <span class="badge" :class="getStatusClass(ticket.status)">
                {{ getStatusLabel(ticket.status) }}
                </span>
                <span :class="getPriorityColor(ticket.priority)">
                <i class="bi bi-flag-fill"></i>
                {{ getPriorityLabel(ticket.priority) }}
                </span>
            </div>

            <small class="text-muted">Aberto em: {{ formatDate(ticket.created_at) }}</small>
            </div>

            <div class="modal-footer">
            <button
                v-for="status in statuses"
                :key="status.value"
                @click="changeStatus(status.value)"
                class="btn btn-sm"
                :class="status.class"
            >
                {{ status.label }}
            </button>
            </div>
        </div>
        </div>
    </div>
</template>

<script setup>
    import { computed } from 'vue'
    import { useTicketsStore } from '@/stores/tickets'
    import { formatDate, getStatusClass, getStatusLabel, getPriorityColor, getPriorityLabel } from '@/utils/formatters'

    const ticketsStore = useTicketsStore()
    const ticket = computed(() => ticketsStore.selectedTicket)

    const statuses = [
        { value: 'aberto', label: 'Aberto', class: 'btn-outline-secondary' },
        { value: 'em_atendimento', label: 'Em Atendimento', class: 'btn-outline-warning' },
        { value: 'resolvido', label: 'Resolvido', class: 'btn-outline-success' },
        { value: 'cancelado', label: 'Cancelado', class: 'btn-outline-danger' }
    ]

    const changeStatus = async (status) => {
        if (ticket.value) {
            await ticketsStore.updateTicketStatus(ticket.value.id, status)
        }
    }
</script>
