<template>
  <section class="app-main">
    <div class="switch-main">
        <SwitchMenu />
    </div>
    <router-view />
  </section>
</template>

<script setup lang="ts">
import SwitchMenu from './SwitchMenu/index.vue'
</script>

<style lang="scss" scoped>
.app-main {
  position: relative;
  width: 100%;
  padding: 20px;
  /* 50= navbar  50  */
  min-height: calc(100vh - 60px);
  overflow: hidden;
  background-color: var(--el-bg-color-page);
  .switch-main {
    position: absolute;
    width: 14px;
    height: 14px;
    top: 50%;
    left: 0px;
  }
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