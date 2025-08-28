import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/services/api'

export const STATUS_VALUES = {
  ABERTO: 'Aberto',
  EM_ATENDIMENTO: 'Em Atendimento',
  RESOLVIDO: 'Resolvido',
  CANCELADO: 'Cancelado'
}

export const PRIORITY_VALUES = {
  BAIXA: 'Baixa',
  MEDIA: 'Média',
  ALTA: 'Alta'
}

export const STATUS_LABELS = {
  'Aberto': 'Aberto',
  'Em Atendimento': 'Em Atendimento',
  'Resolvido': 'Resolvido',
  'Cancelado': 'Cancelado'
}

export const PRIORITY_LABELS = {
  'Baixa': 'Baixa',
  'Média': 'Média',
  'Alta': 'Alta'
}

export const useTicketsStore = defineStore('tickets', () => {
  const tickets = ref([])
  const selectedTicket = ref(null)
  const isLoading = ref(false)
  const error = ref(null)
  const filters = ref({
    status: '',
    priority: '',
    search: ''
  })

  const filteredTickets = computed(() => {
    let result = tickets.value

    if (filters.value.status) {
      result = result.filter(ticket => ticket.status === STATUS_VALUES[filters.value.status])
    }

    if (filters.value.priority) {
      result = result.filter(ticket => ticket.priority === PRIORITY_VALUES[filters.value.priority])
    }

    if (filters.value.search) {
      const search = filters.value.search.toLowerCase()
      result = result.filter(ticket =>
        ticket.title.toLowerCase().includes(search) ||
        ticket.description.toLowerCase().includes(search)
      )
    }

    return result
  })

  const ticketsByStatus = computed(() => {
    return tickets.value.reduce((acc, ticket) => {
      acc[ticket.status] = (acc[ticket.status] || 0) + 1
      return acc
    }, {})
  })

  const fetchTickets = async () => {
    isLoading.value = true
    error.value = null

    try {
      const response = await api.get('/tickets/')
      tickets.value = response.data.results || response.data
    } catch (err) {
      error.value = 'Erro ao carregar chamados'
      console.error('Fetch tickets error:', err)
    } finally {
      isLoading.value = false
    }
  }

  const updateTicketStatus = async (ticketId, newStatusKey) => {
    try {
      const newStatusValue = STATUS_VALUES[newStatusKey]
      await api.patch(`/tickets/${ticketId}/update/`, { status: newStatusValue })

      const ticketIndex = tickets.value.findIndex(t => t.id === ticketId)
      if (ticketIndex !== -1) {
        tickets.value[ticketIndex].status = newStatusValue
      }

      if (selectedTicket.value?.id === ticketId) {
        selectedTicket.value.status = newStatusValue
      }

      return { success: true }
    } catch (err) {
      console.error('Update status error:', err)
      return {
        success: false,
        error: 'Erro ao atualizar status do chamado'
      }
    }
  }

  const setSelectedTicket = (ticket) => selectedTicket.value = ticket
  const clearSelectedTicket = () => selectedTicket.value = null
  const setFilter = (key, value) => filters.value[key] = value
  const clearFilters = () => filters.value = { status: '', priority: '', search: '' }

  return {
    tickets,
    selectedTicket,
    isLoading,
    error,
    filters,
    filteredTickets,
    ticketsByStatus,
    fetchTickets,
    updateTicketStatus,
    setSelectedTicket,
    clearSelectedTicket,
    setFilter,
    clearFilters
  }
})
