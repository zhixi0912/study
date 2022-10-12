<template>
    <div>
        <slot :mark="mark" mark2="--->"></slot>
        <slot name="line2"></slot>
    </div>
</template>

<script setup>
    //局部注册组件
import {ref} from 'vue'
const mark = ref('!!!')
</script>

<style lang="css">

</style>