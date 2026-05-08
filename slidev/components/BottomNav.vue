<template>
  <div class="bottom-shell">
    <button class="round-button" @click="$nav.prev()">‹</button>

    <div class="nav-strip">
      <button
        v-for="item in pageItems"
        :key="item.page"
        class="strip-item"
        :class="{ active: $nav.currentPage === item.page }"
        @click="$nav.go(item.page)"
      >
        <span class="strip-page">{{ item.page }}</span>
        <span class="strip-title">{{ item.title }}</span>
      </button>

      <div class="progress-track">
        <div
          class="progress-inner"
          :style="{ width: `${($nav.currentPage / 3) * 100}%` }"
        />
      </div>
    </div>

    <div class="page-pill">{{ $nav.currentPage }} / 3</div>

    <button class="round-button" @click="$nav.next()">›</button>

    <button class="toc-button" @click="$nav.go(1)">☰ 目录</button>
  </div>
</template>

<script setup>
const pageItems = [
  { page: 1, title: "封面 · qPCR + ddPCR 分析工具" },
  { page: 2, title: "Demo 03 · qPCR + ddPCR 分析工具" },
  { page: 3, title: "下一步 · 持续升级计划" },
]
</script>

<style scoped>
.bottom-shell {
  position: fixed;
  left: 44px;
  right: 44px;
  bottom: 12px;
  z-index: 9999;
  height: 46px;
  display: grid;
  grid-template-columns: 38px 1fr 68px 38px 86px;
  gap: 8px;
  align-items: center;
  pointer-events: auto;
}

.nav-strip {
  position: relative;
  height: 46px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid rgba(229, 231, 235, 0.95);
  box-shadow: 0 10px 26px rgba(15, 23, 42, 0.12);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  padding: 0 14px 5px;
  box-sizing: border-box;
  overflow: hidden;
}

.strip-item {
  border: 0;
  border-radius: 999px;
  padding: 6px 12px;
  margin-right: 6px;
  background: transparent;
  color: #6b7280;
  font-size: 12px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  white-space: nowrap;
}

.strip-item:hover {
  background: #f3f4f6;
  color: #111827;
}

.strip-item.active {
  background: #111827;
  color: #ffffff;
  font-weight: 800;
}

.strip-page {
  opacity: 0.72;
}

.strip-title {
  max-width: 280px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.progress-track {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 7px;
  height: 3px;
  border-radius: 999px;
  background: #e5e7eb;
  overflow: hidden;
}

.progress-inner {
  height: 100%;
  border-radius: 999px;
  background: #111827;
  transition: width 0.25s ease;
}

.round-button {
  width: 38px;
  height: 38px;
  border-radius: 999px;
  border: 1px solid #e5e7eb;
  background: rgba(255, 255, 255, 0.95);
  color: #111827;
  font-size: 23px;
  line-height: 1;
  cursor: pointer;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.12);
}

.round-button:hover {
  background: #111827;
  color: #ffffff;
}

.page-pill {
  height: 38px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid #e5e7eb;
  color: #111827;
  font-size: 13px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.12);
}

.toc-button {
  height: 38px;
  border: 0;
  background: #111827;
  color: #ffffff;
  font-size: 13px;
  font-weight: 800;
  padding: 0 14px;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.15);
}

.toc-button:hover {
  background: #000000;
}
</style>