<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
    <div v-if="loading" class="chart-overlay"><div class="spinner"></div><span>加载 3D 可视化</span></div>
    <div v-if="!loading && noData" class="chart-overlay"><span>暂无数据</span></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts'
import 'echarts-gl'

const props = defineProps<{ sentimentFilter: string; aspectFilter: string }>()
const chartRef = ref<HTMLElement>()
const loading = ref(true)
const noData = ref(false)
let chartInstance: any = null

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
    if (!Array.isArray(items) || items.length === 0) { noData.value = true; return }

    const LABELS: Record<string, string> = {
      'usability':'可用性','general':'整体评价','effectiveness':'有效性',
      'cost':'价格','compatibility':'兼容性','reliability':'可靠性',
      'efficiency':'效率','security':'安全性','safety':'安全',
      'enjoyability':'娱乐性','learnability':'易学性','aesthetics':'美观性'
    }

    const data = items.map((item: any, i: number) => {
      const p = item.positive ?? 0, n = item.negative ?? 0, t = p + n, r = t > 0 ? p / t : 0.5
      return { name: LABELS[item.aspect] || item.aspect, val: [i, r * 10, t], p, n, r }
    })

    chartInstance.setOption({
      tooltip: {
        formatter: (p: any) => {
          const d = data[p.dataIndex]
          return d ? `<strong>${d.name}</strong><br/>正面: ${d.p}<br/>负面: ${d.n}<br/>正面率: ${(d.r*100).toFixed(1)}%` : ''
        },
        backgroundColor: 'rgba(255,255,255,0.95)', borderColor: '#e2e8f0', textStyle: { color: '#0f172a', fontSize: 12 }
      },
      grid3D: {
        viewControl: { autoRotate: true, autoRotateSpeed: 8, distance: 150 },
        boxWidth: 70, boxHeight: 70, boxDepth: 70
      },
      xAxis3D: { type: 'value', axisLabel: { show: false }, splitLine: { show: false } },
      yAxis3D: { name: '正面率', type: 'value', max: 10, axisLabel: { color: '#94a3b8', fontSize: 10 } },
      zAxis3D: { name: '评论量', type: 'value', axisLabel: { color: '#94a3b8', fontSize: 10 } },
      series: [{
        type: 'scatter3D',
        data: data.map(d => d.val),
        symbolSize: (val: number[]) => Math.max(6, Math.sqrt(val[2] || 0) * 2),
        itemStyle: {
          color: (p: any) => { const d = data[p.dataIndex]; return !d ? '#94a3b8' : d.r > 0.6 ? '#16a34a' : d.r > 0.4 ? '#f59e0b' : '#dc2626' },
          opacity: 0.8
        },
        emphasis: {
          itemStyle: { opacity: 1 },
          label: { show: true, formatter: (p: any) => data[p.dataIndex]?.name || '', fontSize: 12 }
        }
      }]
    })
  } catch (e) {
    console.error('3D Bubble:', e)
    noData.value = true
  } finally {
    loading.value = false
  }
}

onMounted(() => { initChart(); window.addEventListener('resize', () => chartInstance?.resize()) })
onUnmounted(() => { chartInstance?.dispose() })
watch(() => [props.sentimentFilter, props.aspectFilter], () => fetchData())
</script>

<style scoped>
.chart-container { width: 100%; height: 380px; position: relative; }
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
