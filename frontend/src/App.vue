<template>
  <div class="app-root">
    <svg style="position:absolute;width:0;height:0" aria-hidden="true">
      <defs>
        <linearGradient id="brandGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0891b2"/>
          <stop offset="100%" stop-color="#d97706"/>
        </linearGradient>
      </defs>
    </svg>
    <!-- Sidebar -->
    <aside class="sidebar" role="navigation" aria-label="主导航">
      <div class="sidebar-header">
        <svg class="brand-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true">
          <rect x="2" y="2" width="24" height="24" rx="6" fill="url(#brandGrad)"/>
          <path d="M10 14l3 3 5-6" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <div class="brand-text">
          <span class="brand-name">AppInsight</span>
          <span class="brand-ver">v2.0</span>
        </div>
      </div>

      <div class="nav-rail">
        <div class="rail-track" aria-hidden="true">
          <div class="rail-indicator" :style="{ transform: 'translateY(' + navIndex * 48 + 'px)' }"></div>
        </div>
        <nav class="nav-list">
          <button
            v-for="(item, i) in nav"
            :key="item.key"
            class="nav-item"
            :class="{ active: view === item.key }"
            @click="view = item.key"
          >
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path :d="item.icon"/></svg>
            <span>{{ item.label }}</span>
          </button>
        </nav>
      </div>

<div class="sidebar-footer">
  <div class="sf-row">
    <span class="sf-label">数据来源</span>
    <span class="sf-value">AWARE 数据集</span>
  </div>
  <div class="sf-row">
    <span class="sf-label">记录数</span>
    <span class="sf-value">11,321 条评论</span>
  </div>

  <!-- 作者与 GitHub 链接 -->
  <div class="sf-row" style="margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.12);">
    <span class="sf-label">作者</span>
    <span class="sf-value">RainVale</span>
  </div>
  <div class="sf-row" style="align-items: center;">
    <span class="sf-label">GitHub</span>
    <a href="https://github.com/rnvale/myweb1" target="_blank" rel="noopener noreferrer"
       class="sf-value"
       style="display: inline-flex; align-items: center; gap: 4px; color: inherit; text-decoration: none; transition: opacity 0.2s;"
       onmouseover="this.style.opacity='0.7'"
       onmouseout="this.style.opacity='1'">
      <svg viewBox="0 0 24 24" fill="currentColor" style="width: 14px; height: 14px;" aria-hidden="true">
        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.385.6.113.82-.26.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.09-.745.083-.73.083-.73 1.205.085 1.84 1.237 1.84 1.237 1.07 1.835 2.807 1.305 3.492.998.108-.776.42-1.305.762-1.605-2.665-.305-5.467-1.332-5.467-5.93 0-1.31.467-2.38 1.235-3.22-.135-.303-.535-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.4 3-.405 1.02.005 2.045.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 21.795 24 17.295 24 12c0-6.63-5.37-12-12-12z"/>
      </svg>
      @rnvale/myweb1
    </a>
  </div>
</div>

    </aside>

    <!-- Main -->
    <main class="main" id="main-content">

      <!-- ==================== DASHBOARD ==================== -->
      <section v-if="view === 'dashboard'" class="page">
        <header class="page-header hero-cyan">
          <div class="hero-content">
            <div class="page-tag-group">
              <span class="tag tag-dark">概览</span>
              <span class="tag tag-dark-outline">仪表盘</span>
            </div>
            <h1 class="page-title hero-title">App 智能分析仪表盘</h1>
            <p class="page-desc hero-desc">基于 AWARE 数据集对 <strong>{{ fmt(total) }}</strong> 条应用评论进行实时情感分析</p>
            <div class="hero-stats">
              <div class="hs-item">
                <span class="hs-num">{{ anim.total }}</span>
                <span class="hs-lbl">评论总数</span>
              </div>
              <div class="hs-divider" aria-hidden="true"></div>
              <div class="hs-item">
                <span class="hs-num hs-pos">{{ anim.pos }}</span>
                <span class="hs-lbl">正面</span>
              </div>
              <div class="hs-divider" aria-hidden="true"></div>
              <div class="hs-item">
                <span class="hs-num hs-neg">{{ anim.neg }}</span>
                <span class="hs-lbl">负面</span>
              </div>
              <div class="hs-divider" aria-hidden="true"></div>
              <div class="hs-item">
                <span class="hs-num hs-accent">{{ posPct }}<small>%</small></span>
                <span class="hs-lbl">正面率</span>
              </div>
            </div>
          </div>
        </header>

        <div class="content">

          <!-- Metrics row: compact bar -->
          <div class="metrics-bar">
            <div class="mb-item">
              <span class="mb-lbl">平均评分</span>
              <span class="mb-val">3.8</span>
              <div class="mb-stars" aria-label="4 星">★★★★☆</div>
            </div>
            <div class="mb-divider"></div>
            <div class="mb-item">
              <span class="mb-lbl">正面率</span>
              <span class="mb-val mb-val-grn">{{ posPct }}<small>%</small></span>
              <div class="bar-track"><div class="bar-fill" :style="{ width: posPct + '%' }"></div></div>
            </div>
            <div class="mb-divider"></div>
            <div class="mb-item">
              <span class="mb-lbl">方面类别</span>
              <span class="mb-val">12</span>
              <span class="mb-sub">可用性·价格·性能</span>
            </div>
            <div class="mb-divider"></div>
            <div class="mb-item">
              <span class="mb-lbl">数据来源</span>
              <span class="mb-val">AWARE</span>
              <span class="mb-sub">学术研究数据集</span>
            </div>
          </div>

          <!-- Section 1: Sentiment charts -->
          <div class="grid-2">
            <div class="card">
              <div class="card-header">
                <div>
                  <h2 class="card-title">情感仪表盘</h2>
                  <p class="card-desc">正面评论占比实时监控</p>
                </div>
                <span class="tag tag-live">实时</span>
              </div>
              <div class="card-body"><SentimentGauge :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
            <div class="card">
              <div class="card-header">
                <div>
                  <h2 class="card-title">评分情感分析</h2>
                  <p class="card-desc">各星级评论的情感分布</p>
                </div>
                <span class="tag">分布</span>
              </div>
              <div class="card-body"><RatingSentiment :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
          </div>

          <!-- Magazine-style section: Domain analysis -->
          <div class="mag-section">
            <div class="mag-image">
              <img src="/img/mag-domain.jpg" alt="" loading="lazy">
            </div>
            <div class="mag-text">
              <span class="mag-label">领域分析</span>
              <h3 class="mag-title">各 App 领域情感对比</h3>
              <p class="mag-desc">娱乐性和美观性类应用正面率最高，而可靠性和价格类别的负面反馈较多。不同 App 领域的正面率与评论量呈现明显分化。</p>
              <div class="mag-stat-row">
                <div class="mag-stat">
                  <span class="mag-stat-val mag-grn">{{ posPct }}<small>%</small></span>
                  <span class="mag-stat-lbl">总体正面率</span>
                </div>
                <div class="mag-stat">
                  <span class="mag-stat-val" style="color:#d97706">12</span>
                  <span class="mag-stat-lbl">方面类别</span>
                </div>
                <div class="mag-stat">
                  <span class="mag-stat-val" style="color:#0891b2">{{ fmt(total) }}</span>
                  <span class="mag-stat-lbl">评论总数</span>
                </div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <div>
                <h2 class="card-title">各领域情感对比</h2>
                <p class="card-desc">不同 App 领域的正面率与评论量对比</p>
              </div>
            </div>
            <div class="card-body"><DomainCompare :sentiment-filter="sf" :aspect-filter="af"/></div>
          </div>

        </div>
      </section>

      <!-- ==================== SENTIMENT ==================== -->
      <section v-if="view === 'sentiment'" class="page">
        <header class="page-header page-header-sm hero-purple">
          <div class="hero-content">
            <div class="page-tag-group"><span class="tag tag-dark">情感</span></div>
            <h1 class="page-title hero-title">情感分析</h1>
            <p class="page-desc hero-desc">评分与方面的情感关联深度洞察</p>
          </div>
        </header>
        <div class="content">
          <div class="grid-2">
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">情感热力图</h2><p class="card-desc">评分与方面类别的情感矩阵</p></div></div>
              <div class="card-body"><EmotionHeatmap :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">3D 气泡图</h2><p class="card-desc">气泡大小=评论量，颜色=正面率</p></div></div>
              <div class="card-body"><BubbleChart3D :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
          </div>
          <div class="grid-2">
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">评论长度分析</h2><p class="card-desc">短评论倾向正面，长评论蕴含更多信息</p></div></div>
              <div class="card-body"><LengthAnalysisChart :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">高频词云</h2><p class="card-desc">正负面评论中频繁出现的关键词</p></div></div>
              <div class="card-body"><WordCloud :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
          </div>

          <div class="mag-section">
            <div class="mag-image">
              <img src="/img/mag-sentiment.jpg" alt="" loading="lazy">
            </div>
            <div class="mag-text">
              <span class="mag-label">情感洞察</span>
              <h3 class="mag-title">评分与情感深度关联</h3>
              <p class="mag-desc">短评论通常倾向正面，而长评论蕴含更多细节信息。高频词分析显示，正负面评论中频繁出现的关键词存在显著差异，反映出用户在不同情感状态下的关注点。</p>
              <div class="mag-stat-row">
                <div class="mag-stat">
                  <span class="mag-stat-val" style="color:#8b5cf6">正面高频</span>
                  <span class="mag-stat-lbl">好用·喜欢·推荐</span>
                </div>
                <div class="mag-stat">
                  <span class="mag-stat-val" style="color:#ef4444">负面高频</span>
                  <span class="mag-stat-lbl">闪退·卡顿·收费</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ==================== ASPECTS ==================== -->
      <section v-if="view === 'aspects'" class="page">
        <header class="page-header page-header-sm hero-emerald">
          <div class="hero-content">
            <div class="page-tag-group"><span class="tag tag-dark">挖掘</span></div>
            <h1 class="page-title hero-title">方面挖掘</h1>
            <p class="page-desc hero-desc">评论中提及的方面类别分布与情感分析</p>
          </div>
        </header>
        <div class="content">
          <div class="grid-2">
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">玫瑰图</h2><p class="card-desc">方面类别评论量分布</p></div></div>
              <div class="card-body"><RoseChart :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">热门 App 情感对比</h2><p class="card-desc">评论量最高的应用情感表现</p></div></div>
              <div class="card-body"><TopAppsChart :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
          </div>

          <div class="mag-section">
            <div class="mag-image">
              <img src="/img/mag-aspects.jpg" alt="" loading="lazy">
            </div>
            <div class="mag-text">
              <span class="mag-label">类别挖掘</span>
              <h3 class="mag-title">评论方面类别分布</h3>
              <p class="mag-desc">用户评论覆盖 12 个方面类别，涵盖可用性、价格、性能、功能、美观性等多个维度。不同类别的情感倾向差异明显，为产品改进提供精准方向。</p>
              <div class="mag-stat-row">
                <div class="mag-stat">
                  <span class="mag-stat-val" style="color:#d97706">12</span>
                  <span class="mag-stat-lbl">方面类别</span>
                </div>
                <div class="mag-stat">
                  <span class="mag-stat-val mag-grn" style="color:#16a34a">前 3</span>
                  <span class="mag-stat-lbl">可用性·功能·性能</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ==================== RANKINGS ==================== -->
      <section v-if="view === 'rankings'" class="page">
        <header class="page-header page-header-sm hero-amber">
          <div class="hero-content">
            <div class="page-tag-group"><span class="tag tag-dark">排行</span></div>
            <h1 class="page-title hero-title">App 排行</h1>
            <p class="page-desc hero-desc">应用评分排行榜与竞争分析</p>
          </div>
        </header>
        <div class="content">
          <div class="grid-2">
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">评分排行榜</h2><p class="card-desc">Top 12 应用按平均评分排名</p></div></div>
              <div class="card-body"><AppRatings :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
            <div class="card">
              <div class="card-header"><div><h2 class="card-title">四象限分析</h2><p class="card-desc">评分与评论量矩阵</p></div></div>
              <div class="card-body"><QuadrantScatter :sentiment-filter="sf" :aspect-filter="af"/></div>
            </div>
          </div>

          <div class="mag-section">
            <div class="mag-image">
              <img src="/img/mag-rankings.jpg" alt="" loading="lazy">
            </div>
            <div class="mag-text">
              <span class="mag-label">竞争格局</span>
              <h3 class="mag-title">应用评分排行与定位</h3>
              <p class="mag-desc">Top 12 应用中，评分与评论量并非简单的正相关。部分应用评论量高但评分中等，四象限分析揭示了"高评分高评论"的明星应用与"低评分高评论"的问题应用。</p>
              <div class="mag-stat-row">
                <div class="mag-stat">
                  <span class="mag-stat-val" style="color:#d97706">Top 12</span>
                  <span class="mag-stat-lbl">上榜应用</span>
                </div>
                <div class="mag-stat">
                  <span class="mag-stat-val" style="color:#16a34a">4 象限</span>
                  <span class="mag-stat-lbl">矩阵分析</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <footer class="footer">
        <span>AppInsight v2.0 情感分析系统</span>
        <span>AWARE 数据集 | 11,321 条评论</span>
      </footer>
    </main>

    <!-- Filter -->
    <div class="filter-dock"><FilterBar v-model:sentimentFilter="sf" v-model:aspectFilter="af"/></div>

    <!-- Back to top -->
    <button v-if="showTop" class="top-btn" @click="scrollToTop" aria-label="回到顶部">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M18 15l-6-6-6 6"/></svg>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, reactive, onMounted } from "vue"
import FilterBar from "./components/FilterBar.vue"
import SentimentGauge from "./components/SentimentGauge.vue"
import RatingSentiment from "./components/RatingSentiment.vue"
import DomainCompare from "./components/DomainCompare.vue"
import EmotionHeatmap from "./components/EmotionHeatmap.vue"
import BubbleChart3D from "./components/BubbleChart3D.vue"
import LengthAnalysisChart from "./components/LengthAnalysisChart.vue"
import WordCloud from "./components/WordCloud.vue"
import RoseChart from "./components/RoseChart.vue"
import TopAppsChart from "./components/TopAppsChart.vue"
import AppRatings from "./components/AppRatings.vue"
import QuadrantScatter from "./components/QuadrantScatter.vue"

const nav = [
  { key: "dashboard", label: "总览", icon: "M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" },
  { key: "sentiment", label: "情感", icon: "M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" },
  { key: "aspects", label: "方面", icon: "M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" },
  { key: "rankings", label: "排行", icon: "M9 5l7 7-7 7" },
]

const fmt = (n: number) => n.toLocaleString()

const navIndex = computed(() => {
  const idx = nav.findIndex((x) => x.key === view.value)
  return idx >= 0 ? idx : 0
})

const view = ref("dashboard")
const sf = ref("全部")
const af = ref("全部")
const showTop = ref(false)

const scrollToTop = () => window.scrollTo({ top: 0, behavior: "smooth" })

const total = ref(0)
const pos = ref(0)
const neg = ref(0)
const posPct = computed(() => (total.value > 0 ? ((pos.value / total.value) * 100).toFixed(1) : "0.0"))
const anim = reactive({ total: "0", pos: "0", neg: "0" })

onMounted(async () => {
  try {
    const { default: http } = await import("./http")
    const r = await http.post("/filtered_summary", { sentiment: "all", category: "all" })
    pos.value = r.data.sentiment?.positive ?? 0
    neg.value = r.data.sentiment?.negative ?? 0
    total.value = pos.value + neg.value
  } catch {
    pos.value = 5310; neg.value = 5291; total.value = 10601
  }

  const t0 = performance.now()
  const tick = () => {
    const p = Math.min((performance.now() - t0) / 1600, 1)
    const e = 1 - Math.pow(1 - p, 3)
    anim.total = Math.round(e * total.value).toLocaleString()
    anim.pos = Math.round(e * pos.value).toLocaleString()
    anim.neg = Math.round(e * neg.value).toLocaleString()
    if (p < 1) requestAnimationFrame(tick)
  }
  requestAnimationFrame(tick)

  const onScroll = () => { showTop.value = window.scrollY > 400 }
  window.addEventListener("scroll", onScroll)
})
</script>
