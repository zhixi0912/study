<template>
<el-row :gutter="12" v-if="false">
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
<el-row :gutter="12">
    <el-col :span="8">
        <el-button type="success" :icon="VideoPlay" @click="startRecord" > {{ startTxt }}</el-button>
    </el-col>
    <el-col :span="8">
      <el-button type="danger" :icon="VideoPause" @click="stopRecord" > {{ startTxt }}</el-button>
    </el-col>
    <el-col :span="8" v-if="false">
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
import { ref, onMounted, reactive } from 'vue'
import { ElMessageBox, ElMessage } from 'element-plus'
import {
    VideoPlay,
    VideoPause,
    VideoCamera,
} from '@element-plus/icons-vue'
// https://blog.csdn.net/weixin_41727824/article/details/107707949

const startTxt = ref('开始录制')
const pauseTxt = ref('暂停')
const start = ref(null)
const isPause = ref(false)
const recorder = reactive({})
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

const startRecording = (callback) => {
    if (startTxt.value==='开始录制') {
        captureScreen((screenStream)=> {
            addStreamStopListener(screenStream, ()=>{
                console.log("流停止监听");
                stopRecord()
            })
            isPause.value = true;
            startTxt.value = '完成录制'
            let options = {
                type: 'video',
                mimeType: 'video/mp4',
                disableLogs: false, // 日志开关,
                getNativeBlob: false,
                ignoreMutedMedia: false,
            }
            recorder.value = RecordRTC(screenStream, options)
            recorder.startRecording()
            recorder.screen = screenStream
            videoStart = true
            callback(true)
        })
    } else if (startTxt.value === "完成录制") {
        stopRecord();
    }
}

const stopRecording = () => {
    recorder && recorder.stopRecording(()=> {

    })
}
//初始化录制
const captureScreen = () => {

}

//流监听
const addStreamStopListener = (stream, callback) => {

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