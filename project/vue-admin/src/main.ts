import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { setupStore } from '@/store';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import '@/styles/index.scss'
import 'uno.css'

const app = createApp(App)
// 全局注册 状态管理(store)
setupStore(app);
app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.mount('#app')
