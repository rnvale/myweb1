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
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #94a3b8;
  font-weight: 600;
  white-space: nowrap;
}

.segmented-control {
  display: flex;
  background: #f1f5f9;
  border-radius: 8px;
  padding: 2px;
  gap: 1px;
}

.seg-btn {
  padding: 5px 12px;
  border: none;
  background: transparent;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
  color: #64748b;
  cursor: pointer;
  transition: all 0.12s ease;
  white-space: nowrap;
  font-family: inherit;
}

.seg-btn:hover { color: #0f172a; }
.seg-btn.active { background: white; color: #0066FF; font-weight: 600; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }

.seg-more { opacity: 0.6; }
.seg-more:hover { opacity: 1; }

.more-dropdown {
  position: absolute;
  top: 100%;
  margin-top: 4px;
  background: white;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 10px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
  padding: 6px;
  z-index: 300;
  min-width: 140px;
}

.more-item {
  display: block;
  width: 100%;
  padding: 7px 14px;
  border: none;
  background: transparent;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
  color: #64748b;
  cursor: pointer;
  text-align: left;
  font-family: inherit;
  transition: all 0.1s ease;
}

.more-item:hover { background: rgba(0,102,255,0.06); color: #0f172a; }
.more-item.active { background: rgba(0,102,255,0.1); color: #0066FF; font-weight: 600; }

.filter-count {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-left: auto;
  padding: 4px 12px;
  background: rgba(0,102,255,0.06);
  border: 1px solid rgba(0,102,255,0.12);
  border-radius: 6px;
  font-size: 12px;
  color: #0066FF;
  font-weight: 500;
  white-space: nowrap;
}

.count-dot {
  width: 5px; height: 5px; border-radius: 50%;
  background: #0066FF;
}
</style>
