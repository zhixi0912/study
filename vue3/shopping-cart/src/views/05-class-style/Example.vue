<template>
    <ul class="box">
        <li v-for="item, index in list"
        :class="{active:index === crunteIndex}"
        @click="handelClick(index)"
        >
            {{item}}
        </li>
    </ul>
</template>

<script setup>
 import { ref  } from 'vue';
 const list = ref(['line 1', 'line 2', 'line 3'])
 const crunteIndex =ref(0)
 const handelClick = (index) => {
    crunteIndex.value = index
 }
</script>

<style lang="css">
.box{
    border: 1px solid #999;
    padding: 20px;
}
.box li{
    cursor: pointer;
}
.active{
    color: red;
    font-size: 30px;
}
</style>