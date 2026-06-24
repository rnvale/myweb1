<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
    <div v-if="loading" class="chart-overlay"><div class="spinner"></div><span>生成玫瑰图</span></div>
    <div v-if="!loading && noData" class="chart-overlay"><span>暂无数据</span></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
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
const loading = ref(true)
const noData = ref(false)
let chartInstance: echarts.ECharts | null = null

const COLORS = [
  '#0066FF', '#4ADE80', '#F87171', '#F59E0B', '#7C3AED',
  '#06B6D4', '#EC4899', '#84CC16', '#F97316', '#3B82F6',
  '#14B8A6', '#A855F7'
]

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
    const res = await fetch('https://myweb-bwk2.onrender.com/api/aspect_sentiment')
    const items = await res.json()
    if (!Array.isArray(items) || items.length === 0) {
      noData.value = true
      return
    }

    const pieData = items.map((item: any) => ({
      name: item.aspect || item._id || 'Unknown',
      value: (item.positive ?? 0) + (item.negative ?? 0)
    })).filter((d: any) => d.value > 0)

    chartInstance.setOption({
      tooltip: {
        trigger: 'item',
        formatter: '{b}: {c} ({d}%)',
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: '#e2e8f0',
        textStyle: { color: '#0f172a' }
      },
      legend: {
        orient: 'vertical',
        right: 8,
        top: 'center',
        textStyle: { color: '#475569', fontSize: 10 }
      },
      series: [{
        type: 'pie',
        roseType: 'area',
        radius: ['18%', '72%'],
        center: ['38%', '52%'],
        itemStyle: {
          borderRadius: 8,
          borderColor: '#fff',
          borderWidth: 2
        },
        color: COLORS,
        label: { color: '#475569', fontSize: 10 },
        data: pieData
      }]
    })
  } catch (e) {
    console.error('RoseChart:', e)
    noData.value = true
  } finally {
    loading.value = false
  }
}

onMounted(() => initChart())
onUnmounted(() => chartInstance?.dispose())
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 320px; position: relative; }
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
