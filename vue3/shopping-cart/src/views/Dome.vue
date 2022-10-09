<template>
    <div class="t1">
        Demo
    </div>
    <div>
        <router-link to="/home">首页</router-link>
        <router-link to="/about">关于我们</router-link>
    </div>
    <div>
        <router-view></router-view>
    </div>
</template>

<script setup>

</script>

<style scoped>
.t1{
    width: 100%;
    padding-bottom: 30px;
    border-bottom: 1px solid #000;
    display: block;
    text-align: center;
}
</style>