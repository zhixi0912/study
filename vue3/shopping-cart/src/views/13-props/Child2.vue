<template>
    <div>
        Child2
    </div>
</template>

<script setup>
    //局部注册组件
    import {ref, onMounted} from 'vue'
    const title = ref ('vue3')
    const emit = defineEmits(['my-event2'])
    onMounted(()=>{
        emit('my-event2', title)
    })
</script>

<style lang="css">

</style>