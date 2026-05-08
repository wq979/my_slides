<script setup>
import { computed, ref } from "vue"
import BottomNav from "./BottomNav.vue"

import appCode from "../snippets/app.py?raw"
import computeCode from "../snippets/compute.py?raw"

const activeFile = ref("app.py")

const files = {
  "app.py": appCode,
  "compute.py": computeCode,
}

const activeCode = computed(() => files[activeFile.value] || "")

const lineCount = computed(() => {
  return activeCode.value.split("\n").length
})
</script>

<template>
  <div class="demo-page">
    <div class="top-bar">
      <div class="brand">
        <div class="brand-mark">03</div>
        <div>
          <div class="top-title">Demo 03 · qPCR + ddPCR 分析工具</div>
          <div class="top-subtitle">代码工作区 + Streamlit 实时工具</div>
        </div>
      </div>

      <div class="top-note">
        Slidev + Streamlit · 本地交互演示
      </div>
    </div>

    <div class="main-grid">
      <section class="workspace">
        <aside class="project-panel">
          <div class="panel-title">项目</div>

          <div class="project active">
            <div class="project-name">qpcr-tool/</div>
            <div class="project-desc">合并前 · qPCR</div>
          </div>

          <div class="project">
            <div class="project-name">ddpcr-tool/</div>
            <div class="project-desc">合并前 · ddPCR</div>
          </div>

          <div class="project">
            <div class="project-name">qpcr-ddpcr-tool/</div>
            <div class="project-desc">合并后</div>
          </div>
        </aside>

        <aside class="file-panel">
          <div class="panel-title">文件</div>

          <button
            v-for="(_, name) in files"
            :key="name"
            class="file-button"
            :class="{ active: activeFile === name }"
            @click="activeFile = name"
          >
            <span class="file-dot"></span>
            {{ name }}
          </button>
        </aside>

        <section class="code-panel">
          <div class="code-tabs">
            <button
              v-for="(_, name) in files"
              :key="name"
              class="code-tab"
              :class="{ active: activeFile === name }"
              @click="activeFile = name"
            >
              {{ name }}
            </button>
          </div>

          <div class="code-header">
            <span># {{ activeFile }}</span>
            <span class="code-header-note">展示代码；右侧为实际运行结果</span>
          </div>

          <div class="code-scroll">
            <div class="line-gutter">
              <span v-for="line in lineCount" :key="line">{{ line }}</span>
            </div>

            <pre class="code-view"><code>{{ activeCode }}</code></pre>
          </div>

          <div class="status-bar">
            <span>Python</span>
            <span>UTF-8</span>
            <span>{{ lineCount }} lines</span>
          </div>
        </section>
      </section>

      <section class="app-card">
        <div class="browser-bar">
          <div class="browser-url">localhost:8501</div>
          <div class="browser-brand">● Streamlit</div>
        </div>

        <div class="iframe-wrap">
          <iframe
            src="http://localhost:8501/?embed=true"
            class="streamlit-frame"
          />
        </div>
      </section>
    </div>

    <BottomNav />
  </div>
</template>

<style scoped>
.demo-page {
  height: 100vh;
  width: 100%;
  box-sizing: border-box;
  padding: 16px 32px 96px;
  background:
    linear-gradient(rgba(15, 23, 42, 0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(15, 23, 42, 0.025) 1px, transparent 1px),
    #f8fafc;
  background-size: 28px 28px;
  color: #111827;
  overflow: hidden;
}

.top-bar {
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-mark {
  width: 36px;
  height: 36px;
  border-radius: 999px;
  background: #111827;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 800;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.18);
}

.top-title {
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.top-subtitle {
  font-size: 12px;
  color: #6b7280;
  margin-top: 2px;
}

.top-note {
  font-size: 13px;
  color: #6b7280;
}

.main-grid {
  height: calc(100vh - 172px);
  display: grid;
  grid-template-columns: 1.32fr 0.9fr;
  gap: 20px;
}

.workspace {
  display: grid;
  grid-template-columns: 150px 140px 1fr;
  min-width: 0;
  background: #0d1117;
  border-radius: 18px;
  overflow: hidden;
  border: 1px solid #1f2937;
  box-shadow: 0 18px 45px rgba(15, 23, 42, 0.22);
}

.project-panel {
  background: #05070a;
  color: #e5e7eb;
  padding: 14px 0;
  border-right: 1px solid #1f2937;
}

.file-panel {
  background: #111827;
  color: #e5e7eb;
  padding: 14px 0;
  border-right: 1px solid #1f2937;
}

.panel-title {
  font-size: 12px;
  color: #9ca3af;
  padding: 0 16px 10px;
}

.project {
  padding: 10px 14px;
  border-left: 3px solid transparent;
}

.project.active {
  background: #1f2937;
  border-left-color: #ef4444;
}

.project-name {
  font-size: 13px;
  font-weight: 800;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.project-desc {
  font-size: 10.5px;
  color: #9ca3af;
  margin-top: 2px;
}

.file-button {
  width: 100%;
  border: 0;
  background: transparent;
  color: #9ca3af;
  text-align: left;
  padding: 10px 14px;
  font-size: 13px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  border-left: 3px solid transparent;
}

.file-button:hover {
  background: rgba(255, 255, 255, 0.04);
}

.file-button.active {
  background: #2b2f36;
  color: #ffffff;
  border-left-color: #ef4444;
}

.file-dot {
  width: 7px;
  height: 7px;
  border-radius: 999px;
  background: #60a5fa;
}

.code-panel {
  display: flex;
  flex-direction: column;
  min-width: 0;
  background: #0d1117;
}

.code-tabs {
  height: 38px;
  display: flex;
  align-items: stretch;
  border-bottom: 1px solid #1f2937;
  background: #111827;
}

.code-tab {
  border: 0;
  border-right: 1px solid #1f2937;
  padding: 0 18px;
  background: transparent;
  color: #9ca3af;
  font-size: 13px;
  cursor: pointer;
}

.code-tab.active {
  background: #0d1117;
  color: #f9fafb;
}

.code-header {
  height: 42px;
  padding: 0 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #1f2937;
  color: #34d399;
  font-size: 13px;
  font-family: Consolas, "Courier New", monospace;
}

.code-header-note {
  color: #6b7280;
  font-size: 11px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.code-scroll {
  flex: 1;
  min-height: 0;
  overflow: auto;
  display: flex;
  background: #0d1117;
}

.line-gutter {
  flex: 0 0 44px;
  padding: 18px 8px 18px 0;
  text-align: right;
  color: #4b5563;
  background: #0a0f16;
  border-right: 1px solid #111827;
  font-size: 12px;
  line-height: 1.55;
  font-family: Consolas, "Courier New", monospace;
  user-select: none;
}

.line-gutter span {
  display: block;
}

.code-view {
  margin: 0;
  padding: 18px 22px;
  color: #f9fafb;
  font-size: 12.5px;
  line-height: 1.55;
  font-family: Consolas, "Courier New", monospace;
  white-space: pre;
  min-width: max-content;
}

.status-bar {
  height: 26px;
  background: #111827;
  border-top: 1px solid #1f2937;
  color: #9ca3af;
  font-size: 11px;
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0 14px;
}

.app-card {
  background: #ffffff;
  border-radius: 18px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
  box-shadow: 0 18px 45px rgba(15, 23, 42, 0.13);
}

.browser-bar {
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  border-bottom: 1px solid #e5e7eb;
  background: #ffffff;
}

.browser-url {
  font-family: Consolas, "Courier New", monospace;
  color: #6b7280;
  font-size: 13px;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 7px;
  padding: 4px 10px;
}

.browser-brand {
  color: #ef4444;
  font-size: 13px;
  font-weight: 800;
}

.iframe-wrap {
  height: calc(100% - 42px);
  overflow: hidden;
  background: #ffffff;
}

.streamlit-frame {
  width: 156%;
  height: 156%;
  border: 0;
  transform: scale(0.64);
  transform-origin: top left;
}
</style>