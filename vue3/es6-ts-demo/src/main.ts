import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import { useLocalStorage } from '@vueuse/core'
import App from './App.vue'
import router from './router'
import VueFullPage from 'vue-fullpage.js'
import 'element-plus/dist/index.css'
import 'uno.css'
import 'animate.css';
import 'vue-fullpage.js/dist/style.css'

const app = createApp(App)
// const userInfo = useLocalStorage('userInfo')
// console.log('userInfo------------>', JSON.parse(userInfo.value))

// if (userInfo.value !== undefined || userInfo.value !== 'undefined') {
//     console.log('userInfo------1------>', userInfo.value)
//     let data = JSON.parse(userInfo.value)
//     if (data.id) {
//         app.use(ElementPlus)
//         console.log('userInfo------2------>', data.id)
//     }
// }
app.use(createPinia())
app.use(router)
app.use(VueFullPage)
// app.use(ElementPlus)
app.mount('#app')
