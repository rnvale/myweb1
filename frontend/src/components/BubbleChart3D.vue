<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
    <div v-if="loading" class="chart-overlay"><div class="spinner"></div><span>加载气泡图</span></div>
    <div v-if="!loading && noData" class="chart-overlay"><span>暂无数据</span></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts'
import 'echarts-gl'
import http from '../http'

const props = defineProps<{ sentimentFilter: string; aspectFilter: string }>()
const chartRef = ref<HTMLElement>()
const loading = ref(true)
const noData = ref(false)
let chartInstance: echarts.ECharts | null = null

const LABEL_MAP: Record<string, string> = {
  'usability': '可用性', 'general': '整体评价', 'effectiveness': '有效性',
  'cost': '价格', 'compatibility': '兼容性', 'reliability': '可靠性',
  'efficiency': '效率', 'security': '安全性', 'safety': '安全',
  'enjoyability': '娱乐性', 'learnability': '易学性', 'aesthetics': '美观性'
}

const COLORS = ['#2563eb', '#16a34a', '#dc2626', '#f59e0b', '#8b5cf6', '#06b6d4', '#ec4899', '#84cc16', '#f97316', '#14b8a6', '#a855f7', '#0ea5e9']

function initChart() {
  if (!chartRef.value) return
  if (chartInstance) chartInstance.dispose()
  chartInstance = echarts.init(chartRef.value)
  fetchData()
}

async function fetchData() {
  if (!chartInstance) return
  loading.value = true; noData.value = false
  try {
    const res = await http.get('/aspect_sentiment')
    const items = res.data
    if (!Array.isArray(items) || items.length === 0) { noData.value = true; return }

    const data = items.map((item: any, i: number) => {
      const p = item.positive ?? 0, n = item.negative ?? 0, t = p + n, r = t > 0 ? p / t : 0.5
      return { name: LABEL_MAP[item.aspect] || item.aspect, x: r * 100, y: i, size: t, p, n, r }
    })

    chartInstance.setOption({
      tooltip: {
        formatter: (p: any) => {
          const d = data[p.dataIndex]
          return d ? `<strong>${d.name}</strong><br/>正面: ${d.p}<br/>负面: ${d.n}<br/>正面率: ${(d.r*100).toFixed(1)}%` : ''
        },
        backgroundColor: 'rgba(255,255,255,0.95)', borderColor: '#e2e8f0', textStyle: { color: '#0f172a' }
      },
      grid: { left: '12%', right: '8%', top: '10%', bottom: '10%', containLabel: true },
      xAxis: {
        type: 'value', name: '正面率', min: 0, max: 100,
        axisLabel: { color: '#94a3b8', formatter: '{value}%' },
        splitLine: { lineStyle: { color: '#f1f5f9', type: 'dashed' } },
        nameTextStyle: { color: '#94a3b8', fontSize: 11 }
      },
      yAxis: {
        type: 'category', data: data.map(d => d.name),
        axisLabel: { color: '#64748b', fontSize: 11, fontWeight: 500 },
        splitLine: { lineStyle: { color: '#f1f5f9' } }
      },
      series: [{
        type: 'scatter',
        data: data.map(d => ({ value: [d.x, d.name, d.size], name: d.name })),
        symbolSize: (val: any) => Math.max(8, Math.sqrt(val[2] || 0) * 1.5),
        itemStyle: {
          color: (p: any) => {
            const d = data[p.dataIndex]
            return !d ? '#94a3b8' : d.r > 0.6 ? '#16a34a' : d.r > 0.4 ? '#f59e0b' : '#dc2626'
          },
          opacity: 0.7, borderColor: '#fff', borderWidth: 1
        },
        label: {
          show: true, position: 'right', formatter: (p: any) => p.name,
          color: '#64748b', fontSize: 10
        },
        emphasis: {
          itemStyle: { opacity: 1, shadowBlur: 10, shadowColor: 'rgba(0,0,0,0.15)' },
          label: { fontSize: 12, fontWeight: 600 }
        }
      }]
    })
  } catch (e) {
    console.error('BubbleChart:', e)
    noData.value = true
  } finally { loading.value = false }
}

onMounted(() => { initChart(); window.addEventListener('resize', () => chartInstance?.resize()) })
onUnmounted(() => { chartInstance?.dispose(); window.removeEventListener('resize', () => chartInstance?.resize()) })
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
  border-top-color: #2563eb; border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
</style>