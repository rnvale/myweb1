<template>
  <div class="app-shell">

    <!-- ====== SIDEBAR ====== -->
    <aside class="sidebar">
      <div class="sidebar-brand">
        <div class="brand-mark">
          <svg viewBox="0 0 32 32" fill="none">
            <rect x="2" y="2" width="28" height="28" rx="8" fill="currentColor"/>
            <path d="M10 16l4 4 8-8" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="brand-text">
          <span class="brand-name">AppInsight</span>
          <span class="brand-ver">v2.0</span>
        </div>
      </div>

      <nav class="nav-list">
        <button
          v-for="item in navItems"
          :key="item.id"
          class="nav-btn"
          :class="{ active: activeView === item.id }"
          @click="activeView = item.id"
        >
          <svg class="nav-btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path :d="item.icon"/></svg>
          <span>{{ item.label }}</span>
        </button>
      </nav>

      <div class="sidebar-foot">
        <div class="side-info">
          <span class="side-info-label">Dataset</span>
          <span class="side-info-value">AWARE &middot; 11.3k</span>
        </div>
      </div>
    </aside>

    <!-- ====== MAIN ====== -->
    <main class="main-area">

      <!-- ===================== DASHBOARD ===================== -->
      <section v-if="activeView === 'dashboard'" class="page">

        <!-- Hero -->
        <div class="hero hero-lg" style="background-image: url(/img/hero-analytics.jpg);">
          <div class="hero-curtain"></div>
          <div class="hero-body">
            <div class="hero-tag">Overview</div>
            <h1 class="hero-h1">App Intelligence Dashboard</h1>
            <p class="hero-p">Real-time sentiment analysis across 11,321 app store reviews from the AWARE dataset.</p>
            <div class="hero-statbar">
              <div class="hero-stat">
                <span class="hero-stat-num">{{ anim.total }}</span>
                <span class="hero-stat-lbl">Reviews</span>
              </div>
              <div class="hero-stat">
                <span class="hero-stat-num hero-stat-green">{{ anim.pos }}</span>
                <span class="hero-stat-lbl">Positive</span>
              </div>
              <div class="hero-stat">
                <span class="hero-stat-num hero-stat-red">{{ anim.neg }}</span>
                <span class="hero-stat-lbl">Negative</span>
              </div>
            </div>
          </div>
        </div>

        <div class="page-content">

          <!-- KPI with progress -->
          <div class="kpi-strip">
            <div class="kpi-tile">
              <div class="kpi-tile-icon blue-glow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 12h2m0 0h2m-2 0v2m0-2V9"/><path d="M5 3h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2z"/></svg>
              </div>
              <div class="kpi-tile-body">
                <span class="kpi-tile-lbl">Average Rating</span>
                <span class="kpi-tile-val">{{ avgRating }} <small>/ 5.0</small></span>
                <div class="kpi-tile-stars">
                  <span v-for="n in 5" :key="n" class="star-i" :class="n <= Math.round(avgRating) ? 'star-on' : 'star-off'">☆</span>
                </div>
              </div>
            </div>
            <div class="kpi-tile">
              <div class="kpi-tile-icon green-glow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20"/></svg>
              </div>
              <div class="kpi-tile-body">
                <span class="kpi-tile-lbl">Positive Rate</span>
                <span class="kpi-tile-val kpi-tile-green">{{ posPct }}<small>%</small></span>
                <div class="mini-bar"><div class="mini-bar-fill green-fill" :style="{ width: posPct + '%' }"></div></div>
              </div>
            </div>
            <div class="kpi-tile">
              <div class="kpi-tile-icon orange-glow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
              </div>
              <div class="kpi-tile-body">
                <span class="kpi-tile-lbl">Categories</span>
                <span class="kpi-tile-val">12</span>
                <span class="kpi-tile-sub">Aspect categories</span>
              </div>
            </div>
            <div class="kpi-tile">
              <div class="kpi-tile-icon purple-glow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </div>
              <div class="kpi-tile-body">
                <span class="kpi-tile-lbl">Data Source</span>
                <span class="kpi-tile-val">AWARE</span>
                <span class="kpi-tile-sub">v2.1 dataset</span>
              </div>
            </div>
          </div>

          <!-- Insight callout -->
          <div class="insight-callout">
            <div class="insight-dot"></div>
            <div class="insight-body">
              <span class="insight-label">Sentiment Snapshot</span>
              <p class="insight-text">Across all categories, <strong>{{ posPct }}%</strong> of reviews express positive sentiment. The highest-rated categories are usability and aesthetics, while pricing and compatibility show mixed patterns.</p>
            </div>
          </div>

          <!-- Chart row 1 -->
          <div class="grid-2col">
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Sentiment Gauge</h3>
                  <p class="viz-desc">Overall positive-to-negative ratio across all reviews</p>
                </div>
                <span class="viz-badge live-badge">Live</span>
              </div>
              <div class="viz-body" style="padding:0 12px;">
                <SentimentGauge :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Rating & Sentiment</h3>
                  <p class="viz-desc">Stacked bar chart showing sentiment per star rating</p>
                </div>
                <span class="viz-badge">Distribution</span>
              </div>
              <div class="viz-body">
                <RatingSentiment :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
          </div>

          <!-- Insight callout 2 with bg image -->
          <div class="insight-wide" style="background-image: url(/img/bg-data.jpg);">
            <div class="insight-wide-curtain"></div>
            <div class="insight-wide-body">
              <span class="insight-wide-hl">Domain Comparison</span>
              <p class="insight-wide-p">Explore how sentiment varies across different app domains — from productivity tools to entertainment apps. The data reveals distinct emotional patterns tied to each domain's core use case.</p>
            </div>
          </div>

          <!-- Chart row full -->
          <div class="viz-card">
            <div class="viz-head">
              <div>
                <h3 class="viz-title">Domain Comparison</h3>
                <p class="viz-desc">Cross-domain sentiment and positive rate analysis</p>
              </div>
            </div>
            <div class="viz-body">
              <DomainCompare :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>
          </div>

        </div>
      </section>

      <!-- ===================== SENTIMENT ===================== -->
      <section v-if="activeView === 'sentiment'" class="page">
        <div class="hero hero-sm" style="background-image: url(/img/hero-charts.jpg);">
          <div class="hero-curtain"></div>
          <div class="hero-body">
            <div class="hero-tag">Sentiment</div>
            <h1 class="hero-h1">Sentiment Analysis</h1>
            <p class="hero-p">Deep dive into emotional patterns across ratings and categories</p>
          </div>
        </div>
        <div class="page-content">
          <div class="grid-2col">
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Emotion Heatmap</h3>
                  <p class="viz-desc">Rating vs category sentiment matrix — higher is better</p>
                </div>
              </div>
              <div class="viz-body">
                <EmotionHeatmap :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">3D Aspect Comparison</h3>
                  <p class="viz-desc">Multi-dimensional bubble chart — size = volume, color = sentiment</p>
                </div>
              </div>
              <div class="viz-body">
                <BubbleChart3D :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
          </div>
          <div class="grid-2col">
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Review Length Correlation</h3>
                  <p class="viz-desc">Does review length relate to sentiment? Short reviews trend positive, long ones reveal nuance.</p>
                </div>
              </div>
              <div class="viz-body">
                <LengthAnalysisChart :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Word Cloud</h3>
                  <p class="viz-desc">Most frequent terms in positive vs negative reviews</p>
                </div>
              </div>
              <div class="viz-body">
                <WordCloud :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== ASPECTS ===================== -->
      <section v-if="activeView === 'aspects'" class="page">
        <div class="hero hero-sm" style="background-image: url(/img/bg-data.jpg);">
          <div class="hero-curtain"></div>
          <div class="hero-body">
            <div class="hero-tag">Aspects</div>
            <h1 class="hero-h1">Aspect Category Mining</h1>
            <p class="hero-p">Category-level distribution and sentiment breakdown</p>
          </div>
        </div>
        <div class="page-content">
          <div class="grid-2col">
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Aspect Rose Chart</h3>
                  <p class="viz-desc">Category volume distribution — wider petals = more reviews</p>
                </div>
              </div>
              <div class="viz-body">
                <RoseChart :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Top Apps Sentiment</h3>
                  <p class="viz-desc">Sentiment breakdown for the most-reviewed applications</p>
                </div>
              </div>
              <div class="viz-body">
                <TopAppsChart :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== RANKINGS ===================== -->
      <section v-if="activeView === 'rankings'" class="page">
        <div class="hero hero-sm" style="background-image: url(/img/hero-analytics.jpg);">
          <div class="hero-curtain"></div>
          <div class="hero-body">
            <div class="hero-tag">Rankings</div>
            <h1 class="hero-h1">App Rankings</h1>
            <p class="hero-p">Leaderboard and competitive analysis</p>
          </div>
        </div>
        <div class="page-content">
          <div class="grid-2col">
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Rating Leaderboard</h3>
                  <p class="viz-desc">Top 12 apps ranked by average user rating</p>
                </div>
              </div>
              <div class="viz-body">
                <AppRatings :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
            <div class="viz-card">
              <div class="viz-head">
                <div>
                  <h3 class="viz-title">Quadrant Analysis</h3>
                  <p class="viz-desc">Rating vs volume — identifies stars, potentials, and risks</p>
                </div>
              </div>
              <div class="viz-body">
                <QuadrantScatter :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="app-footer">
        <span>AppInsight v2.0 &mdash; Sentiment Analysis System</span>
        <span class="footer-right">Data: AWARE Dataset &middot; 11,321 reviews</span>
      </footer>
    </main>

    <!-- Floating filter -->
    <div class="filter-float">
      <FilterBar v-model:sentimentFilter="sentimentFilter" v-model:aspectFilter="aspectFilter" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, reactive, onMounted } from 'vue'
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

const navItems = [
  { id: 'dashboard', label: 'Dashboard', icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
  { id: 'sentiment', label: 'Sentiment', icon: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' },
  { id: 'aspects', label: 'Aspects', icon: 'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10' },
  { id: 'rankings', label: 'Rankings', icon: 'M9 5l7 7-7 7' }
]

const activeView = ref('dashboard')
const sentimentFilter = ref('全部')
const aspectFilter = ref('全部')

const totalReviews = 11321
const positiveCount = 5310
const negativeCount = 5291
const avgRating = 3.8

const posPct = computed(() => ((positiveCount / totalReviews) * 100).toFixed(1))
const negPct = computed(() => ((negativeCount / totalReviews) * 100).toFixed(1))

const anim = reactive({ total: '0', pos: '0', neg: '0' })

onMounted(() => {
  const dur = 1600
  const t0 = performance.now()

  function tick() {
    const p = Math.min((performance.now() - t0) / dur, 1)
    const e = 1 - Math.pow(1 - p, 3)
    anim.total = Math.round(e * totalReviews).toLocaleString()
    anim.pos = Math.round(e * positiveCount).toLocaleString()
    anim.neg = Math.round(e * negativeCount).toLocaleString()
    if (p < 1) requestAnimationFrame(tick)
  }
  requestAnimationFrame(tick)
})
</script>

<style scoped>
/* ====== BASE ====== */
.app-shell {
  display: flex;
  min-height: 100vh;
  background: #f5f5f7;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #0f172a;
}

/* ====== SIDEBAR ====== */
.sidebar {
  position: fixed; left: 0; top: 0; bottom: 0;
  width: 220px;
  background: rgba(255,255,255,0.88);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border-right: 1px solid rgba(0,0,0,0.05);
  display: flex; flex-direction: column; z-index: 100;
}
.sidebar-brand {
  display: flex; align-items: center; gap: 12px;
  padding: 22px 20px 18px;
  border-bottom: 1px solid rgba(0,0,0,0.04);
}
.brand-mark {
  width: 32px; height: 32px; color: #0066FF; flex-shrink: 0;
}
.brand-mark svg { width: 100%; height: 100%; }
.brand-text { display: flex; flex-direction: column; gap: 1px; }
.brand-name { font-size: 17px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.2; }
.brand-ver { font-size: 10px; color: #94a3b8; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; }

.nav-list {
  flex: 1; padding: 14px 10px; display: flex; flex-direction: column; gap: 3px;
}
.nav-btn {
  display: flex; align-items: center; gap: 10px;
  padding: 9px 12px; border: none; background: transparent; border-radius: 10px;
  color: #64748b; font-size: 14px; font-weight: 500; cursor: pointer;
  transition: all 0.15s ease; text-align: left; width: 100%; font-family: inherit;
}
.nav-btn:hover { background: rgba(0,102,255,0.06); color: #0f172a; }
.nav-btn.active { background: rgba(0,102,255,0.1); color: #0066FF; font-weight: 600; }
.nav-btn-icon { width: 18px; height: 18px; flex-shrink: 0; }

.sidebar-foot { padding: 14px 20px; border-top: 1px solid rgba(0,0,0,0.04); }
.side-info { display: flex; flex-direction: column; gap: 1px; }
.side-info-label { font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; color: #94a3b8; font-weight: 600; }
.side-info-value { font-size: 12px; color: #475569; font-weight: 500; }

/* ====== MAIN ====== */
.main-area { flex: 1; margin-left: 220px; min-height: 100vh; }

/* ====== HERO ====== */
.hero {
  position: relative; background-size: cover; background-position: center;
  display: flex; align-items: flex-end; overflow: hidden;
}
.hero-lg { min-height: 340px; }
.hero-sm { min-height: 200px; }
.hero-curtain {
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(15,23,42,0.75) 0%, rgba(15,23,42,0.25) 100%);
}
.hero-body { position: relative; z-index: 2; padding: 48px 40px; max-width: 800px; }
.hero-tag {
  display: inline-block; padding: 3px 10px; margin-bottom: 14px;
  background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.15);
  border-radius: 6px; font-size: 10px; font-weight: 600; color: white;
  text-transform: uppercase; letter-spacing: 0.06em;
}
.hero-h1 { font-size: 38px; font-weight: 700; color: white; line-height: 1.1; letter-spacing: -0.03em; margin-bottom: 8px; }
.hero-p { font-size: 15px; color: rgba(255,255,255,0.65); font-weight: 400; margin-bottom: 28px; max-width: 580px; }
.hero-statbar { display: flex; gap: 32px; }
.hero-stat-num { font-size: 30px; font-weight: 700; color: white; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; }
.hero-stat-green { color: #4ADE80; }
.hero-stat-red { color: #F87171; }
.hero-stat-lbl { display: block; font-size: 11px; color: rgba(255,255,255,0.45); font-weight: 500; margin-top: 2px; }

/* ====== PAGE CONTENT ====== */
.page-content { padding: 32px 40px 48px; display: flex; flex-direction: column; gap: 28px; }

/* ====== KPI STRIP ====== */
.kpi-strip { display: grid; grid-template-columns: repeat(4,1fr); gap: 16px; }
.kpi-tile {
  display: flex; gap: 14px; background: white; border-radius: 14px;
  padding: 20px; border: 1px solid rgba(0,0,0,0.05);
  transition: all 0.2s ease;
}
.kpi-tile:hover { border-color: rgba(0,0,0,0.08); box-shadow: 0 4px 24px rgba(0,0,0,0.04); transform: translateY(-2px); }
.kpi-tile-icon {
  width: 44px; height: 44px; border-radius: 12px;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.kpi-tile-icon svg { width: 22px; height: 22px; }
.blue-glow { background: rgba(0,102,255,0.1); color: #0066FF; }
.green-glow { background: rgba(74,222,128,0.12); color: #16A34A; }
.orange-glow { background: rgba(251,146,60,0.12); color: #EA580C; }
.purple-glow { background: rgba(124,58,237,0.1); color: #7C3AED; }
.kpi-tile-body { flex:1; min-width:0; }
.kpi-tile-lbl { font-size: 11px; color: #94a3b8; font-weight: 500; display: block; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.04em; }
.kpi-tile-val { font-size: 26px; font-weight: 700; color: #0f172a; line-height: 1.1; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; display: block; }
.kpi-tile-val small { font-size: 14px; font-weight: 500; color: #94a3b8; }
.kpi-tile-green { color: #16A34A; }
.kpi-tile-sub { font-size: 11px; color: #94a3b8; margin-top: 6px; display: block; }
.kpi-tile-stars { display: flex; gap: 2px; margin-top: 6px; }
.star-i { font-size: 16px; transition: color 0.2s; }
.star-on { color: #F59E0B; }
.star-off { color: #e2e8f0; }
.mini-bar { width: 100%; height: 4px; background: #f1f5f9; border-radius: 2px; margin-top: 8px; overflow: hidden; }
.mini-bar-fill { height: 100%; border-radius: 2px; transition: width 1.2s ease; }
.green-fill { background: #16A34A; }

/* ====== INSIGHT ====== */
.insight-callout {
  display: flex; align-items: flex-start; gap: 14px;
  background: rgba(0,102,255,0.03); border: 1px solid rgba(0,102,255,0.1);
  border-radius: 12px; padding: 18px 22px;
}
.insight-dot { width: 8px; height: 8px; border-radius: 50%; background: #0066FF; margin-top: 5px; flex-shrink: 0; }
.insight-label { font-size: 11px; font-weight: 600; color: #0066FF; text-transform: uppercase; letter-spacing: 0.04em; display: block; margin-bottom: 4px; }
.insight-text { font-size: 14px; color: #475569; line-height: 1.6; margin: 0; }
.insight-text strong { color: #0f172a; }

/* Large insight with bg */
.insight-wide {
  position: relative; background-size: cover; background-position: center;
  border-radius: 14px; overflow: hidden; min-height: 120px;
}
.insight-wide-curtain {
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(15,23,42,0.8) 0%, rgba(15,23,42,0.4) 100%);
}
.insight-wide-body { position: relative; z-index: 2; padding: 28px 32px; }
.insight-wide-hl { font-size: 15px; font-weight: 700; color: white; display: block; margin-bottom: 6px; }
.insight-wide-p { font-size: 14px; color: rgba(255,255,255,0.7); line-height: 1.5; margin: 0; max-width: 600px; }

/* ====== VIZ CARDS ====== */
.grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.viz-card {
  background: white; border: 1px solid rgba(0,0,0,0.05); border-radius: 14px;
  overflow: hidden; transition: all 0.2s ease;
}
.viz-card:hover { border-color: rgba(0,0,0,0.08); box-shadow: 0 4px 24px rgba(0,0,0,0.04); }
.viz-head {
  display: flex; justify-content: space-between; align-items: flex-start;
  padding: 20px 24px 0;
}
.viz-title { font-size: 15px; font-weight: 600; color: #0f172a; margin: 0; }
.viz-desc { font-size: 12px; color: #94a3b8; margin: 3px 0 0; line-height: 1.5; }
.viz-badge { font-size: 10px; font-weight: 600; color: #64748b; background: #f1f5f9; padding: 3px 10px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.04em; white-space: nowrap; }
.live-badge { color: #16A34A; background: rgba(74,222,128,0.12); }
.viz-body { padding: 8px 0; }

/* ====== FOOTER ====== */
.app-footer {
  display: flex; justify-content: space-between; align-items: center;
  padding: 18px 40px; border-top: 1px solid rgba(0,0,0,0.05);
  font-size: 12px; color: #94a3b8;
}

/* ====== FILTER ====== */
.filter-float {
  position: fixed; top: 20px; right: 32px; z-index: 200; max-width: 440px;
}

/* ====== RESPONSIVE ====== */
@media (max-width: 1100px) {
  .kpi-strip { grid-template-columns: repeat(2,1fr); }
  .grid-2col { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
  .sidebar { display: none; }
  .main-area { margin-left: 0; }
  .kpi-strip { grid-template-columns: 1fr; }
  .hero-h1 { font-size: 26px; }
  .hero-statbar { flex-direction: column; gap: 12px; }
  .page-content { padding: 20px; gap: 20px; }
  .hero-body { padding: 32px 24px; }
  .filter-float { right: 16px; left: 16px; max-width: none; }
}
</style>
