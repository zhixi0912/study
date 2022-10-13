<template>
    <div>
        {{title}} Child2
        <Grandson></Grandson>
    </div>
</template>

<script setup>
    //局部注册组件
import { ref, inject } from 'vue';
import Grandson from './Grandson.vue';
const title = inject('title')
</script>

<style lang="css">

</style>