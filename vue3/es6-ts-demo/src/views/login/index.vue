<template>
  <button type="primary" @click="login">登录</button>
</template>
<script setup lang="ts">
import {getCurrentInstance, reactive} from 'vue'
// import { useLocalStorage } from '@vueuse/core'
import router from "@/router";
import { ElButton } from 'element-plus'
import ElementPlus from "@/utils/element";
const { appContext } = getCurrentInstance()

const login = () => {
  const userInfo = reactive({
    id: '01',
    name: '小明',
    token: 'qwert12345'
  })
  // useLocalStorage('userInfo', userInfo)
  appContext.app.use(ElementPlus)
  // setTimeout(()=>{
  //   console.log(appContext.app)
  //   router.push('/user')
  // },2000)
  router.push('/user')
}
</script>