<template>
    <div>
        <p>{{ count }}</p>
        <p>{{numb}}</p>
        <p>{{ text }}</p>
        <button @click="handel1(), handel2()">add</button>
        <input type="text" @input="handelInput(100, $event)" />
    </div>
</template>

<script setup>
 import { ref } from 'vue';
 const count = ref('事件处理')
 const numb = ref(0)
 const text =ref('')
 const handelInput = (num, e) => {
    numb.value += num
    text.value = e.target.value
 }
 //一个动作触发2个事件，vue3特有新属性
 const handel1 = ()=>{
    console.log('事件1')
 }
 const handel2 = ()=>{
    console.log('事件2')
 }
</script>

<style lang="css">

</style>