<template>
    <div>
        {{ rawHtml }}
    </div>
    <div v-html="rawHtml"></div>
    <div v-bind="obj">obj</div>
    <button @click="handelClick">反转切换</button>
    <div v-if="toggle">是</div>
    <div v-else>否</div>
    <div v-bind:title="title">我有标题</div>
    <div>
        {{ title2.split('').reverse().join('') }}
    </div>
    <div>
        <p>{{ inputVal }}</p>
        <!-- <input type="text" v-on:keyup.enter="hanedlKeyup" /> -->
        <input type="text" v-on:keyup="hanedlKeyup" />
    </div>
</template>

<script setup>
 import { ref  } from 'vue';
 const rawHtml = ref('<p>2022</p>')
 const title = '我是标题'
 const title2 = 'hello vue3'
 const obj = ref({
    id: '01',
    class: 'box'
 })
 const toggle = ref(true)
 const handelClick = () => {
    toggle.value = !toggle.value
 }
 const inputVal = ref('')
 const hanedlKeyup = (e)=>{
    console.log(e.target.value)
    inputVal.value = e.target.value
 }
</script>

<style lang="css">

</style>