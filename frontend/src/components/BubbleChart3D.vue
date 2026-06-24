<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
    <div v-if="loading" class="loading-chart">
      <div class="loading-spinner"></div>
      <span>Loading 3D visualization...</span>
    </div>
    <div v-if="error" class="error-chart">
      <span>Failed to load data</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, onUnmounted } from 'vue'
import * as echarts from 'echarts/core'
import { ScatterChart } from 'echarts/charts'
import { TooltipComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import 'echarts-gl'

echarts.use([ScatterChart, TooltipComponent, CanvasRenderer])

const props = defineProps<{
  sentimentFilter: string
  aspectFilter: string
}>()

const chartRef = ref<HTMLElement>()
const loading = ref(true)
const error = ref(false)
let chartInstance: echarts.ECharts | null = null
let resizeHandler: (() => void) | null = null

function initChart() {
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)
  resizeHandler = () => chartInstance?.resize()
  window.addEventListener('resize', resizeHandler)
  fetchData()
}

async function fetchData() {
  if (!chartInstance) return
  loading.value = true
  error.value = false
  try {
    const res = await fetch('https://myweb-bwk2.onrender.com/api/aspect_stats')
    const json = await res.json()
    const items = json.data || json || []

    if (items.length === 0) {
      chartInstance.setOption({
        title: { text: 'No data available', left: 'center', top: 'center', textStyle: { color: '#94a3b8', fontSize: 14 } }
      })
      return
    }

    // Map aspects to numeric coordinates for 3D
    const aspects = items.map((item: any) => item.aspect || item.category || item._id)
    const data3d = items.map((item: any, i: number) => {
      const pos = item.positive ?? 0
      const neg = item.negative ?? 0
      const total = pos + neg
      const rate = total > 0 ? (pos / total) : 0.5
      return {
        name: aspects[i],
        value: [rate * 5, i, total],
        positive: pos,
        negative: neg,
        total,
        rate
      }
    })

    chartInstance.setOption({
      tooltip: {
        formatter: (p: any) => {
          const d = data3d[p.dataIndex]
          if (!d) return ''
          return `<strong>${d.name}</strong><br/>Positive: ${d.positive}<br/>Negative: ${d.negative}<br/>Positive Rate: ${(d.rate * 100).toFixed(1)}%`
        },
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a', fontSize: 12 }
      },
      grid3D: {
        viewControl: {
          autoRotate: true,
          autoRotateSpeed: 10,
          distance: 150
        },
        boxWidth: 60,
        boxHeight: 60,
        boxDepth: 60,
        axisPointer: { show: false }
      },
      xAxis3D: {
        name: 'Positive Rate',
        type: 'value',
        min: 0,
        max: 5,
        axisLabel: { color: '#94a3b8', fontSize: 10 },
        nameTextStyle: { color: '#94a3b8', fontSize: 11 }
      },
      yAxis3D: {
        name: 'Aspect',
        type: 'category',
        data: aspects,
        axisLabel: { color: '#94a3b8', fontSize: 9, interval: 0 },
        nameTextStyle: { color: '#94a3b8', fontSize: 11 }
      },
      zAxis3D: {
        name: 'Volume',
        type: 'value',
        axisLabel: { color: '#94a3b8', fontSize: 10 },
        nameTextStyle: { color: '#94a3b8', fontSize: 11 }
      },
      series: [{
        type: 'scatter3D',
        data: data3d.map(d => d.value),
        symbolSize: (val: number[]) => Math.max(6, Math.sqrt(val[2] ?? 0) * 2),
        itemStyle: {
          color: (params: any) => {
            const d = data3d[params.dataIndex]
            if (!d) return '#94a3b8'
            if (d.rate > 0.6) return '#16a34a'
            if (d.rate > 0.4) return '#f59e0b'
            return '#dc2626'
          },
          opacity: 0.8,
          borderWidth: 0
        },
        emphasis: {
          itemStyle: { opacity: 1 },
          label: { show: true, formatter: (p: any) => data3d[p.dataIndex]?.name || '', fontSize: 12 }
        }
      }]
    })
  } catch (e) {
    console.error('BubbleChart3D fetch error:', e)
    error.value = true
  } finally {
    loading.value = false
  }
}

onMounted(() => initChart())
onUnmounted(() => {
  if (resizeHandler) window.removeEventListener('resize', resizeHandler)
  chartInstance?.dispose()
})
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 380px; position: relative; }
.chart { width: 100%; height: 100%; }
.loading-chart, .error-chart {
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
