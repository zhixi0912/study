<template>
    <div :class="[italic,{a:isA,b:isB}]" class="c d">
        <p>hello vue3</p>
    </div>
    <div>
        <button @click="handelClick">change</button>
    </div>
    <div><example></example></div>
</template>

<script setup>
 import { ref  } from 'vue';
 import example from './Example.vue'
 const italic = ref('italic')
 const isA = ref(true)
 const isB = ref(true)
 const handelClick = () => {
    isA.value = !isA.value
 }
</script>

<style lang="css">
.a{
    color: red;
}
.b{
    font-size: 50px;
}
.c{
    font-weight: 900;
}
.d{
    text-decoration: underline;
}
.italic{
    font-style: italic;
}
</style>