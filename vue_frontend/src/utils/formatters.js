export function formatDate(dateString) {
    if (!dateString) return '-'
    const date = new Date(dateString)
    return date.toLocaleString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    })
}

export function getStatusLabel(status) {
    switch(status) {
        case 'Aberto': return 'Aberto'
        case 'Em Atendimento': return 'Em Atendimento'
        case 'Resolvido': return 'Resolvido'
        case 'Cancelado': return 'Cancelado'
        default: return 'Desconhecido'
    }
}

export function getStatusClass(status) {
    switch(status) {
        case 'Aberto': return 'badge bg-info'
        case 'Em Atendimento': return 'badge bg-warning'
        case 'Resolvido': return 'badge bg-success'
        case 'Cancelado': return 'badge bg-danger'
        default: return 'badge bg-secondary'
    }
}

export function getPriorityLabel(priority) {
    switch(priority) {
        case 'Baixa': return 'Baixa'
        case 'Média': return 'Média'
        case 'Alta': return 'Alta'
        default: return 'Desconhecida'
    }
}

export function getPriorityColor(priority) {
    switch(priority) {
        case 'Baixa': return 'text-info'
        case 'Média': return 'text-warning'
        case 'Alta': return 'text-danger'
        default: return 'text-secondary'
    }
}
