<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as echarts from 'echarts/core'
import { PieChart } from 'echarts/charts'
import { TooltipComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([PieChart, TooltipComponent, LegendComponent, CanvasRenderer])

const props = defineProps<{
  sentimentFilter: string
  aspectFilter: string
}>()

const chartRef = ref<HTMLElement>()
let chartInstance: echarts.ECharts | null = null

const COLORS = ['#2563eb', '#16a34a', '#dc2626', '#f59e0b', '#8b5cf6', '#06b6d4', '#ec4899', '#84cc16']

function initChart() {
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)
  fetchData()
}

async function fetchData() {
  if (!chartInstance) return
  try {
    const res = await fetch('https://myweb-bwk2.onrender.com/api/aspect_stats')
    const json = await res.json()
    const items = json.data || json || []

    const pieData = items
      .map((item: any) => ({
        name: item.aspect || item.category || item._id,
        value: (item.positive ?? 0) + (item.negative ?? 0)
      }))
      .filter((d: any) => d.value > 0)

    chartInstance.setOption({
      tooltip: {
        trigger: 'item',
        formatter: '{b}: {c} 条 ({d}%)',
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a' }
      },
      legend: {
        type: 'scroll',
        orient: 'vertical',
        right: 10,
        top: 'center',
        textStyle: { color: '#475569', fontSize: 11 }
      },
      series: [{
        type: 'pie',
        roseType: 'area',
        radius: ['20%', '70%'],
        center: ['40%', '50%'],
        itemStyle: {
          borderRadius: 6,
          borderColor: '#fff',
          borderWidth: 2
        },
        color: COLORS,
        label: { color: '#475569', fontSize: 11 },
        data: pieData
      }]
    })
  } catch (e) {
    console.error('RoseChart fetch error:', e)
  }
}

onMounted(() => initChart())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 320px; }
.chart { width: 100%; height: 100%; }
</style>
