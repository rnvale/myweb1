<template>
  <div class="app">
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo">
          <svg class="logo-icon" viewBox="0 0 28 28" fill="none">
            <rect x="2" y="2" width="24" height="24" rx="6" fill="var(--accent)" fill-opacity="0.12"/>
            <path d="M8 14l3 3 5-6" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M6 10v8a2 2 0 002 2h12a2 2 0 002-2v-8a2 2 0 00-2-2H8a2 2 0 00-2 2z" stroke="var(--accent)" stroke-width="1.5" fill="var(--accent)" fill-opacity="0.08"/>
          </svg>
          <span class="logo-text">AppInsight</span>
        </div>
      </div>

      <nav class="nav">
        <router-link
          v-for="item in navItems"
          :key="item.name"
          :to="item.path"
          class="nav-item"
          :class="{ active: currentSection === item.name }"
          @click="currentSection = item.name"
        >
          <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
            <path :d="item.icon" />
          </svg>
          <span class="nav-text">{{ item.name }}</span>
        </router-link>
      </nav>

      <div class="sidebar-footer">
        <div class="footer-stats">
          <span class="footer-stat-label">数据源</span>
          <span class="footer-stat-value">AWARE 数据集</span>
        </div>
      </div>
    </aside>

    <div class="main">
      <header class="main-header">
        <FilterBar
          v-model:sentimentFilter="sentimentFilter"
          v-model:aspectFilter="aspectFilter"
        />
      </header>

      <div class="content">
        <!-- Dashboard -->
        <section v-if="currentSection === '总览仪表盘'" class="section">
          <div class="section-heading">
            <div>
              <h2 class="section-title">总览仪表盘</h2>
              <p class="section-desc">全局数据概览与核心指标</p>
            </div>
            <span class="section-badge">{{ totalComments }} 条评论</span>
          </div>

          <div class="kpi-grid">
            <div class="kpi-card">
              <div class="kpi-icon-wrap kpi-icon-blue">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9 12h2m0 0h2m-2 0v2m0-2V9m-3 12h12a2 2 0 002-2V7a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <div class="kpi-body">
                <span class="kpi-label">总评论数</span>
                <div class="kpi-value">{{ totalComments }}</div>
                <span class="kpi-desc">AWARE 数据集</span>
              </div>
            </div>

            <div class="kpi-card">
              <div class="kpi-icon-wrap kpi-icon-green">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905a3.61 3.61 0 01-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                </svg>
              </div>
              <div class="kpi-body">
                <span class="kpi-label">正面评论</span>
                <div class="kpi-value kpi-positive">{{ positiveComments }}</div>
                <span class="kpi-desc">占比 {{ positivePercentage }}%</span>
              </div>
            </div>

            <div class="kpi-card">
              <div class="kpi-icon-wrap kpi-icon-red">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M10 14H5.236a2 2 0 01-1.789-2.894l3.5-7A2 2 0 018.736 3h4.018a2 2 0 01.485.06l3.76.94m-7 10v5a2 2 0 002 2h.095c.5 0 .905-.405.905-.905a3.61 3.61 0 01.608-2.006l1.99-4A2 2 0 0014.5 10h-4.5m-3 0h2m-2 0v2" />
                </svg>
              </div>
              <div class="kpi-body">
                <span class="kpi-label">负面评论</span>
                <div class="kpi-value kpi-negative">{{ negativeComments }}</div>
                <span class="kpi-desc">占比 {{ negativePercentage }}%</span>
              </div>
            </div>

            <div class="kpi-card">
              <div class="kpi-icon-wrap kpi-icon-yellow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                </svg>
              </div>
              <div class="kpi-body">
                <span class="kpi-label">平均评分</span>
                <div class="kpi-value">{{ averageRating }}<span class="kpi-unit">/5.0</span></div>
                <div class="kpi-stars">
                  <span v-for="n in 5" :key="n" class="star" :class="{ active: n <= Math.round(averageRating) }">★</span>
                </div>
              </div>
            </div>
          </div>

          <div class="chart-grid">
            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">情感仪表盘</h3>
                <span class="chart-card-tag">实时分析</span>
              </div>
              <SentimentGauge :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>

            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">评分情感分析</h3>
                <span class="chart-card-tag">分布趋势</span>
              </div>
              <RatingSentiment :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>

            <div class="chart-card chart-card-full">
              <div class="chart-card-header">
                <h3 class="chart-card-title">领域对比</h3>
                <span class="chart-card-tag">多维度</span>
              </div>
              <DomainCompare :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>
          </div>
        </section>

        <!-- Sentiment -->
        <section v-if="currentSection === '情感分析'" class="section">
          <div class="section-heading">
            <div>
              <h2 class="section-title">情感分析</h2>
              <p class="section-desc">各应用情感表现排名与对比</p>
            </div>
          </div>

          <div class="chart-grid">
            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">评分-方面情感热力图</h3>
                <span class="chart-card-tag">关联分析</span>
              </div>
              <EmotionHeatmap :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>

            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">3D气泡图</h3>
                <span class="chart-card-tag">立体对比</span>
              </div>
              <BubbleChart3D :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>

            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">评论长度关联分析</h3>
                <span class="chart-card-tag">文本挖掘</span>
              </div>
              <LengthAnalysisChart :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>

            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">高频词云</h3>
                <span class="chart-card-tag">关键词提取</span>
              </div>
              <WordCloud :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>
          </div>
        </section>

        <!-- Aspect -->
        <section v-if="currentSection === '方面挖掘'" class="section">
          <div class="section-heading">
            <div>
              <h2 class="section-title">方面挖掘</h2>
              <p class="section-desc">评论中提及的方面类别分布与情感</p>
            </div>
          </div>

          <div class="chart-grid">
            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">玫瑰图 — 方面评论数量分布</h3>
                <span class="chart-card-tag">占比分析</span>
              </div>
              <RoseChart :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>

            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">热门App情感对比</h3>
                <span class="chart-card-tag">时间趋势</span>
              </div>
              <TopAppsChart :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>
          </div>
        </section>

        <!-- Ranking -->
        <section v-if="currentSection === 'App排行'" class="section">
          <div class="section-heading">
            <div>
              <h2 class="section-title">App排行</h2>
              <p class="section-desc">各应用情感表现排名与对比</p>
            </div>
          </div>

          <div class="chart-grid">
            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">App评分排行榜</h3>
                <span class="chart-card-tag">Top 10</span>
              </div>
              <AppRatings :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>

            <div class="chart-card">
              <div class="chart-card-header">
                <h3 class="chart-card-title">App四象限分析图</h3>
                <span class="chart-card-tag">综合评价</span>
              </div>
              <QuadrantScatter :sentiment-filter="sentimentFilter" :aspect-filter="aspectFilter" />
            </div>
          </div>
        </section>

        <footer class="footer">
          <div class="footer-left">
            <span>AppInsight 情感分析系统</span>
          </div>
          <div class="footer-right">
            <span>数据来源：AWARE 数据集</span>
            <span class="footer-dot">·</span>
            <span>{{ totalComments }} 条评论</span>
          </div>
        </footer>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
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
  { name: '总览仪表盘', path: '/', icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
  { name: '情感分析', path: '/sentiment', icon: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' },
  { name: '方面挖掘', path: '/aspect', icon: 'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10' },
  { name: 'App排行', path: '/ranking', icon: 'M9 5l7 7-7 7' }
]

const currentSection = ref('总览仪表盘')
const sentimentFilter = ref('全部')
const aspectFilter = ref('全部')

const totalComments = 11321
const positiveComments = 5310
const negativeComments = 5291
const averageRating = 3.8

const positivePercentage = computed(() => ((positiveComments / totalComments) * 100).toFixed(1))
const negativePercentage = computed(() => ((negativeComments / totalComments) * 100).toFixed(1))
</script>

<style scoped>
.app {
  display: flex;
  min-height: 100vh;
  background: var(--bg-body);
}

/* ====== Sidebar ====== */
.sidebar {
  width: var(--sidebar-width);
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  position: fixed;
  height: 100vh;
  z-index: 100;
}

.sidebar-header {
  padding: 20px 20px 16px;
  border-bottom: 1px solid var(--border-subtle);
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-icon {
  width: 28px;
  height: 28px;
  flex-shrink: 0;
}

.logo-text {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.03em;
}

.nav {
  flex: 1;
  padding: 12px 8px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: var(--radius-md);
  color: var(--text-secondary);
  text-decoration: none;
  transition: all var(--transition-fast);
  margin-bottom: 2px;
}

.nav-item:hover {
  background: var(--accent-subtle);
  color: var(--text-primary);
}

.nav-item.active {
  background: var(--accent-subtle);
  color: var(--accent);
  font-weight: 600;
}

.nav-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

.nav-text {
  font-size: 14px;
}

.sidebar-footer {
  padding: 16px 20px;
  border-top: 1px solid var(--border-subtle);
}

.footer-stats {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.footer-stat-label {
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.footer-stat-value {
  font-size: 12px;
  color: var(--text-secondary);
  font-weight: 500;
}

/* ====== Main ====== */
.main {
  flex: 1;
  margin-left: var(--sidebar-width);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-header {
  padding: 20px 32px 0;
}

.content {
  flex: 1;
  padding: 24px 32px 40px;
}

/* ====== Section ====== */
.section-heading {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 24px;
}

.section-title {
  font-size: 24px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.3;
  letter-spacing: -0.02em;
}

.section-desc {
  font-size: 14px;
  color: var(--text-muted);
  margin-top: 4px;
}

.section-badge {
  display: inline-flex;
  align-items: center;
  padding: 6px 14px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 20px;
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 500;
}

/* ====== KPI Cards ====== */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 28px;
}

.kpi-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 20px;
  transition: all var(--transition-base);
}

.kpi-card:hover {
  border-color: var(--border-default);
  box-shadow: var(--shadow-md);
}

.kpi-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.kpi-icon-wrap svg {
  width: 22px;
  height: 22px;
}

.kpi-icon-blue { background: rgba(37, 99, 235, 0.1); color: #2563eb; }
.kpi-icon-green { background: rgba(22, 163, 74, 0.1); color: #16a34a; }
.kpi-icon-red { background: rgba(220, 38, 38, 0.1); color: #dc2626; }
.kpi-icon-yellow { background: rgba(217, 119, 6, 0.1); color: #d97706; }

.kpi-body { flex: 1; min-width: 0; }

.kpi-label {
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 500;
  display: block;
  margin-bottom: 4px;
}

.kpi-value {
  font-size: 26px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.kpi-unit {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-muted);
}

.kpi-positive { color: var(--positive); }
.kpi-negative { color: var(--negative); }

.kpi-desc {
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 4px;
  display: block;
}

.kpi-stars {
  display: flex;
  gap: 2px;
  margin-top: 6px;
}

.star {
  font-size: 14px;
  color: var(--border-strong);
  transition: color var(--transition-fast);
}

.star.active {
  color: #f59e0b;
}

/* ====== Chart Grid ====== */
.chart-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.chart-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 20px;
  transition: all var(--transition-base);
}

.chart-card:hover {
  border-color: var(--border-default);
  box-shadow: var(--shadow-card-hover);
}

.chart-card-full {
  grid-column: 1 / -1;
}

.chart-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-subtle);
}

.chart-card-title {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
}

.chart-card-tag {
  font-size: 11px;
  color: var(--accent);
  background: var(--accent-subtle);
  padding: 3px 10px;
  border-radius: 12px;
  font-weight: 500;
}

/* ====== Footer ====== */
.footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 60px;
  padding-top: 20px;
  border-top: 1px solid var(--border-subtle);
  font-size: 12px;
  color: var(--text-muted);
}

.footer-right { display: flex; align-items: center; gap: 8px; }
.footer-dot { color: var(--border-default); }

@media (max-width: 1200px) {
  .kpi-grid { grid-template-columns: repeat(2, 1fr); }
  .chart-grid { grid-template-columns: 1fr; }
  .chart-card-full { grid-column: 1; }
}

@media (max-width: 768px) {
  .kpi-grid { grid-template-columns: 1fr; }
  .content { padding: 16px; }
  .main-header { padding: 16px 16px 0; }
}
</style>
