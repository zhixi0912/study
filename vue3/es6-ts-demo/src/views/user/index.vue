<template>
  <div class="app-container">
    <div class="app-item" v-for="n in 100">
      <heavy-comp v-if="defer(n)" />
    </div>
  </div>
</template>
<script setup lang="ts">
import HeavyComp from './HeavyComp.vue'
import { useDefer } from './useDefer'
// 分步加载组件，提高页面渲染效率
const defer = useDefer();

</script>
<style lang="scss" scoped>
.app-container {
  display: flex;
  flex-wrap: wrap;
  .app-item{
    margin: 10px;
    max-width: 30%;
    flex: 0 0 30%;
  }
}
</style>
