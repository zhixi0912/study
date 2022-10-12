<template>
    <div>
        <Child2 :count="count" @my-event2="handelEvent"></Child2>
    </div>
    <div>
        <Child1 :count="count" @my-event1="handelClick"></Child1>
    </div>
    <div>
        {{title}}
    </div>
</template>

<script setup>
    //注册组件
 import {ref} from 'vue'
 import Child1 from './Child1.vue'
 import Child2 from './Child2.vue'
 const title = ref('')
 const count = ref(100)
 const handelClick =(e)=>{
    console.log('来自child1-->', e.value)
    title.value += e.value
 }
 const handelEvent=(e)=>{
    console.log('来自child2-->', e.value)
    title.value += e.value
 }
</script>

<style lang="css">

</style>