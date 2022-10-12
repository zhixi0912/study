<template>
    <div>
        <Child>
            <!-- <template #default="data"> -->
            <template v-slot:default="data">
                <div>{{str}} {{data.mark2}} world {{data.mark}}</div>
            </template>
            <template v-slot:line2>
                <div>{{str}} slot</div>
            </template>
        </Child>
    </div>
</template>

<script setup>
 import { ref  } from 'vue';
import Child from './Child.vue'
const str = ref('hello')
</script>

<style lang="css">

</style>