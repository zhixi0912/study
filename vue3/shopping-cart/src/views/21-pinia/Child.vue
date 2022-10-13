<template>
    <div>
        Child
        <p>
            {{title}} --- {{count}}
        </p>
    </div>
</template>

<script setup>
    //局部注册组件
import useCounterStore from '@/store/counterState';
import { storeToRefs } from 'pinia'; //storeToRefs将失去响应性的数据恢复响应性
const countStore = useCounterStore()
const {count, title} = storeToRefs(countStore)
</script>

<style lang="css">

</style>