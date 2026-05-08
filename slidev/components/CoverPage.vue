<script setup>
import BottomNav from "./BottomNav.vue"
</script>

<template>
  <div class="cover-page">
    <div class="cover-card">
      <div class="badge">Slidev + Streamlit</div>

      <h1>qPCR + ddPCR 分析工具</h1>

      <p class="subtitle">
        基于 Python、Streamlit 与 Slidev 的交互式演示课件
      </p>

      <div class="info-grid">
        <div class="info-card">
          <div class="info-title">左侧</div>
          <div class="info-text">展示项目结构与 Python 代码</div>
        </div>

        <div class="info-card">
          <div class="info-title">右侧</div>
          <div class="info-text">嵌入可实时操作的 Streamlit 工具</div>
        </div>

        <div class="info-card">
          <div class="info-title">底部</div>
          <div class="info-text">横向目录、页码与翻页导航</div>
        </div>
      </div>
    </div>

    <BottomNav />
  </div>
</template>

<style scoped>
.cover-page {
  height: 100vh;
  width: 100%;
  box-sizing: border-box;
  padding: 38px 64px 96px;
  background:
    linear-gradient(rgba(15, 23, 42, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(15, 23, 42, 0.035) 1px, transparent 1px),
    #f8fafc;
  background-size: 30px 30px;
  color: #111827;
  overflow: hidden;
}

.cover-card {
  height: calc(100vh - 150px);
  border-radius: 28px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #e5e7eb;
  box-shadow: 0 28px 70px rgba(15, 23, 42, 0.13);
  padding: 48px 70px;
  box-sizing: border-box;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 8px 14px;
  border-radius: 999px;
  background: #111827;
  color: #ffffff;
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 28px;
}

h1 {
  font-size: 58px;
  line-height: 1.06;
  letter-spacing: -0.04em;
  margin: 0;
  font-weight: 900;
}

.subtitle {
  margin-top: 22px;
  color: #6b7280;
  font-size: 22px;
  line-height: 1.45;
}

.info-grid {
  margin-top: 58px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}

.info-card {
  min-height: 120px;
  border-radius: 20px;
  border: 1px solid #e5e7eb;
  background: #ffffff;
  padding: 22px 24px;
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.08);
}

.info-title {
  font-size: 16px;
  font-weight: 800;
  color: #111827;
  margin-bottom: 10px;
}

.info-text {
  color: #6b7280;
  font-size: 15px;
  line-height: 1.55;
}
</style>