<template>
    <div>
        Child1
        <p>{{count}}</p>
    </div>
</template>

<script setup>
    //局部注册组件
    import {ref, onMounted} from 'vue'
    const props = defineProps(['count'])
    const title = ref('hello')
    const emit = defineEmits(['my-event1'])
    console.log('child1--->', props.count)
    onMounted(()=>{
        emit('my-event1', title)
    })
</script>

<style lang="css">

</style>