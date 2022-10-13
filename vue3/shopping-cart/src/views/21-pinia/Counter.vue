<template>
    <div>
        <!-- {{counterStore.count}}
        <p><button @click="counterStore.add()">add</button></p> -->
        {{count}}
        <p>{{title}}</p>
        <p><button @click="counterStore.add()">add</button></p>
        <Child></Child>
    </div>
</template>

<script setup>
import {storeToRefs} from 'pinia'  //storeToRefs将失去响应性的数据恢复响应性
import useCounterStore from '../../store/counterState'
import Child from './Child.vue'
const counterStore = useCounterStore()
const {count, title} = storeToRefs(counterStore)
</script>

<style lang="scss">

</style>