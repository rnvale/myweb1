<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts/core'
import { GaugeChart } from 'echarts/charts'
import { TooltipComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([GaugeChart, TooltipComponent, CanvasRenderer])

const props = defineProps<{
  sentimentFilter: string
  aspectFilter: string
}>()

const chartRef = ref<HTMLElement>()
let chartInstance: echarts.ECharts | null = null

function initChart() {
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)
  fetchData()
}

async function fetchData() {
  if (!chartInstance) return
  try {
    const params = new URLSearchParams()
    if (props.sentimentFilter && props.sentimentFilter !== '全部') params.append('sentiment', props.sentimentFilter)
    if (props.aspectFilter && props.aspectFilter !== '全部') params.append('aspect', props.aspectFilter)

    const res = await fetch(`https://myweb-bwk2.onrender.com/api/summary?${params}`)
    const data = await res.json()

    // Backend returns: {sentiment: {positive: N, negative: N}}
    const sentiment = data.sentiment || {}
    const positive = sentiment.positive ?? 0
    const negative = sentiment.negative ?? 0
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
      }],
      tooltip: {
        formatter: '正面率: {c}%',
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a' }
      }
    })
  } catch (e) {
    console.error('SentimentGauge fetch error:', e)
  }
}

onMounted(() => initChart())

watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 300px; }
.chart { width: 100%; height: 100%; }
</style>
