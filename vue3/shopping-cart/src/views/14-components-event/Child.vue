<template>
    <div>
        Child
    </div>
</template>

<script setup>
    //局部注册组件
    import {ref, onMounted} from 'vue'
    const props = defineProps(['titleEvent'])
    const emit =defineEmits(['update:titleEvent'])
    const title = ref('World')
    onMounted(()=>{
        console.log('props--->', props.titleEvent)
        let obj = props.titleEvent
        emit('update:titleEvent', obj += title.value)
    })
</script>

<style lang="css">

</style>