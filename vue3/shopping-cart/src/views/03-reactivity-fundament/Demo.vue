<template>
    <div>
        <button @click="handelClickRef">ref add {{count}}</button>
        <button @click="handelClickRec">reactive add {{state.count}}</button>
    </div>
</template>

<script setup>
 import { ref, reactive  } from 'vue';
 const count = ref(0)
 const state = reactive({
    count: 0
 })
 const handelClickRef = ()=>{
    count.value++
 }
 const handelClickRec = ()=>{
    state.count++
 }
</script>

<style lang="css">

</style>