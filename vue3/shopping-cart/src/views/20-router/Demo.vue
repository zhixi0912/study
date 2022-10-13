<template>
    <div>
        <p>{{ count }}</p>
        <router-link to="/home">Hpme</router-link>{{  }}
        <router-link to="/about">About</router-link>
        <router-view></router-view>
    </div>
</template>

<script setup>
 import { ref  } from 'vue';
 const count = ref('index')
</script>

<style lang="css">

</style>