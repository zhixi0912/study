<template>
<el-row :gutter="12">
    <el-col :span="8">
        <el-button type="success" :icon="VideoPlay" @click="startRecord" >开始</el-button>
    </el-col>
    <el-col :span="8">
      <el-button type="danger" :icon="VideoPause" @click="stopRecord" >暂停</el-button>
    </el-col>
    <el-col :span="8">
      <el-button type="primary" :icon="VideoCamera" @click="dialogVisible = true" >播放</el-button>
    </el-col>
</el-row>
</template>
<script lang="ts" setup>
import RecordRTC from 'recordrtc';
import { ElMessageBox, ElMessage } from 'element-plus'
import {
    VideoPlay,
    VideoPause,
    VideoCamera,
} from '@element-plus/icons-vue'
const startRecord = () => {
    ElMessage({
        message: '开始视频录制',
        type: 'success'
    })

}

const stopRecord = () => {
    ElMessage({
        message: '停止视频录制',
        type: 'success'
    })

}
</script>