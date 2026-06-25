<template>
  <div class="app-root">
    <div class="ambient"><div class="ambient-orb ambient-orb-1"><div class="ambient-orb ambient-orb-2">
    <aside class="sidebar">
      <div class="sidebar-brand">
        <div class="brand-check"><svg viewBox="0 0 32 32" fill="none"><rect x="2" y="2" width="28" height="28" rx="8" fill="#2563eb"/><path d="M10 16l4 4 8-8" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <div class="brand-text"><span class="brand-name">AppInsight<span class="brand-ver">v2.0
      
      <nav class="nav">
        <button v-for="item in nav" :key="item.key" class="nav-btn" :class="{active: view === item.key}" @click="view = item.key">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path :d="item.icon"/>
          <span>{{ item.label }}
        
      
      <div class="sidebar-foot"><div class="sf-label"><div class="sf-value">AWARE  11,321 
    
    <main class="main">
      <section v-if="view === 'dashboard'">
        <div class="hero" style="background-image:url(/img/hero-analytics.jpg)"><div class="hero-mask"><div class="hero-body"><div class="hero-tag"><h1 class="hero-h1">App <p class="hero-p"> AWARE  11,321 <div class="hero-stats"><div class="hero-stat"><span class="hero-num">{{ anim.total }}<span class="hero-lbl"><div class="hero-stat sep"><div class="hero-stat"><span class="hero-num hero-grn">{{ anim.pos }}<span class="hero-lbl"><div class="hero-stat sep"><div class="hero-stat"><span class="hero-num hero-red">{{ anim.neg }}<span class="hero-lbl">
        <div class="content">
          <div class="kpi-row">
            <div class="kpi-card"><div class="kpi-ico kpi-blue"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 12h2m0 0h2m-2 0v2m0-2V9"/><path d="M5 3h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2z"/><div class="kpi-body"><span class="kpi-label"><span class="kpi-val">3.8 <small>/ 5.0<div class="kpi-stars"><span v-for="n in 5" :key="n" class="star" :class="n <= 4 ? 'on' : ''">
            <div class="kpi-card"><div class="kpi-ico kpi-em"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20"/><div class="kpi-body"><span class="kpi-label"><span class="kpi-val kpi-text-grn">{{ posPct }}<small>%<div class="bar"><div class="bar-fill bar-grn" :style="{width: posPct+'%'}">
            <div class="kpi-card"><div class="kpi-ico kpi-org"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/><div class="kpi-body"><span class="kpi-label"><span class="kpi-val">12 <small><span class="kpi-sub">
            <div class="kpi-card"><div class="kpi-ico kpi-purp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/><div class="kpi-body"><span class="kpi-label"><span class="kpi-val">AWARE<span class="kpi-sub"> v2.1
          
          <div class="insight"><div class="insight-dot"><div class="insight-body"><span class="insight-hl"><p class="insight-p"> <strong>{{ posPct }}%
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc"><span class="tag tag-live"><div class="panel-bd">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc"><span class="tag"><div class="panel-bd">
          
          <div class="banner" style="background-image:url(/img/bg-data.jpg)"><div class="banner-mask"><div class="banner-body"><span class="banner-hl"><p class="banner-p">
          <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc">App<div class="panel-bd">
        
      
      <section v-if="view === 'sentiment'">
        <div class="hero hero-sm" style="background-image:url(/img/hero-charts.jpg)"><div class="hero-mask"><div class="hero-body"><div class="hero-tag"><h1 class="hero-h1"><p class="hero-p">
        <div class="content">
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc">  <div class="panel-bd">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title">3D <p class="panel-desc">==<div class="panel-bd">
          
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc"><div class="panel-bd">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc"><div class="panel-bd">
          
        
      
      <section v-if="view === 'aspects'">
        <div class="hero hero-sm" style="background-image:url(/img/bg-data.jpg)"><div class="hero-mask"><div class="hero-body"><div class="hero-tag"><h1 class="hero-h1"><p class="hero-p">
        <div class="content">
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc"><div class="panel-bd">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"> App <p class="panel-desc"><div class="panel-bd">
          
        
      
      <section v-if="view === 'rankings'">
        <div class="hero hero-sm" style="background-image:url(/img/hero-analytics.jpg)"><div class="hero-mask"><div class="hero-body"><div class="hero-tag"><h1 class="hero-h1">App <p class="hero-p">
        <div class="content">
          <div class="grid-2">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc">Top 12 <div class="panel-bd">
            <div class="panel"><div class="panel-hd"><div><h3 class="panel-title"><p class="panel-desc">  <div class="panel-bd">
          
        
      
      <footer class="footer"><span>AppInsight v2.0<span>AWARE  11,321 
    
    <div class="floating-filter">
    <button v-if="showTop" class="top-btn" @click="window.scrollTo({top:0,behavior:'smooth'})"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 15l-6-6-6 6"/>
  


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

const nav = [
  { key: 'dashboard', label: '', icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
  { key: 'sentiment', label: '', icon: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' },
  { key: 'aspects', label: '', icon: 'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10' },
  { key: 'rankings', label: '', icon: 'M9 5l7 7-7 7' }
]

const view = ref('dashboard')
const sf = ref('')
const af = ref('')
const showTop = ref(false)
const total = 11321
const pos = 5310
const neg = 5291
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
  window.addEventListener('scroll', () => { showTop.value = window.scrollY > 400 })
})


<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:Inter,-apple-system,BlinkMacSystemFont,sans-serif;background:#f5f5f7;color:#0f172a;-webkit-font-smoothing:antialiased}
.app-root{display:flex;min-height:100vh;position:relative}
.ambient{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.ambient-orb{position:absolute;border-radius:50%;filter:blur(100px);opacity:.25}
.ambient-orb-1{width:600px;height:600px;top:-200px;right:-100px;background:radial-gradient(circle,#2563eb,transparent 70%)}
.ambient-orb-2{width:500px;height:500px;bottom:-150px;left:-150px;background:radial-gradient(circle,#7c3aed,transparent 70%)}
.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:rgba(255,255,255,.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-right:1px solid rgba(0,0,0,.05);display:flex;flex-direction:column;z-index:100}
.sidebar-brand{display:flex;align-items:center;gap:12px;padding:24px 20px 18px;border-bottom:1px solid rgba(0,0,0,.04)}
.brand-check{width:32px;height:32px;flex-shrink:0}
.brand-check svg{width:100%;height:100%}
.brand-text{display:flex;flex-direction:column;gap:1px}
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
.main{flex:1;margin-left:220px;min-height:100vh;position:relative;z-index:1}
.hero{position:relative;background-size:cover;background-position:center;display:flex;align-items:flex-end;overflow:hidden;min-height:340px}
.hero-sm{min-height:200px}
.hero-mask{position:absolute;inset:0;background:linear-gradient(135deg,rgba(15,23,42,.75),rgba(15,23,42,.2))}
.hero-body{position:relative;z-index:2;padding:48px 40px;max-width:800px}
.hero-tag{display:inline-block;padding:4px 10px;margin-bottom:14px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.15);border-radius:6px;font-size:10px;font-weight:600;color:#fff;text-transform:uppercase;letter-spacing:.06em}
.hero-h1{font-size:38px;font-weight:700;color:#fff;line-height:1.1;letter-spacing:-.03em;margin-bottom:8px}
.hero-p{font-size:15px;color:rgba(255,255,255,.65);margin-bottom:28px;max-width:580px}
.hero-stats{display:flex;gap:28px;align-items:center}
.hero-stat .hero-num{font-size:30px;font-weight:700;color:#fff;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.hero-grn{color:#4ade80}
.hero-red{color:#f87171}
.hero-lbl{display:block;font-size:11px;color:rgba(255,255,255,.45);font-weight:500;margin-top:2px}
.sep{width:1px;height:36px;background:rgba(255,255,255,.12)}
.content{padding:28px 40px 48px;display:flex;flex-direction:column;gap:24px}
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
.insight{display:flex;gap:14px;align-items:flex-start;background:rgba(37,99,235,.03);border:1px solid rgba(37,99,235,.1);border-radius:12px;padding:18px 22px}
.insight-dot{width:8px;height:8px;border-radius:50%;background:#2563eb;margin-top:5px;flex-shrink:0;box-shadow:0 0 8px rgba(37,99,235,.3)}
.insight-hl{font-size:11px;font-weight:600;color:#2563eb;text-transform:uppercase;letter-spacing:.04em;display:block;margin-bottom:4px}
.insight-p{font-size:14px;color:#475569;line-height:1.6;margin:0;font-weight:400}
.insight-p strong{color:#0f172a}
.banner{position:relative;background-size:cover;background-position:center;border-radius:14px;overflow:hidden;min-height:100px}
.banner-mask{position:absolute;inset:0;background:linear-gradient(135deg,rgba(15,23,42,.8),rgba(15,23,42,.4))}
.banner-body{position:relative;z-index:2;padding:28px 32px}
.banner-hl{font-size:15px;font-weight:700;color:#fff;display:block;margin-bottom:6px}
.banner-p{font-size:14px;color:rgba(255,255,255,.7);line-height:1.5;margin:0;max-width:600px}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.panel{background:#fff;border:1px solid rgba(0,0,0,.05);border-radius:14px;overflow:hidden;transition:all .2s}
.panel:hover{border-color:rgba(0,0,0,.08);box-shadow:0 4px 24px rgba(0,0,0,.04)}
.panel-hd{display:flex;justify-content:space-between;align-items:flex-start;padding:20px 24px 0}
.panel-title{font-size:15px;font-weight:600;color:#0f172a;margin:0}
.panel-desc{font-size:12px;color:#94a3b8;margin:3px 0 0;line-height:1.5}
.panel-bd{padding:8px 0}
.tag{font-size:10px;font-weight:600;color:#64748b;background:#f1f5f9;padding:3px 10px;border-radius:6px;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
.tag-live{color:#16a34a;background:rgba(74,222,128,.12)}
.footer{display:flex;justify-content:space-between;align-items:center;padding:18px 40px;border-top:1px solid rgba(0,0,0,.05);font-size:12px;color:#94a3b8}
.floating-filter{position:fixed;top:20px;right:32px;z-index:200;max-width:440px}
.top-btn{position:fixed;bottom:32px;right:32px;z-index:300;width:40px;height:40px;border-radius:50%;background:#fff;border:1px solid rgba(0,0,0,.08);box-shadow:0 4px 16px rgba(0,0,0,.08);cursor:pointer;display:flex;align-items:center;justify-content:center;color:#64748b;transition:all .15s;font-family:inherit;font-size:14px}
.top-btn:hover{background:#f8fafc;color:#2563eb;transform:translateY(-2px)}
.top-btn svg{width:18px;height:18px}
@media(max-width:1100px){.kpi-row{grid-template-columns:repeat(2,1fr)}.grid-2{grid-template-columns:1fr}}
@media(max-width:768px){.sidebar{display:none}.main{margin-left:0}.kpi-row{grid-template-columns:1fr}.hero-h1{font-size:26px}.hero-stats{flex-direction:column;gap:12px;align-items:flex-start}.sep{display:none}.content{padding:20px}.hero-body{padding:32px 24px}.floating-filter{right:16px;left:16px;max-width:none}}

