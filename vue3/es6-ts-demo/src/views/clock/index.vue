<template>
  <div class="clock">
    <canvas ref="canvas" />
  </div>
</template>
<script setup lang="ts">
import { onMounted ,ref } from 'vue'
import { p } from './index'
onMounted(()=>{
  p.draw();
})
</script>
<style lang="scss" scoped>
body {
  margin: 0;
  padding: 0;
}
.clock {
  canvas {
    background: radial-gradient(#fff, #8c738c);
    display: block;
    width: 100%;
    height: 100vh;
  }
}
</style>