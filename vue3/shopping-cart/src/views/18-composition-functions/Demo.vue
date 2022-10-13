<template>
    <div>
        {{ count }}
        <button @click="handelClick">add</button>
    </div>
</template>

<script setup>
 import userCount from './userCount'
 import userTitle from './userTitel'
 
const {count, handelClick} = userCount()
userTitle(count)
</script>

<style lang="css">

</style>