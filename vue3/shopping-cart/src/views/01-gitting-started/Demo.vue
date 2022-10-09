<template>
    <div>
        {{ count }}
        <button @click="handelClick">add</button>
    </div>
</template>

<script setup>
 import { ref  } from 'vue';
 const count = ref(0)
 const handelClick = () => {
    count.value ++
 }
</script>

<style lang="css">

</style>