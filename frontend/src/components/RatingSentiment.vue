<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as echarts from 'echarts/core'
import { BarChart, LineChart } from 'echarts/charts'
import { TooltipComponent, GridComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([BarChart, LineChart, TooltipComponent, GridComponent, LegendComponent, CanvasRenderer])

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
    const res = await fetch(`https://myweb-bwk2.onrender.com/api/rating_sentiment`)
    const data = await res.json()

    // Backend returns array: [{rating, positive, negative, positive_rate, total}]
    if (!Array.isArray(data)) {
      chartInstance.setOption({ backgroundColor: '#ffffff' })
      return
    }

    const ratings = data.map((item: any) => `${item.rating} 星`)
    const positives = data.map((item: any) => item.positive ?? 0)
    const negatives = data.map((item: any) => item.negative ?? 0)
    const totals = data.map((item: any) => item.total ?? 0)

    chartInstance.setOption({
      tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'shadow' },
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a' }
      },
      legend: {
        data: ['正面评论', '负面评论', '总计'],
        top: 0,
        textStyle: { color: '#475569', fontSize: 12 }
      },
      grid: { left: '3%', right: '4%', bottom: '3%', top: '15%', containLabel: true },
      xAxis: {
        type: 'category',
        data: ratings,
        axisLabel: { color: '#475569', fontWeight: 500 },
        axisLine: { lineStyle: { color: '#e2e8f0' } }
      },
      yAxis: {
        type: 'value',
        axisLabel: { color: '#94a3b8' },
        splitLine: { lineStyle: { color: '#f1f5f9' } }
      },
      series: [
        {
          name: '正面评论',
          type: 'bar',
          stack: 'sentiment',
          data: positives,
          itemStyle: { color: '#16a34a', borderRadius: [4, 4, 0, 0] },
          barWidth: '50%'
        },
        {
          name: '负面评论',
          type: 'bar',
          stack: 'sentiment',
          data: negatives,
          itemStyle: { color: '#dc2626', borderRadius: [0, 0, 4, 4] }
        },
        {
          name: '总计',
          type: 'line',
          data: totals,
          lineStyle: { color: '#2563eb', width: 2 },
          itemStyle: { color: '#2563eb' },
          symbol: 'circle',
          symbolSize: 6
        }
      ]
    })
  } catch (e) {
    console.error('RatingSentiment fetch error:', e)
  }
}

onMounted(() => initChart())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 300px; }
.chart { width: 100%; height: 100%; }
</style>
