<script setup lang="ts">
import { ref } from 'vue'
</script>

<template>
  <section class="app-main">
    <router-view />
  </section>
</template>

<style lang="scss" scoped>
.app-main {
  position: relative;
  width: 100%;
  padding: 20px;
  /* 50= navbar  50  */
  min-height: calc(100vh - 60px);
  overflow: hidden;
  background-color: var(--el-bg-color-page);
}

.fixed-header + .app-main {
  padding-top: 50px;
}

.hasTagsView {
  .app-main {
    /* 84 = navbar + tags-view = 50 + 34 */
    min-height: calc(100vh - 84px);
  }

  .fixed-header + .app-main {
    min-height: 100vh;
    padding-top: 84px;
  }
}
</style>