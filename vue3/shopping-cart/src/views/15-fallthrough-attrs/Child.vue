<template>
    <div id="child">
        Child
    </div>
</template>
<script>
    export default {
        inheritAttrs: false //阻止组件之间的透传
    }
</script>
<script setup>
    //局部注册组件
import {ref, useAttrs} from 'vue'
const attrs = useAttrs()
console.log('class-->', attrs) //通过useAttrs透传可以直接获取父组件继承过来的所有属性
</script>

<style lang="css">
.world{
    font-size: 50px;
    color: red;
}
</style>