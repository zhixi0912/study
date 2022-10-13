<template>
    <div>
        {{title}} Grandson
    </div>
</template>

<script setup>
    //局部注册组件
    import { ref, inject } from 'vue';
    const title = inject('title')
</script>

<style lang="css">

</style>