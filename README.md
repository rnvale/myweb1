# AppInsight — App 评论情感分析可视化系统

基于 AWARE 数据集的 App 评论情感分析与可视化平台，提供多维度、交互式的数据探索体验。

## 📊 项目简介

**AppInsight v2.0** 是一个完整的全栈数据可视化应用，旨在帮助产品经理和开发者快速洞察用户评论中的情感倾向和关注重点。系统采用 **四页式导航结构**，将 11 种图表按分析主题组织为「总览 → 情感 → 方面 → 排行」四大模块，配合全局筛选器实现跨页面联动分析。

> 💡 **在线体验**：[https://haolin-zone.xyz](https://haolin-zone.xyz) （已部署至公网，无需本地配置）

---

## ✨ 功能特点

### 🖥 界面设计
- **四页导航架构**：总览 / 情感 / 方面 / 排行，侧边栏切换，每页聚焦一类分析视角
- **全局筛选器**：顶部支持按情感类型（正面 / 负面 / 全部）和方面类别（12 类可选）筛选，所有图表实时联动更新
- **卡片式布局**：每个图表模块独立成卡，配有标题、说明文字和关键数据摘要
- **品牌标识**：AppInsight v2.0 统一品牌，页脚展示数据集来源与规模

### 📈 可视化能力（11 种图表）

| 页面 | 图表 | 图表类型 | 分析目标 |
|------|------|----------|----------|
| **总览** | 情感仪表盘 | 仪表盘 + 环形图 | 整体正负面比例一目了然 |
| **总览** | 评分情感分析 | 折线图 + 组合柱状图 | 各星级的正面/负面率走势 |
| **总览** | 领域雷达图 | 雷达图 | 6 大领域 App 多维对比 |
| **总览** | 热门 App 河流图 | 堆叠面积图 | Top App 的情感时序变化 |
| **情感** | 方面玫瑰图 | 南丁格尔玫瑰图 | 12 个方面类别的评论量分布 |
| **情感** | 3D 气泡图 | 3D 气泡图 | 方面类别 × 正负评论量立体对比 |
| **情感** | 评论长度分析 | 分组柱状图 + 趋势折线 | 评论长度与情感的关联 |
| **情感** | 情感热力图 | 热力图 | 评分 × 方面的情感密度矩阵 |
| **方面** | 方面类别分布 | 南丁格尔玫瑰图 | 方面类别关注度排名 |
| **方面** | 热门 App 情感对比 | 条形对比图 | 高评论量 App 的各维度表现 |
| **排行** | 评分排行榜 | 水平条形图 | Top 12 应用平均评分排名 |
| **排行** | 四象限分析 | 四象限散点图 | 评分 vs 评论量的产品定位 |

### 🔧 交互特性
- **悬停提示**：每个数据点均支持 Tooltip 查看详情
- **平滑动画**：图表渲染和数据切换时带有过渡动画
- **响应式布局**：适配桌面端浏览体验

---

## 🛠 技术栈

### 前端
| 技术 | 用途 |
|------|------|
| Vue 3 + TypeScript | 核心框架 |
| Vite | 构建工具 |
| ECharts / ECharts GL / echarts-wordcloud | 图表渲染引擎 |
| D3.js | 辅助数据处理与可视化 |
| Element Plus | UI 组件库 |
| Axios | HTTP 请求 |
| Mitt | 事件总线（跨组件通信） |

### 后端
| 技术 | 用途 |
|------|------|
| Flask | Web 框架 |
| Flask-CORS | 跨域支持 |
| Pandas | 数据处理与分析 |
| Gunicorn | 生产环境 WSGI 服务器 |

### 部署
| 平台 | 用途 |
|------|------|
| **Vercel** | 前端静态托管（自动部署） |
| **Render** | 后端 API 托管（新加坡区域） |

---

## 🌐 在线访问

**网站地址**：[https://haolin-zone.xyz](https://haolin-zone.xyz)

系统已部署至公网，前端托管于 Vercel，后端 API 托管于 Render，可直接访问使用。

---

## 💻 本地开发运行

### 前置要求

- Node.js ≥ 20
- Python ≥ 3.11
- Git

### 快速启动

```bash
# 1. 克隆项目
git clone https://github.com/YYJXX-lab/myWeb.git
cd myWeb

# 2. 启动后端
cd backend
pip install -r requirements.txt
python app.py          # 或 python render_start.py（使用 uvicorn）
# 后端服务将在 http://localhost:5000 启动

# 3. 启动前端（新终端）
cd frontend
npm install
npm run dev
# 前端服务将在 http://localhost:5173 启动
```

打开浏览器访问 `http://localhost:5173` 即可使用本地版本。

### 构建生产版本

```bash
cd frontend
npm run build
# 构建产物输出到 frontend/dist 目录
```

---

## 📁 项目结构

```
myWeb/
├── frontend/                    # Vue3 前端项目
│   ├── src/
│   │   ├── components/          # 图表组件 + 筛选器组件
│   │   │   ├── overview/        # 总览页组件（仪表盘、评分分析、雷达图、河流图）
│   │   │   ├── sentiment/       # 情感页组件（玫瑰图、3D气泡、长度分析、热力图）
│   │   │   ├── aspect/          # 方面页组件（类别分布、App对比）
│   │   │   └── ranking/         # 排行页组件（评分排行、四象限）
│   │   ├── utils/               # 中英文映射、事件总线
│   │   ├── App.vue              # 主布局（侧边栏导航 + 路由切换 + 全局筛选器）
│   │   ├── http.ts              # API 地址配置
│   │   └── main.ts              # 入口文件
│   ├── dist/                    # 构建产物
│   └── vercel.json              # Vercel 部署配置
├── backend/                     # Flask 后端项目
│   ├── app.py                   # API 接口（数据分析与聚合）
│   ├── data/                    # AWARE 数据集
│   ├── requirements.txt         # Python 依赖
│   └── render.yaml              # Render 部署配置
├── wsgi.py                      # WSGI 入口（Render 使用）
├── render_start.py              # 本地开发启动脚本（uvicorn）
├── runtime.txt                  # Python 版本指定（3.11）
└── README.md
```

---

## 📈 核心数据洞察

基于 AWARE 数据集（11,321 条标注评论）的分析结论：

1. **整体评价趋于平衡**：正面 50.1%，负面 49.9%
2. **三星用户是矛盾群体**：正面率仅 44.3%，最值得关注和挽回
3. **游戏 App 正面率最高**（52.4%），社交网络最低（44.7%）
4. **娱乐性是最大亮点**（正面率 69%），**可靠性是核心痛点**（负面率 73%）
5. **整体评价类最受关注**（约 3,000 条评论），远超其他方面类别
6. **长评论更倾向于负面表达**，用户在不满时更愿意详细阐述

---

## 📚 数据来源

| 项目 | 说明 |
|------|------|
| **数据集名称** | AWARE（App Review Analysis with Weak REcognition） |
| **访问地址** | [OpenDataLab/AWARE](https://opendatalab.com/OpenDataLab/AWARE) |
| **数据规模** | 11,321 条标注评论，12 个方面类别，5 个应用领域 |

---

## 🔧 云端部署说明

本项目采用 **前后端分离部署**方案：

### 前端（Vercel）
- 关联 GitHub 仓库，推送后自动构建部署
- `vercel.json` 配置构建命令和路由重写规则
- 构建完成后将 `frontend/dist` 静态托管

### 后端（Render）
- `render.yaml` 定义 Web Service 配置：
  - 运行时：Python（Singapore 区域）
  - 构建：`pip install -r backend/requirements.txt`
  - 启动：`gunicorn backend.app:app --workers 1 --threads 2 --timeout 120`
  - 健康检查：`/api/test`
- `wsgi.py` 作为 WSGI 入口，`render_start.py` 用于本地 uvicorn 开发

### 本地 ↔ 云端切换
- 前端 `http.ts` 中修改 API base URL 即可切换后端地址
- 后端 `app.py` 从环境变量读取端口，`host='0.0.0.0'` 适配云平台

---

## 📄 开源协议

本项目仅供学习交流使用。

---

## 👤 作者

- **GitHub**：[rnvale](https://github.com/rnvale)
- **网站**：[https://haolin-zone.xyz](https://haolin-zone.xyz)
