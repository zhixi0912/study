<template>
    <div>
        <p id="box">{{ count }}</p>
    </div>
</template>

<script setup>
    //生命周期
 import { ref, onMounted, onBeforeMount, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted } from 'vue';

 const count = ref(0)
 let t = null
 onMounted(()=>{
    //加载后
    console.log('加载后----->',document.getElementById('box').innerHTML)
    t = setTimeout(()=>{
        count.value = 1000
    },1000)
 })
onBeforeMount(()=>{
    //加载前
    // console.log('加载前----->',document.getElementById('box').innerHTML)
    count.value = 100
})
onBeforeUpdate(()=>{
    //数据更新前，DOM不变
    console.log('更新前DOM----->',document.getElementById('box').innerHTML)
    console.log('更新前value----->',count.value)
 })
 onUpdated(()=>{
    //更新后
    console.log('更新后----->',document.getElementById('box').innerHTML)
 })
 onBeforeUnmount(()=>{
    //销毁前
    // console.log('销毁前----->',document.getElementById('box').innerHTML)
 })
 onUnmounted(()=>{
    //销毁后
    // console.log('销毁后----->',document.getElementById('box').innerHTML)
    clearTimeout(t)
 })
</script>

<style lang="css">

</style>