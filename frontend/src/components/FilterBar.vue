<template>
  <div class="filter-bar">
    <div class="filter-group">
      <label class="filter-label">情感</label>
      <el-select
        v-model="selectedSentiment"
        placeholder="全部"
        @change="onFilterChange"
        clearable
        size="default"
        style="min-width: 140px;"
      >
        <el-option label="全部" value="all"></el-option>
        <el-option label="正面" value="positive"></el-option>
        <el-option label="负面" value="negative"></el-option>
      </el-select>
    </div>

    <div class="filter-group">
      <label class="filter-label">方面</label>
      <el-select
        v-model="selectedCategory"
        placeholder="全部"
        @change="onFilterChange"
        clearable
        filterable
        size="default"
        style="min-width: 160px;"
      >
        <el-option label="全部" value="all"></el-option>
        <el-option v-for="cat in categoryOptions" :key="cat.value" :label="cat.label" :value="cat.value"></el-option>
      </el-select>
    </div>

    <div class="filter-badge" v-if="totalCount > 0">
      <span class="badge-dot"></span>
      <span class="badge-text">{{ totalCount }} 条评论</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import http from '../http'
import emitter from '../utils/eventBus'
import { categoryMap } from '../utils/chineseMap'

const selectedSentiment = ref('all')
const selectedCategory = ref('all')
const totalCount = ref(0)

const categoryOptions = computed(() => {
  return Object.entries(categoryMap).map(([value, label]) => ({ value, label }))
})

onMounted(async () => {
  try {
    await http.get('/aspect_sentiment')
  } catch (e) {
    // Silently handle preload
  }
})

const onFilterChange = () => {
  const filters = { sentiment: selectedSentiment.value, category: selectedCategory.value }
  emitter.emit('filter-change', filters)
  http.post('/filtered_summary', filters).then(res => {
    totalCount.value = res.data.total
  }).catch(() => {})
}
</script>

<style scoped>
.filter-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  padding: 10px 16px;
  background: var(--bg-glass);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  transition: border-color var(--transition-fast);
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.filter-label {
  font-size: 11px;
  color: var(--text-muted);
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  white-space: nowrap;
}

.filter-group :deep(.el-select .el-input__wrapper) {
  background-color: #ffffff !important;
  border: 1px solid var(--border-default) !important;
  box-shadow: none !important;
  border-radius: 10px !important;
  min-width: 130px !important;
  transition: all var(--transition-fast) !important;
}

.filter-group :deep(.el-select .el-input__wrapper:hover) {
  border-color: var(--border-strong) !important;
}

.filter-group :deep(.el-select .el-input__wrapper.is-focus) {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-glow) !important;
}

.filter-group :deep(.el-input__inner) {
  color: var(--text-primary) !important;
  font-size: 13px !important;
}

.filter-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-left: auto;
  padding: 6px 14px;
  background: var(--accent-subtle);
  border: 1px solid var(--accent-border);
  border-radius: 20px;
}

.badge-dot {
  width: 5px; height: 5px; border-radius: 50%;
  background: var(--accent);
}

.badge-text {
  font-size: 12px;
  color: var(--accent);
  font-weight: 500;
}
</style>
