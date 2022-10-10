<template>
    <div>
        <p>{{count}}</p>
        {{doubleCount}}
        <!-- {{doubleCount()}} -->
    </div>
    <div>
        <button @click="handelClick">add</button>
    </div>
</template>

<script setup>
 import { ref, computed  } from 'vue'
 const count = ref(1)
 const handelClick = ()=>{
    count.value++
 }
 const doubleCount = computed(()=>{
    return count.value *2
 })
//  const doubleCount = ()=>{
//     return count.value *2
//  }
</script>

<style lang="css">

</style>