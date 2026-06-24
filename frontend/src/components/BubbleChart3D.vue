<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
    <div v-if="loading" class="chart-overlay">
      <div class="spinner"></div>
      <span>加载 3D 可视化</span>
    </div>
    <div v-if="!loading && noData" class="chart-overlay">
      <span>暂无数据</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts'
import 'echarts-gl'

const props = defineProps<{
  sentimentFilter: string
  aspectFilter: string
}>()

const chartRef = ref<HTMLElement>()
const loading = ref(true)
const noData = ref(false)
let chartInstance: echarts.ECharts | null = null
let resizeTimer: number | null = null

function initChart() {
  if (!chartRef.value) return
  if (chartInstance) chartInstance.dispose()
  chartInstance = echarts.init(chartRef.value)
  fetchData()
}

async function fetchData() {
  if (!chartInstance) return
  loading.value = true
  noData.value = false
  try {
    // 用已有的 /api/aspect_sentiment（不用 /api/aspect_stats 因为那个后端不可用）
    const res = await fetch('https://myweb-bwk2.onrender.com/api/aspect_sentiment')
    const items = await res.json()
    if (!Array.isArray(items) || items.length === 0) {
      noData.value = true
      return
    }

    const mapped = items.map((item: any, i: number) => {
      const pos = item.positive ?? 0
      const neg = item.negative ?? 0
      const total = pos + neg
      const rate = total > 0 ? pos / total : 0.5
      return {
        name: item.aspect || (typeof item._id === 'string' ? item._id : ''),
        value: [i, rate * 10, total],
        positive: pos, negative: neg, rate
      }
    })

    chartInstance.setOption({
      tooltip: {
        formatter: (p: any) => {
          const d = mapped[p.dataIndex]
          if (!d) return ''
          return `<strong>${d.name}</strong><br/>正面: ${d.positive}<br/>负面: ${d.negative}<br/>正面率: ${(d.rate*100).toFixed(1)}%`
        },
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a', fontSize: 12 }
      },
      grid3D: {
        viewControl: { autoRotate: true, autoRotateSpeed: 6, distance: 140 },
        boxWidth: 60, boxHeight: 60, boxDepth: 60
      },
      xAxis3D: { name: 'Index', type: 'value', axisLabel: { show: false }, axisLine: { show: false }, splitLine: { show: false } },
      yAxis3D: { name: 'Positive Rate', type: 'value', max: 10, axisLabel: { color: '#94a3b8', fontSize: 10 } },
      zAxis3D: { name: 'Volume', type: 'value', axisLabel: { color: '#94a3b8', fontSize: 10 } },
      series: [{
        type: 'scatter3D',
        data: mapped.map(d => d.value),
        symbolSize: (val: number[]) => Math.max(5, Math.sqrt(val[2] || 0) * 1.8),
        itemStyle: {
          color: (p: any) => {
            const d = mapped[p.dataIndex]
            if (!d) return '#94a3b8'
            if (d.rate > 0.6) return '#16a34a'
            if (d.rate > 0.4) return '#f59e0b'
            return '#dc2626'
          },
          opacity: 0.78
        },
        emphasis: {
          itemStyle: { opacity: 1 },
          label: { show: true, formatter: (p: any) => mapped[p.dataIndex]?.name || '', fontSize: 11 }
        }
      }]
    })
  } catch (e) {
    console.error('BubbleChart3D:', e)
    noData.value = true
  } finally {
    loading.value = false
  }
}

const handleResize = () => {
  if (resizeTimer) clearTimeout(resizeTimer)
  resizeTimer = window.setTimeout(() => chartInstance?.resize(), 150)
}

onMounted(() => {
  initChart()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  if (resizeTimer) clearTimeout(resizeTimer)
  chartInstance?.dispose()
})

watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 380px; position: relative; }
.chart { width: 100%; height: 100%; }
.chart-overlay {
  position: absolute; inset: 0; display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 8px;
  color: #94a3b8; font-size: 13px; background: white; z-index: 2;
}
.spinner {
  width: 20px; height: 20px; border: 2px solid #e2e8f0;
  border-top-color: #0066FF; border-radius: 50%; animation: spin 0.6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
</style>
