<template>
    <div>
        {{name}}
        <input type="text" v-model="name" />
    </div>
    <div>
        <textarea v-model="about"></textarea>
    </div>
    <div>
        隐藏：<input type="checkbox" v-model="isShow" />{{isShow ? '是' : '否'}}
    </div>
    <div>
        {{sex}}
        <input type="radio" value="男" v-model="sex" />男
        <input type="radio" value="女" v-model="sex" />女
        <input type="radio" value="保密" v-model="sex" />保密
    </div>
    <div>
        {{interest}}
        <input type="checkbox" value="教育" v-model="interest" />教育
        <input type="checkbox" value="动漫" v-model="interest" />动漫
        <input type="checkbox" value="新闻" v-model="interest" />新闻
    </div>
    <div>
        {{city}}
        <select v-model="city">
            <option>北京</option>
            <option>上海</option>
            <option>广州</option>
        </select>
    </div>
    <div>
        {{time}}
        <select v-model="time" @click="handelClick" multiple>
            <option>06:00</option>
            <option>08:00</option>
            <option>10:00</option>
            <option>12:00</option>
            <option>14:00</option>
        </select>
    </div>
</template>

<script setup>
 import { ref  } from 'vue';
const name = ref('')
const about =ref('')
const isShow = ref(true)
const sex = ref('')
const interest = ref([])
const city = ref('广州')
const time = ref([])
const handelClick =(e)=>{
    console.log(e.target.value)
}
</script>

<style lang="css">
div{
    margin-bottom: 10px;
}
</style>