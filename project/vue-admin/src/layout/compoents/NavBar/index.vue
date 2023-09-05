<template>
    <div class="navbar">
        <div class="flex">
          <Breadcrumb />
        </div>
        <div class="flex">
          <NavRight />
        </div>
    </div>
</template>

<script setup lang="ts">
import NavRight from './NavRight.vue'
import Breadcrumb from '../Breadcrumb/index.vue'
</script>

<style lang="scss" scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 50px;
  background-color: #fff;
  box-shadow: 0 0 1px #0003;
}
</style>