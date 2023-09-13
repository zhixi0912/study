<template>
    <div class="switch-box" @click="switchMenu">
        <el-icon><Grid /></el-icon>
    </div>
</template>

<script setup lang="ts">
import { Grid } from '@element-plus/icons-vue'
import { useFoldSideberStore } from '@/store/modules/settings.ts'
import { storeToRefs } from 'pinia'

const fold = useFoldSideberStore()
const { isCollapse } = storeToRefs(fold)
const switchMenu = () => {
    fold.foldSideber(isCollapse.value)
    console.log('isCollapse------------>', isCollapse.value)
}
</script>
<style scoped>
.switch-box {
    color: #99a9bf;
    font-size: 14px;
    cursor: pointer;
}
</style>