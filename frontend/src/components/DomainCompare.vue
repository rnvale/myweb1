<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as echarts from 'echarts/core'
import { BarChart } from 'echarts/charts'
import { TooltipComponent, GridComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([BarChart, TooltipComponent, GridComponent, LegendComponent, CanvasRenderer])

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
    const filters = {
      sentiment: props.sentimentFilter === '全部' ? 'all' : props.sentimentFilter,
      category: props.aspectFilter === '全部' ? 'all' : props.aspectFilter
    }

    const res = await fetch('https://myweb-bwk2.onrender.com/api/filtered_domain_compare', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(filters)
    })
    const data = await res.json()
    if (!Array.isArray(data) || data.length === 0) {
      chartInstance.setOption({ backgroundColor: '#ffffff' })
      return
    }

    const domains = data.map((d: any) => d.domain || '未知')
    const positives = data.map((d: any) => d.positive ?? 0)
    const negatives = data.map((d: any) => d.negative ?? 0)
    const rates = data.map((d: any) => d.positive_rate ?? 0)

    chartInstance.setOption({
      tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'shadow' },
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a' }
      },
      legend: {
        data: ['正面评论', '负面评论', '正面率'],
        top: 0,
        textStyle: { color: '#475569', fontSize: 12 }
      },
      grid: { left: '3%', right: '5%', bottom: '3%', top: '15%', containLabel: true },
      xAxis: {
        type: 'category',
        data: domains,
        axisLabel: { color: '#475569', fontWeight: 500, rotate: domains.length > 6 ? 20 : 0 },
        axisLine: { lineStyle: { color: '#e2e8f0' } }
      },
      yAxis: [
        {
          type: 'value',
          name: '评论数量',
          nameTextStyle: { color: '#94a3b8', fontSize: 11, fontWeight: 500 },
          axisLabel: { color: '#94a3b8' },
          splitLine: { lineStyle: { color: '#f1f5f9' } }
        },
        {
          type: 'value',
          name: '正面率',
          nameTextStyle: { color: '#2563eb', fontSize: 11, fontWeight: 500 },
          min: 0,
          max: 100,
          axisLabel: { color: '#2563eb', formatter: '{value}%' },
          splitLine: { show: false }
        }
      ],
      series: [
        {
          name: '正面评论',
          type: 'bar',
          stack: 'total',
          data: positives,
          itemStyle: { color: '#16a34a', borderRadius: [4, 4, 0, 0] },
          barWidth: '50%'
        },
        {
          name: '负面评论',
          type: 'bar',
          stack: 'total',
          data: negatives,
          itemStyle: { color: '#dc2626', borderRadius: [0, 0, 4, 4] }
        },
        {
          name: '正面率',
          type: 'line',
          yAxisIndex: 1,
          data: rates,
          lineStyle: { color: '#2563eb', width: 2 },
          itemStyle: { color: '#2563eb' },
          symbol: 'circle',
          symbolSize: 6
        }
      ]
    })
  } catch (e) {
    console.error('DomainCompare fetch error:', e)
  }
}

onMounted(() => initChart())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 360px; }
.chart { width: 100%; height: 100%; }
</style>
