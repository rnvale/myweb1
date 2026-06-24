<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as echarts from 'echarts/core'
import { ScatterChart } from 'echarts/charts'
import { TooltipComponent, GridComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import 'echarts-gl'

echarts.use([ScatterChart, TooltipComponent, GridComponent, LegendComponent, CanvasRenderer])

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
    const res = await fetch('https://myweb-bwk2.onrender.com/api/aspect_stats')
    const json = await res.json()
    const items = json.data || json || []

    if (items.length === 0) {
      chartInstance.setOption({
        title: { text: '暂无数据', left: 'center', top: 'center', textStyle: { color: '#94a3b8', fontSize: 14 } }
      })
      return
    }

    const aspects = [...new Set(items.map((item: any) => item.aspect || item.category || item._id))]
    const scatterData = items.map((item: any, index: number) => {
      const aspectValue = String(item.aspect || item.category || item._id || '')
      const actualIdx = aspects.indexOf(aspectValue)
      const aspectIdx = actualIdx < 0 ? 0 : actualIdx
      const positive = item.positive ?? item.positive_count ?? 0
      const negative = item.negative ?? item.negative_count ?? 0
      const total = positive + negative
      const positiveRate = total > 0 ? positive / total : 0.5
      const categoryIndex = index % 3
      return {
        name: aspectValue,
        value: [categoryIndex, aspectIdx % 3, total, positiveRate],
        positive, negative
      }
    })

    chartInstance.setOption({
      tooltip: {
        formatter: (p: any) => {
          const d = scatterData[p.dataIndex]
          if (!d) return ''
          const total = (d.positive || 0) + (d.negative || 0)
          const rate = total > 0 ? ((d.positive / total) * 100).toFixed(1) : '0'
          return `<strong>${d.name}</strong><br/>正面: ${d.positive} 条<br/>负面: ${d.negative} 条<br/>正面率: ${rate}%`
        },
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a', fontSize: 12 }
      },
      grid3D: {
        viewControl: { autoRotate: true },
        boxWidth: 80,
        boxHeight: 80,
        boxDepth: 80
      },
      xAxis3D: {
        type: 'category',
        data: ['正面', '中性', '负面'],
        axisLabel: { color: '#475569' }
      },
      yAxis3D: {
        type: 'category',
        data: aspects.slice(0, 3),
        axisLabel: { color: '#475569' }
      },
      zAxis3D: {
        type: 'value',
        axisLabel: { color: '#94a3b8' }
      },
      series: [{
        type: 'scatter3D',
        data: scatterData.map((s: any) => s.value),
        symbolSize: (val: number[]) => Math.sqrt(val[2] ?? 0) * 2.5 + 2,
        itemStyle: {
          color: (params: any) => {
            const rate = scatterData[params.dataIndex]?.value[3] || 0.5
            if (rate > 0.6) return '#16a34a'
            if (rate > 0.4) return '#f59e0b'
            return '#dc2626'
          },
          opacity: 0.8
        },
        emphasis: { itemStyle: { opacity: 1 } }
      }]
    })
  } catch (e) {
    console.error('BubbleChart3D fetch error:', e)
  }
}

onMounted(() => initChart())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 340px; }
.chart { width: 100%; height: 100%; }
</style>
