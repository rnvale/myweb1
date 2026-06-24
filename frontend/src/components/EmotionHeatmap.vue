<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
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
let chartInstance: echarts.ECharts | null = null

function initChart() {
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)
  fetchData()
}

async function fetchData() {
  if (!chartInstance) return
  try {
    const res = await fetch('https://myweb-bwk2.onrender.com/api/emotion_heatmap')
    const data = await res.json()

    // Backend returns array: [{rating, category, positive_rate, total}]
    if (!Array.isArray(data) || data.length === 0) {
      chartInstance.setOption({ title: { text: '暂无数据', left: 'center', top: 'center', textStyle: { color: '#94a3b8' } } })
      return
    }

    const ratings = [...new Set(data.map((item: any) => item.rating))].sort()
    const aspects = [...new Set(data.map((item: any) => item.category))]

    const heatmapData: [number, number, number][] = data.map((item: any) => {
      const rIdx = ratings.indexOf(item.rating)
      const aIdx = aspects.indexOf(item.category)
      return [rIdx, aIdx, (item.positive_rate ?? 0) / 100]
    })

    chartInstance.setOption({
      tooltip: {
        formatter: (p: any) => {
          const r = ratings[p.value[0]]
          const a = aspects[p.value[1]]
          const v = p.value[2]
          return `${r} 星 · ${a}<br/>正面率: ${(v * 100).toFixed(1)}%`
        },
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a' }
      },
      grid: { left: '12%', right: '5%', bottom: '5%', top: '5%' },
      xAxis: {
        type: 'category',
        data: ratings.map((r: any) => `${r} 星`),
        axisLabel: { color: '#475569', fontWeight: 500 },
        axisLine: { lineStyle: { color: '#e2e8f0' } }
      },
      yAxis: {
        type: 'category',
        data: aspects,
        axisLabel: { color: '#475569', fontSize: 11 },
        splitLine: { lineStyle: { color: '#f1f5f9' } }
      },
      visualMap: {
        min: 0,
        max: 1,
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        top: -5,
        inRange: { color: ['#fca5a5', '#fde68a', '#86efac'] },
        textStyle: { color: '#475569' }
      },
      series: [{
        type: 'heatmap',
        data: heatmapData,
        label: { show: true, color: '#0f172a', fontSize: 10 },
        emphasis: { itemStyle: { shadowBlur: 10, shadowColor: 'rgba(0,0,0,0.15)' } }
      }]
    })
  } catch (e) {
    console.error('EmotionHeatmap fetch error:', e)
  }
}

onMounted(() => initChart())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 340px; }
.chart { width: 100%; height: 100%; }
</style>
