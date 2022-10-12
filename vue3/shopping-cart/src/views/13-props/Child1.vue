<template>
    <div>
        Child1
        <p>{{count.count}}</p>
    </div>
</template>

<script setup>
    //局部注册组件
    import {ref, onMounted} from 'vue'
    const count = defineProps(['count'])
    const title = ref('hello')
    const emit = defineEmits(['my-event1'])
    console.log('child1--->', count.count)
    onMounted(()=>{
        emit('my-event1', title)
    })
</script>

<style lang="css">

</style>