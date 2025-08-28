<template>
    <div class="card ticket-card shadow-sm">
        <div class="card-body">
        <h5 class="card-title">
            <i class="bi bi-ticket-detailed"></i> {{ ticket.title }}
        </h5>
        <p class="card-text text-muted small">
            {{ ticket.description.slice(0, 80) }}...
        </p>

        <div class="d-flex justify-content-between align-items-center mt-3">
            <span class="badge" :class="getStatusClass(ticket.status)">
            {{ getStatusLabel(ticket.status) }}
            </span>
            <span :class="getPriorityColor(ticket.priority)">
            <i class="bi bi-flag-fill"></i>
            {{ getPriorityLabel(ticket.priority) }}
            </span>
        </div>

        <div class="d-flex justify-content-end mt-3">
            <button
            class="btn btn-outline-primary btn-sm"
            data-bs-toggle="modal"
            data-bs-target="#ticketModal"
            @click="$emit('open')"
            >
            <i class="bi bi-eye"></i> Detalhes
            </button>
        </div>
        </div>
    </div>
</template>

<script setup>
    import { getStatusClass, getStatusLabel, getPriorityColor, getPriorityLabel } from '@/utils/formatters'

    defineProps({
        ticket: { type: Object, required: true }
    })
</script>

<style scoped>
    .ticket-card {
        border-radius: 12px;
        transition: transform 0.2s ease;
    }

    .ticket-card:hover {
        transform: translateY(-3px);
    }
</style>
