<template>
    <div>
        {{title}}
        <Child v-model:titleEvent="title"></Child>
    </div>
</template>

<script setup>
    //注册组件
    import {ref} from 'vue'
 import Child from './Child.vue'
const title = ref('hello')
</script>

<style lang="css">

</style>