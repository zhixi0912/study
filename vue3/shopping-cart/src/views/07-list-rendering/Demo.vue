<template>
    <div>
        <ul>
            <template v-for="item,index in bookList">
                <li v-if="item.type !== '历史'">{{index+1}}: {{item.name}} --- {{item.user}}</li>
            </template>
        </ul>
    </div>
    <div>
        <ul>
            <li v-for="n,u,i in course">{{i}} - {{u}}: {{n}}</li>
        </ul>
    </div>
</template>

<script setup>
 import { ref, reactive } from 'vue';
 const course = reactive({
    name: '轮语',
    user: '孔子',
    time: '春秋战国'
 })
 const bookList = ref([
    {
        id:'01',
        name:'红楼梦',
        user:'罗惯中',
        type: '四大名著'
    },
    {
        id:'02',
        name:'西游记',
        user:'吴承恩',
        type: '四大名著'
    },
    {
        id:'03',
        name:'三国演义',
        user:'罗惯中',
        type: '四大名著'
    },
    {
        id:'04',
        name:'水浒传',
        user:'罗惯中',
        type: '四大名著'
    },
    {
        id:'03',
        name:'史记',
        user:'司马迁',
        type: '历史'
    }
 ])
</script>

<style lang="css">

</style>