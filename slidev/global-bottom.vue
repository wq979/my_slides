<script setup>
const pageItems = [
  { page: 1, title: "封面 · qPCR + ddPCR 分析工具" },
  { page: 2, title: "Demo 03 · qPCR + ddPCR 分析工具" },
  { page: 3, title: "下一步 · 持续升级计划" },
]
</script>

<template>
  <div class="bottom-shell">
    <div class="chapter-strip">
      <div class="strip-scroll">
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
      </div>

      <div class="strip-progress">
        <div
          class="strip-progress-inner"
          :style="{ width: `${($nav.currentPage / $nav.total) * 100}%` }"
        />
      </div>
    </div>

    <div class="nav-center">
      <div class="page-circle">
        {{ $nav.currentPage }}
      </div>

      <button class="nav-button" @click="$nav.prev()">
        ‹ 上一页
      </button>

      <div class="page-total">
        / {{ $nav.total }}
      </div>

      <button class="nav-button" @click="$nav.next()">
        下一页 ›
      </button>

      <button class="toc-button" @click="$nav.go(1)">
        ☰ 目录
      </button>
    </div>
  </div>
</template>

<style scoped>
.bottom-shell {
  position: fixed;
  left: 28px;
  right: 28px;
  bottom: 18px;
  z-index: 9999;
  pointer-events: none;
}

.chapter-strip {
  pointer-events: auto;
  height: 54px;
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.96);
  border: 1px solid rgba(229, 231, 235, 0.95);
  box-shadow: 0 12px 35px rgba(15, 23, 42, 0.18);
  backdrop-filter: blur(10px);
  overflow: hidden;
  padding: 8px 14px 6px;
  box-sizing: border-box;
}

.strip-scroll {
  display: flex;
  align-items: center;
  gap: 8px;
  overflow-x: auto;
  overflow-y: hidden;
  white-space: nowrap;
  height: 30px;
}

.strip-scroll::-webkit-scrollbar {
  height: 5px;
}

.strip-scroll::-webkit-scrollbar-thumb {
  background: #9ca3af;
  border-radius: 999px;
}

.strip-item {
  flex: 0 0 auto;
  border: 0;
  border-radius: 8px;
  padding: 6px 11px;
  background: transparent;
  color: #6b7280;
  font-size: 12px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.strip-item:hover {
  background: #f3f4f6;
  color: #111827;
}

.strip-item.active {
  background: #111827;
  color: #ffffff;
  font-weight: 700;
}

.strip-page {
  opacity: 0.7;
}

.strip-title {
  max-width: 260px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.strip-progress {
  height: 4px;
  background: #e5e7eb;
  border-radius: 999px;
  margin-top: 6px;
  overflow: hidden;
}

.strip-progress-inner {
  height: 100%;
  background: #111827;
  border-radius: 999px;
  transition: width 0.25s ease;
}

.nav-center {
  pointer-events: auto;
  width: max-content;
  height: 46px;
  margin: 10px auto 0;
  padding: 0 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.96);
  border: 1px solid rgba(229, 231, 235, 0.95);
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.18);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  gap: 10px;
}

.page-circle {
  width: 36px;
  height: 36px;
  border-radius: 999px;
  border: 3px solid #111827;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 800;
  color: #111827;
}

.nav-button {
  border: 0;
  background: transparent;
  color: #4b5563;
  font-size: 13px;
  cursor: pointer;
  padding: 7px 8px;
  border-radius: 8px;
}

.nav-button:hover {
  background: #f3f4f6;
  color: #111827;
}

.page-total {
  color: #9ca3af;
  font-size: 13px;
}

.toc-button {
  border: 0;
  background: #111827;
  color: #ffffff;
  font-size: 13px;
  font-weight: 700;
  padding: 8px 13px;
  border-radius: 999px;
  cursor: pointer;
}

.toc-button:hover {
  background: #000000;
}
</style>