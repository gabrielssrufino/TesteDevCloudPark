<template>
  <div class="card mb-4 shadow-sm">
    <div class="card-body">
      <div class="row g-3 align-items-end">
        <div class="col-md-4">
          <label class="form-label">Status</label>
          <select class="form-select" v-model="localFilters.status" @change="update">
            <option value="">Todos</option>
            <option v-for="(label, key) in STATUS_VALUES" :key="key" :value="key">{{ label }}</option>
          </select>
        </div>

        <div class="col-md-4">
          <label class="form-label">Prioridade</label>
          <select class="form-select" v-model="localFilters.priority" @change="update">
            <option value="">Todas</option>
            <option v-for="(label, key) in PRIORITY_VALUES" :key="key" :value="key">{{ label }}</option>
          </select>
        </div>

        <div class="col-md-4">
          <label class="form-label">Busca</label>
          <input
            type="text"
            class="form-control"
            v-model="localFilters.search"
            placeholder="Título ou descrição"
            @input="update"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue'
import { STATUS_VALUES, PRIORITY_VALUES } from '@/stores/tickets'

const props = defineProps({
  filters: { type: Object, required: true }
})
const emit = defineEmits(['update-filter'])

const localFilters = reactive({ ...props.filters })

const update = () => {
  emit('update-filter', {
    status: localFilters.status,
    priority: localFilters.priority,
    search: localFilters.search
  })
}

watch(() => props.filters, (newFilters) => {
  Object.assign(localFilters, newFilters)
})
</script>

