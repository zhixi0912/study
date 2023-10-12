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
<el-dialog
    v-model="dialogVisible"
    title="录屏回放"
    width="30%"
    :before-close="handleClose"
    center
>
    <div class="vido-box" v-loading="loading">
      <span>This is a message</span>

    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogVisible = false">
          Confirm
        </el-button>
      </span>
    </template>
</el-dialog>
</template>
<script lang="ts" setup>
import RecordRTC from 'recordrtc';
import { ref, onMounted } from 'vue'
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

const dialogVisible = ref(false)
const loading = ref(true)
const handleClose = (done: () => void) => {
    ElMessageBox.confirm('Are you sure to close this dialog?')
    .then(() => {
        done()
    })
    .catch(() => {
        // catch error
    })
}
</script>
<style scoped>
.vido-box {
  min-height: 300px;
}
</style>