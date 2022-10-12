<template>
    <div>
        {{ count }}
        <p>{{doubleCount}}</p>
        <p>{{text}}</p>
        <button @click="handelClick">add</button>
    </div>
</template>

<script setup>
    //侦听器
 import { computed } from '@vue/reactivity';
import { ref, watchEffect, watch  } from 'vue';
 const count = ref(1)
 const doubleCount = computed(()=>count.value*2)
 const text = ref('hello')
 const handelClick = () => {
    count.value ++
 }
 watchEffect(()=>{
    //侦听所有条件的变化，页面加载时会执行一次
    console.log('count变化为：'+count.value)
 })
 watch(
    //精确侦听具体某一条件的变化，页面加载时不触发
    // count,
    // ()=>{
    //     console.log('----')
    // }
    ()=>{
        text.value = 'vue3'
        //可在条件发生变化前执行某些逻辑
        return count.value//侦听的条件
    },
    ()=>{
        console.log('count发生变化了')
        //侦听到变化后执行逻辑
    }
 )
</script>

<style lang="css">

</style>