<template>
  <div class="app-root">
    <!-- Ambient background decoration -->
    <div class="ambient"><div class="ambient-orb ambient-orb-1"></div><div class="ambient-orb ambient-orb-2"></div></div>

    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-brand">
        <div class="brand-check"><svg viewBox="0 0 32 32" fill="none"><rect x="2" y="2" width="28" height="28" rx="8" fill="#2563eb"/><path d="M10 16l4 4 8-8" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div class="brand-text"><span class="brand-name">AppInsight</span><span class="brand-ver">v2.0</span></div>
      </div>
      <nav class="nav">
        <button v-for="item in nav" :key="item.key" class="nav-btn" :class="{active: view === item.key}" @click="view = item.key">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path :d="item.icon"/></svg>
          <span>{{ item.label }}</span>
        </button>
      </nav>
      <div class="sidebar-foot"><div class="sf-label">数据源</div><div class="sf-value">AWARE &middot; 11,321 条评论</div></div>
    </aside>

    <!-- Main -->
    <main class="main">

      <!-- ======================== DASHBOARD ======================== -->
      <section v-if="view === 'dashboard'">
        <div class="hero" style="background-image:url(/img/hero-analytics.jpg)">
          <div class="hero-mask"></div>
          <div class="hero-body">
            <div class="hero-tag">概览</div>
            <h1 class="hero-h1">App 智能分析仪表盘</h1>
            <p class="hero-p">基于 AWARE 数据集对 11,321 条应用评论进行实时情感分析</p>
            <div class="hero-stats">
              <div class="hero-stat"><span class="hero-num">{{ anim.total }}</span><span class="hero-lbl">评论总数</span></div>
              <div class="hero-stat sep"></div>
              <div class="hero-stat"><span class="hero-num hero-grn">{{ anim.pos }}</span><span class="hero-lbl">正面</span></div>
              <div class="hero-stat sep"></div>
              <div class="hero-stat"><span class="hero-num hero-red">{{ anim.neg }}</span><span class="hero-lbl">负面</span></div>
            </div>
          </div>
        </div>

        <div class="content">
          <!-- KPI -->
          <div class="kpi-row">
            <div class="kpi-card"><div class="kpi-ico kpi-blue"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 12h2m0 0h2m-2 0v2m0-2V9"/><path d="M5 3h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2z"/></svg></div><div class="kpi-body"><span class="kpi-label">平均评分</span><span class="kpi-val">3.8 <small>/ 5.0</small></span><div class="kpi-stars"><span v-for="n in 5" :key="n" class="star" :class="n <= 4 ? 'on' : ''">★</span></div></div></div>
            <div class="kpi-card"><div class="kpi-ico kpi-em"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20"/></svg></div><div class="kpi-body"><span class="kpi-label">正面率</span><span class="kpi-val kpi-text-grn">{{ posPct }}<small>%</small></span><div class="bar"><div class="bar-fill bar-grn" :style="{width: posPct+'%'}"></div></div></div></div>
            <div class="kpi-card"><div class="kpi-ico kpi-org"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div><div class="kpi-body"><span class="kpi-label">方面类别</span><span class="kpi-val">12 <small>类</small></span><span class="kpi-sub">涵盖可用性、价格、性能等</span></div></div>
            <div class="kpi-card"><div class="kpi-ico kpi-purp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></div><div class="kpi-body"><span class="kpi-label">数据来源</span><span class="kpi-val">AWARE</span><span class="kpi-sub">学术研究数据集 v2.1</span></div></div>
          </div>

          <!-- Insight -->
          <div class="insight"><div class="insight-dot"></div><div class="insight-body"><span class="insight-hl">情感快照</span><p class="insight-p">整体正面评论占比 <strong>{{ posPct }}%</strong>，其中娱乐性、美观性和整体评价类别正面率最高，而可靠性和价格类别的负面反馈较多，值得关注。</p></div></div>

          <!-- Charts -->
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">情感仪表盘</h3><p class="panel-desc">正面评论占比实时监控</p></div><span class="tag tag-live">实时</span></div><div class="panel-bd"><SentimentGauge :sentiment-filter="sf" :aspect-filter="af"/></div></div>
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">评分情感分析</h3><p class="panel-desc">各星级评论的情感分布</p></div><span class="tag">分布</span></div><div class="panel-bd"><RatingSentiment :sentiment-filter="sf" :aspect-filter="af"/></div></div>
          </div>

          <div class="banner" style="background-image:url(/img/bg-data.jpg)"><div class="banner-mask"></div><div class="banner-body"><span class="banner-hl">领域对比分析</span><p class="banner-p">从生产力工具到娱乐应用，每个领域的情感模式截然不同——数据揭示了功能价值与情感体验之间的深层关联。</p></div></div>

          <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">各领域情感对比</h3><p class="panel-desc">不同App领域的正面率与评论量对比</p></div></div><div class="panel-bd"><DomainCompare :sentiment-filter="sf" :aspect-filter="af"/></div></div>
        </div>
      </section>

      <!-- ======================== SENTIMENT ======================== -->
      <section v-if="view === 'sentiment'">
        <div class="hero hero-sm" style="background-image:url(/img/hero-charts.jpg)"><div class="hero-mask"></div><div class="hero-body"><div class="hero-tag">情感</div><h1 class="hero-h1">情感分析</h1><p class="hero-p">评分与方面的情感关联深度洞察</p></div></div>
        <div class="content">
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">情感热力图</h3><p class="panel-desc">评分 × 方面类别的情感矩阵——绿色代表正面率高</p></div></div><div class="panel-bd"><EmotionHeatmap :sentiment-filter="sf" :aspect-filter="af"/></div></div>
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">3D 气泡图</h3><p class="panel-desc">方面类别的立体对比——球体大小=评论量，颜色=正面率</p></div></div><div class="panel-bd"><BubbleChart3D :sentiment-filter="sf" :aspect-filter="af"/></div></div>
          </div>
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">评论长度关联分析</h3><p class="panel-desc">短评论倾向正面，长评论蕴含更多复杂情感</p></div></div><div class="panel-bd"><LengthAnalysisChart :sentiment-filter="sf" :aspect-filter="af"/></div></div>
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">高频词云</h3><p class="panel-desc">正负面评论中频繁出现的关键词</p></div></div><div class="panel-bd"><WordCloud :sentiment-filter="sf" :aspect-filter="af"/></div></div>
          </div>
        </div>
      </section>

      <!-- ======================== ASPECTS ======================== -->
      <section v-if="view === 'aspects'">
        <div class="hero hero-sm" style="background-image:url(/img/bg-data.jpg)"><div class="hero-mask"></div><div class="hero-body"><div class="hero-tag">挖掘</div><h1 class="hero-h1">方面挖掘</h1><p class="hero-p">评论中提及的方面类别分布与情感分析</p></div></div>
        <div class="content">
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">玫瑰图</h3><p class="panel-desc">方面类别评论量分布——花瓣越宽评论越多</p></div></div><div class="panel-bd"><RoseChart :sentiment-filter="sf" :aspect-filter="af"/></div></div>
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">热门 App 情感对比</h3><p class="panel-desc">评论量最高的应用情感表现</p></div></div><div class="panel-bd"><TopAppsChart :sentiment-filter="sf" :aspect-filter="af"/></div></div>
          </div>
        </div>
      </section>

      <!-- ======================== RANKINGS ======================== -->
      <section v-if="view === 'rankings'">
        <div class="hero hero-sm" style="background-image:url(/img/hero-analytics.jpg)"><div class="hero-mask"></div><div class="hero-body"><div class="hero-tag">排行</div><h1 class="hero-h1">App 排行</h1><p class="hero-p">应用评分排行榜与竞争分析</p></div></div>
        <div class="content">
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">评分排行榜</h3><p class="panel-desc">Top 12 应用按平均评分排名</p></div></div><div class="panel-bd"><AppRatings :sentiment-filter="sf" :aspect-filter="af"/></div></div>
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">四象限分析</h3><p class="panel-desc">评分 × 评论量矩阵——明星、潜力、问题、边缘一目了然</p></div></div><div class="panel-bd"><QuadrantScatter :sentiment-filter="sf" :aspect-filter="af"/></div></div>
          </div>
        </div>
      </section>

      <footer class="footer"><span>AppInsight v2.0 &mdash; 情感分析系统</span><span>数据来源: AWARE 数据集 &middot; 11,321 条评论</span></footer>
    </main>

    <!-- Floating filter -->
    <div class="floating-filter"><FilterBar v-model:sentimentFilter="sf" v-model:aspectFilter="af"/></div>

    <!-- Back to top -->
    <button v-if="showTop" class="top-btn" @click="window.scrollTo({top:0,behavior:'smooth'})">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 15l-6-6-6 6"/></svg>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, reactive, onMounted, onUnmounted } from 'vue'
import FilterBar from './components/FilterBar.vue'
import SentimentGauge from './components/SentimentGauge.vue'
import RatingSentiment from './components/RatingSentiment.vue'
import DomainCompare from './components/DomainCompare.vue'
import EmotionHeatmap from './components/EmotionHeatmap.vue'
import BubbleChart3D from './components/BubbleChart3D.vue'
import LengthAnalysisChart from './components/LengthAnalysisChart.vue'
import WordCloud from './components/WordCloud.vue'
import RoseChart from './components/RoseChart.vue'
import TopAppsChart from './components/TopAppsChart.vue'
import AppRatings from './components/AppRatings.vue'
import QuadrantScatter from './components/QuadrantScatter.vue'

const nav = [
  { key: 'dashboard', label: '总览', icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
  { key: 'sentiment', label: '情感', icon: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' },
  { key: 'aspects', label: '方面', icon: 'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10' },
  { key: 'rankings', label: '排行', icon: 'M9 5l7 7-7 7' }
]

const view = ref('dashboard')
const sf = ref('全部')
const af = ref('全部')
const showTop = ref(false)

const total = 11321, pos = 5310, neg = 5291
const posPct = computed(() => ((pos / total) * 100).toFixed(1))

const anim = reactive({ total: '0', pos: '0', neg: '0' })

onMounted(() => {
  const t0 = performance.now()
  function tick() {
    const p = Math.min((performance.now() - t0) / 1600, 1), e = 1 - Math.pow(1 - p, 3)
    anim.total = Math.round(e * total).toLocaleString()
    anim.pos = Math.round(e * pos).toLocaleString()
    anim.neg = Math.round(e * neg).toLocaleString()
    if (p < 1) requestAnimationFrame(tick)
  }
  requestAnimationFrame(tick)

  const onScroll = () => { showTop.value = window.scrollY > 400 }
  window.addEventListener('scroll', onScroll)
})

const win = window as any
</script>

<style>
/* === GLOBAL === */
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:#f5f5f7;color:#0f172a;-webkit-font-smoothing:antialiased}

/* === LAYOUT === */
.app-root{display:flex;min-height:100vh;position:relative}

.ambient{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.ambient-orb{position:absolute;border-radius:50%;filter:blur(100px);opacity:.25}
.ambient-orb-1{width:600px;height:600px;top:-200px;right:-100px;background:radial-gradient(circle,#2563eb,transparent 70%)}
.ambient-orb-2{width:500px;height:500px;bottom:-150px;left:-150px;background:radial-gradient(circle,#7c3aed,transparent 70%)}

/* Sidebar */
.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:rgba(255,255,255,.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-right:1px solid rgba(0,0,0,.05);display:flex;flex-direction:column;z-index:100}
.sidebar-brand{display:flex;align-items:center;gap:12px;padding:24px 20px 18px;border-bottom:1px solid rgba(0,0,0,.04)}
.brand-check{width:32px;height:32px;flex-shrink:0}
.brand-check svg{width:100%;height:100%}
.brand-text{display:flex;flex-direction:column}
.brand-name{font-size:17px;font-weight:700;letter-spacing:-.03em;line-height:1.2}
.brand-ver{font-size:10px;color:#94a3b8;font-weight:500;text-transform:uppercase;letter-spacing:.05em}
.nav{flex:1;padding:14px 10px;display:flex;flex-direction:column;gap:2px}
.nav-btn{display:flex;align-items:center;gap:10px;padding:10px 12px;border:none;background:transparent;border-radius:10px;color:#64748b;font-size:14px;font-weight:500;cursor:pointer;transition:all .15s;text-align:left;width:100%;font-family:inherit}
.nav-btn:hover{background:rgba(37,99,235,.06);color:#0f172a}
.nav-btn.active{background:rgba(37,99,235,.1);color:#2563eb;font-weight:600}
.nav-icon{width:18px;height:18px;flex-shrink:0}
.sidebar-foot{padding:14px 20px;border-top:1px solid rgba(0,0,0,.04)}
.sf-label{font-size:10px;text-transform:uppercase;letter-spacing:.06em;color:#94a3b8;font-weight:600;margin-bottom:2px}
.sf-value{font-size:12px;color:#475569;font-weight:500}

/* Main */
.main{flex:1;margin-left:220px;min-height:100vh;position:relative;z-index:1}

/* Hero */
.hero{position:relative;background-size:cover;background-position:center;display:flex;align-items:flex-end;overflow:hidden;min-height:340px}
.hero-sm{min-height:200px}
.hero-mask{position:absolute;inset:0;background:linear-gradient(135deg,rgba(15,23,42,.75),rgba(15,23,42,.2))}
.hero-body{position:relative;z-index:2;padding:48px 40px;max-width:800px}
.hero-tag{display:inline-block;padding:4px 10px;margin-bottom:14px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.15);border-radius:6px;font-size:10px;font-weight:600;color:#fff;text-transform:uppercase;letter-spacing:.06em}
.hero-h1{font-size:38px;font-weight:700;color:#fff;line-height:1.1;letter-spacing:-.03em;margin-bottom:8px}
.hero-p{font-size:15px;color:rgba(255,255,255,.65);font-weight:400;margin-bottom:28px;max-width:580px}
.hero-stats{display:flex;gap:28px;align-items:center}
.hero-stat .hero-num{font-size:30px;font-weight:700;color:#fff;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.hero-grn{color:#4ade80}
.hero-red{color:#f87171}
.hero-lbl{display:block;font-size:11px;color:rgba(255,255,255,.45);font-weight:500;margin-top:2px}
.sep{width:1px;height:36px;background:rgba(255,255,255,.12)}

/* Content */
.content{padding:28px 40px 48px;display:flex;flex-direction:column;gap:24px}

/* KPI */
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.kpi-card{display:flex;gap:14px;background:#fff;border-radius:14px;padding:20px;border:1px solid rgba(0,0,0,.05);transition:all .2s}
.kpi-card:hover{border-color:rgba(0,0,0,.08);box-shadow:0 4px 24px rgba(0,0,0,.04);transform:translateY(-2px)}
.kpi-ico{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.kpi-ico svg{width:22px;height:22px}
.kpi-blue{background:rgba(37,99,235,.1);color:#2563eb}
.kpi-em{background:rgba(74,222,128,.12);color:#16a34a}
.kpi-org{background:rgba(251,146,60,.12);color:#ea580c}
.kpi-purp{background:rgba(124,58,237,.1);color:#7c3aed}
.kpi-body{flex:1;min-width:0}
.kpi-label{font-size:11px;color:#94a3b8;font-weight:500;display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:.04em}
.kpi-val{font-size:26px;font-weight:700;color:#0f172a;line-height:1.1;letter-spacing:-.02em;font-variant-numeric:tabular-nums;display:block}
.kpi-val small{font-size:14px;font-weight:500;color:#94a3b8}
.kpi-text-grn{color:#16a34a}
.kpi-sub{font-size:11px;color:#94a3b8;margin-top:6px;display:block}
.kpi-stars{display:flex;gap:2px;margin-top:6px}
.star{font-size:15px;color:#e2e8f0}
.star.on{color:#f59e0b}
.bar{width:100%;height:4px;background:#f1f5f9;border-radius:2px;margin-top:8px;overflow:hidden}
.bar-fill{height:100%;border-radius:2px;transition:width 1.2s ease}
.bar-grn{background:#16a34a}

/* Insight */
.insight{display:flex;gap:14px;align-items:flex-start;background:rgba(37,99,235,.03);border:1px solid rgba(37,99,235,.1);border-radius:12px;padding:18px 22px}
.insight-dot{width:8px;height:8px;border-radius:50%;background:#2563eb;margin-top:5px;flex-shrink:0;box-shadow:0 0 8px rgba(37,99,235,.3)}
.insight-hl{font-size:11px;font-weight:600;color:#2563eb;text-transform:uppercase;letter-spacing:.04em;display:block;margin-bottom:4px}
.insight-p{font-size:14px;color:#475569;line-height:1.6;margin:0}
.insight-p strong{color:#0f172a}

/* Banner */
.banner{position:relative;background-size:cover;background-position:center;border-radius:14px;overflow:hidden;min-height:100px}
.banner-mask{position:absolute;inset:0;background:linear-gradient(135deg,rgba(15,23,42,.8),rgba(15,23,42,.4))}
.banner-body{position:relative;z-index:2;padding:28px 32px}
.ban