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
    <el-col :span="8" v-if="startTxt !== '开始录制'">
      <el-button type="danger" :icon="VideoPause" @click="stopRecord" > {{ pauseTxt }}</el-button>
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
// https://juejin.cn/post/6992104922426654727
//https://juejin.cn/post/7072669600839630879

const startTxt = ref('开始录制')
const pauseTxt = ref('暂停')
const start = ref(false)
const isPause = ref(false)
const recorder = reactive({})
const startRecord = () => {
  let name = ref('开始视频录制')
  ElMessage({
      message: name.value,
      type: 'success'
  })
  console.log('测试开始----/------>',name.value,isPause.value)
  goBack(name)
}
const getTableData = () => {
  const data = [{name: '///'}]
  console.log(data)
}
const stopRecord = () => {
  start.value = true
  let msg = ref('停止视频录制')
    ElMessage({
        message: msg,
        type: 'success'
    })
    console.log('测试停止', msg)
  goBack(start)
}

const goBack = (val) => {
  let msg = '测试返回'
  console.log('测试返回',msg,start.value,val)
  start.value = false
  startRecording()
  getTableData()
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

const stopRecording = (callback) => {
    recorder && recorder.stopRecording(()=> {
        let fileName = getTimeIndex()
        const url = URL.createObjectURL(recorder.getBlob());
        let aTag = document.createElement("a")
        let videoFile = new File(
            [recorder.getBlob()],
            fileName + ".mp4",
            {
                type: "video/mp4",
            }
        );
        let downloadUrl = URL.createObjectURL(videoFile);
        document.body.appendChild(this.aTag);
        aTag.style.display = "none";
        aTag.href = url;
        videoFile = videoFile;
        let previewVideo = downloadUrl;
        // 停止录屏时同时下载到本地
        aTag.download = fileName + ".mp4";
        aTag.click();
        recorder.screen.stop();
        recorder.destroy();
        recorder = null;
        videoStart = false;
        ElMessage({
            message: "录屏停止",
            type: "success",
        });
        callback(false);
    })
}
//初始化录制
const captureScreen = () => {
    console.log("测试录屏效果")
    back(1)
}
const back = (id: Number) => {
    const data = 'yes'
    console.log('返回', id, data)
}
//流监听
const addStreamStopListener = (stream, callback) => {
    back(2)
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