<template>
  <div class="login-main">
    login
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const data = ref(false)
console.log('data---->', data)
</script>


<style lang="scss" scoped>
.login-main {
  background: #1f2d3d;
  font-size: 12px;
  color: #000000;
  line-height: 20px;
}
</style>