<script setup>
import BottomNav from "./BottomNav.vue"

const steps = [
  {
    title: "继续优化演示页",
    text: "调整代码区比例、Streamlit 嵌入比例、字号、边距与页面层级。"
  },
  {
    title: "增强代码展示",
    text: "让 app.py 与 compute.py 与真实文件同步，减少展示代码和运行代码不一致。"
  },
  {
    title: "部署 Streamlit",
    text: "将 Python 工具部署到 Streamlit Community Cloud，得到公网工具链接。"
  },
  {
    title: "部署 Slidev",
    text: "将课件部署到 GitHub Pages、Vercel 或 Netlify，形成可分享网页课件。"
  }
]
</script>

<template>
  <div class="next-page">
    <div class="header">
      <div>
        <div class="eyebrow">Next Steps</div>
        <h1>下一步 · 持续升级计划</h1>
      </div>

      <div class="note">
        从本地演示走向可分享网页课件
      </div>
    </div>

    <div class="step-grid">
      <div
        v-for="(step, index) in steps"
        :key="step.title"
        class="step-card"
      >
        <div class="step-index">
          {{ String(index + 1).padStart(2, "0") }}
        </div>

        <div class="step-title">
          {{ step.title }}
        </div>

        <div class="step-text">
          {{ step.text }}
        </div>
      </div>
    </div>

    <div class="summary-card">
      <div class="summary-title">当前已经完成</div>
      <div class="summary-text">
        Streamlit 本地运行、Slidev 本地运行、课件嵌入工具、代码文件切换、底部导航原型。
      </div>
    </div>

    <BottomNav />
  </div>
</template>

<style scoped>
.next-page {
  height: 100vh;
  width: 100%;
  box-sizing: border-box;
  padding: 30px 64px 105px;
  background:
    linear-gradient(rgba(15, 23, 42, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(15, 23, 42, 0.035) 1px, transparent 1px),
    #f8fafc;
  background-size: 30px 30px;
  color: #111827;
  overflow: hidden;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
}

.eyebrow {
  display: inline-flex;
  padding: 7px 13px;
  border-radius: 999px;
  background: #111827;
  color: #ffffff;
  font-size: 13px;
  font-weight: 800;
  margin-bottom: 16px;
}

h1 {
  font-size: 38px;
  line-height: 1.1;
  margin: 0;
  font-weight: 900;
  letter-spacing: -0.03em;
}

.note {
  margin-top: 16px;
  color: #6b7280;
  font-size: 16px;
}

.step-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.step-card {
  min-height: 166px;
  border-radius: 22px;
  padding: 18px 20px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid #e5e7eb;
  box-shadow: 0 18px 42px rgba(15, 23, 42, 0.09);
}

.step-index {
  width: 36px;
  height: 36px;
  border-radius: 999px;
  background: #111827;
  color: #ffffff;
  font-size: 13px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}

.step-title {
  font-size: 17px;
  font-weight: 850;
  margin-bottom: 9px;
}

.step-text {
  font-size: 13.5px;
  line-height: 1.6;
  color: #6b7280;
}

.summary-card {
  margin-top: 22px;
  border-radius: 24px;
  background: #111827;
  color: #ffffff;
  padding: 18px 26px;
  box-shadow: 0 20px 48px rgba(15, 23, 42, 0.18);
}

.summary-title {
  font-size: 18px;
  font-weight: 850;
  margin-bottom: 8px;
}

.summary-text {
  color: #d1d5db;
  font-size: 15px;
}
</style>