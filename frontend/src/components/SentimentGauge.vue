<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
    <div v-if="loading" class="chart-overlay"><div class="spinner"></div><span>加载仪表盘</span></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts/core'
import { GaugeChart } from 'echarts/charts'
import { TooltipComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import http from '../http'

echarts.use([GaugeChart, TooltipComponent, CanvasRenderer])

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
    const params: Record<string, string> = {}
    if (props.sentimentFilter && props.sentimentFilter !== '全部') params.sentiment = props.sentimentFilter
    if (props.aspectFilter && props.aspectFilter !== '全部') params.aspect = props.aspectFilter

    const res = await http.get('/summary', { params })
    const data = res.data

    const positive = data.sentiment?.positive ?? 0
    const negative = data.sentiment?.negative ?? 0
    const total = positive + negative
    const positiveRate = total > 0 ? ((positive / total) * 100) : 0

    chartInstance.setOption({
      series: [{
        type: 'gauge',
        startAngle: 210,
        endAngle: -30,
        center: ['50%', '55%'],
        radius: '85%',
        min: 0,
        max: 100,
        splitNumber: 10,
        axisLine: {
          show: true,
          lineStyle: {
            width: 20,
            color: [
              [0.3, '#dc2626'],
              [0.5, '#f59e0b'],
              [0.7, '#16a34a'],
              [1, '#15803d']
            ]
          }
        },
        pointer: {
          icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
          length: '60%',
          width: 8,
          itemStyle: { color: '#0f172a' }
        },
        axisTick: { length: 10, lineStyle: { width: 2 } },
        splitLine: { length: 22, lineStyle: { width: 4 } },
        axisLabel: { color: '#64748b', fontSize: 12, distance: 30 },
        title: {
          offsetCenter: [0, '75%'],
          fontSize: 13,
          color: '#94a3b8',
          fontWeight: 500
        },
        detail: {
          valueAnimation: true,
          formatter: '{value}%',
          color: '#0f172a',
          fontSize: 28,
          fontWeight: 700,
          offsetCenter: [0, '50%']
        },
        data: [{ value: parseFloat(positiveRate.toFixed(1)), name: '正面率' }]
      }]
    })
  } catch (e) {
    console.error('SentimentGauge:', e)
  } finally {
    loading.value = false
  }
}

onMounted(() => initChart())
onUnmounted(() => chartInstance?.dispose())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 300px; position: relative; }
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
