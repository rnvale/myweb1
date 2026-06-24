<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
    <div v-if="loading" class="loading-chart">
      <div class="loading-spinner"></div>
      <span>Loading heatmap...</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as echarts from 'echarts/core'
import { HeatmapChart } from 'echarts/charts'
import { TooltipComponent, GridComponent, VisualMapComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([HeatmapChart, TooltipComponent, GridComponent, VisualMapComponent, CanvasRenderer])

const props = defineProps<{
  sentimentFilter: string
  aspectFilter: string
}>()

const chartRef = ref<HTMLElement>()
const loading = ref(true)
let chartInstance: echarts.ECharts | null = null

function initChart() {
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)
  fetchData()
}

async function fetchData() {
  if (!chartInstance) return
  loading.value = true
  try {
    const res = await fetch('https://myweb-bwk2.onrender.com/api/emotion_heatmap')
    const data = await res.json()

    if (!Array.isArray(data) || data.length === 0) {
      chartInstance.setOption({ title: { text: 'No data', left: 'center', top: 'center', textStyle: { color: '#94a3b8', fontSize: 14 } } })
      return
    }

    const ratings = [...new Set(data.map((item: any) => item.rating))].sort()
    const aspects = [...new Set(data.map((item: any) => item.category))]

    // Build a proper 2D grid for the heatmap
    const heatmapData: [number, number, number][] = []
    for (const rating of ratings) {
      for (const aspect of aspects) {
        const item = data.find((d: any) => d.rating === rating && d.category === aspect)
        const value = item ? ((item.positive_rate ?? 0) / 100) : 0
        heatmapData.push([ratings.indexOf(rating), aspects.indexOf(aspect), value])
      }
    }

    chartInstance.setOption({
      tooltip: {
        formatter: (p: any) => {
          const r = ratings[p.value[0]]
          const a = aspects[p.value[1]]
          const v = p.value[2]
          return `<strong>${r} Star</strong> &middot; ${a}<br/>Positive Rate: ${(v * 100).toFixed(1)}%`
        },
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a' }
      },
      grid: { left: '15%', right: '5%', bottom: '12%', top: '8%' },
      xAxis: {
        type: 'category',
        data: ratings.map((r: any) => `${r} Star`),
        splitArea: { show: true },
        axisLabel: { color: '#64748b', fontWeight: 600, fontSize: 11 },
        axisLine: { lineStyle: { color: '#e2e8f0' } }
      },
      yAxis: {
        type: 'category',
        data: aspects,
        splitArea: { show: true },
        axisLabel: { color: '#64748b', fontSize: 10 },
        axisLine: { lineStyle: { color: '#e2e8f0' } }
      },
      visualMap: {
        min: 0,
        max: 1,
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        bottom: 0,
        inRange: {
          color: ['#fecaca', '#fde68a', '#86efac', '#22c55e']
        },
        textStyle: { color: '#64748b', fontSize: 11 }
      },
      series: [{
        type: 'heatmap',
        data: heatmapData,
        label: {
          show: true,
          color: '#0f172a',
          fontSize: 11,
          fontWeight: 600,
          formatter: (p: any) => (p.value[2] * 100).toFixed(0) + '%'
        },
        emphasis: {
          itemStyle: { shadowBlur: 10, shadowColor: 'rgba(0,0,0,0.1)' }
        },
        itemStyle: {
          borderColor: '#fff',
          borderWidth: 2,
          borderRadius: 4
        }
      }]
    })
  } catch (e) {
    console.error('EmotionHeatmap fetch error:', e)
  } finally {
    loading.value = false
  }
}

onMounted(() => initChart())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 380px; position: relative; }
.chart { width: 100%; height: 100%; }
.loading-chart {
  position: absolute; inset: 0; display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 8px;
  color: #94a3b8; font-size: 13px; background: white;
}
.loading-spinner {
  width: 20px; height: 20px; border: 2px solid #e2e8f0;
  border-top-color: #0066FF; border-radius: 50%; animation: spin 0.6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
</style>
