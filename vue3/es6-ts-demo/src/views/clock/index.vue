<template>
  <div class="clock">
    <canvas ref="canvas" />
  </div>
</template>
<script setup lang="ts">
import { onMounted } from 'vue'
import { clock } from './index'

onMounted(()=>{
  const canvas = document.querySelector('canvas')
  clock(canvas)
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