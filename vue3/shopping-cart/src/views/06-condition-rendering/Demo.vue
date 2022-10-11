<template>
    <div v-if="isShow >= 75">{{isShow}}</div>
    <div>
        {{ count }}
        <button @click="handelClick">tagger</button>
    </div>
</template>

<script setup>
 import { ref  } from 'vue';
 const isShow = ref(65)
 const handelClick = () => {
    isShow.value = 85
 }
</script>

<style lang="css">

</style>