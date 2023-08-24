<template>
  <div class="app-wrapper common-layout">
    <el-container>
      <el-aside class="sidebar-container">
        <sidebar />
      </el-aside>
      <el-container class="main-container">
        <el-header>
          <navBar />
        </el-header>
        <el-main style="padding: 0">
          <appMain />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import appMain from './compoents/index.vue'
import sidebar from './compoents/Sidebar/index.vue'
import navBar from './compoents/NavBar/index.vue'
</script>

<style lang="scss" scoped>
.app-wrapper {
  &::after {
    display: table;
    clear: both;
    content: "";
  }

  position: relative;
  width: 100%;
  height: 100%;

  &.mobile.openSidebar {
    position: fixed;
    top: 0;
  }
}

.fixed-header {
  position: fixed;
  top: 0;
  right: 0;
  z-index: 9;
  width: calc(100% - #{$sideBarWidth});
  transition: width 0.28s;
}

.hideSidebar .fixed-header {
  width: calc(100% - 54px);
}

.mobile .fixed-header {
  width: 100%;
}

.drawer-bg {
  position: absolute;
  top: 0;
  z-index: 999;
  width: 100%;
  height: 100%;
  background: #000;
  opacity: 0.3;
}
// 导航栏顶部显示
.isTop {
  .sidebar-container {
    z-index: 800;
    display: flex;
    width: 100% !important;
    height: 50px;

    :deep(.logo-wrap) {
      width: 210px;
    }

    :deep(.el-scrollbar) {
      flex: 1;
      min-width: 0;
      height: 50px;
    }
  }

  .main-container {
    padding-top: 50px;
    margin-left: 0;
  }

  // 顶部模式全局变量修改
  --el-menu-item-height: 50px;
}
</style>