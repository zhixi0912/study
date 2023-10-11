<script setup lang="ts">
import { ref, onMounted } from 'vue'



const dialogVisible = ref(false)
defineProps<{ msg: string }>()

const count = ref(0)
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








onMounted(() => {
  //  startRecord();
});
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
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

<style scoped>
.read-the-docs {
  color: #888;
}
.vido-box {
  min-height: 300px;
}
</style>
