<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <sidebar />
      </el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <appMain />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import appMain from './compoents/index.vue'
import sidebar from './compoents/Sidebar/index.vue'
</script>

<style scoped>

</style>