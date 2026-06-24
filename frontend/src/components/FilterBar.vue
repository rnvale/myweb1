<template>
  <div class="filter-panel">
    <div class="filter-row">
      <div class="filter-group">
        <label class="filter-label">Sentiment</label>
        <div class="segmented-control">
          <button
            v-for="opt in sentimentOptions"
            :key="opt.value"
            class="seg-btn"
            :class="{ active: selectedSentiment === opt.value }"
            @click="selectedSentiment = opt.value; emitChange()"
          >{{ opt.label }}</button>
        </div>
      </div>
      <div class="filter-group">
        <label class="filter-label">Category</label>
        <div class="segmented-control">
          <button
            class="seg-btn"
            :class="{ active: selectedCategory === 'all' }"
            @click="selectedCategory = 'all'; emitChange()"
          >All</button>
          <button
            v-for="cat in visibleCategories"
            :key="cat.value"
            class="seg-btn"
            :class="{ active: selectedCategory === cat.value }"
            @click="selectedCategory = cat.value; emitChange()"
          >{{ cat.label }}</button>
          <button
            v-if="hiddenCategories.length > 0"
            class="seg-btn seg-more"
            :class="{ active: showMore }"
            @click="showMore = !showMore"
          >+{{ hiddenCategories.length }}</button>
        </div>
        <div v-if="showMore" class="more-dropdown">
          <button
            v-for="cat in hiddenCategories"
            :key="cat.value"
            class="more-item"
            :class="{ active: selectedCategory === cat.value }"
            @click="selectedCategory = cat.value; showMore = false; emitChange()"
          >{{ cat.label }}</button>
        </div>
      </div>
      <div v-if="totalCount > 0" class="filter-count">
        <div class="count-dot"></div>
        <span>{{ totalCount }} reviews</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import http from '../http'
import emitter from '../utils/eventBus'
import { categoryMap } from '../utils/chineseMap'

const emit = defineEmits(['update:sentimentFilter', 'update:aspectFilter'])

const sentimentOptions = [
  { label: 'All', value: 'all' },
  { label: 'Positive', value: 'positive' },
  { label: 'Negative', value: 'negative' }
]

const selectedSentiment = ref('all')
const selectedCategory = ref('all')
const totalCount = ref(0)
const showMore = ref(false)

const categoryOptions = computed(() =>
  Object.entries(categoryMap).map(([value, label]) => ({ value, label }))
)

const visibleCategories = computed(() => categoryOptions.value.slice(0, 4))
const hiddenCategories = computed(() => categoryOptions.value.slice(4))

onMounted(async () => {
  try { await http.get('/aspect_sentiment') } catch {}
})

const emitChange = () => {
  const filters = { sentiment: selectedSentiment.value, category: selectedCategory.value }
  emitter.emit('filter-change', filters)
  emit('update:sentimentFilter', selectedSentiment.value === 'all' ? '全部' : selectedSentiment.value === 'positive' ? '正面' : '负面')
  emit('update:aspectFilter', selectedCategory.value === 'all' ? '全部' : selectedCategory.value)
  http.post('/filtered_summary', filters).then(r => { totalCount.value = r.data.total }).catch(() => {})
}
</script>

<style scoped>
.filter-panel {
  background: white;
  border: 1px solid rgba(0,0,0,0.06);
  border-radius: 12px;
  padding: 10px 14px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.04);
}

.filter-row {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.filter-label {
  font-size: 10px;
  text-transform: upp