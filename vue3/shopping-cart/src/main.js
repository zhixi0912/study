import { createApp } from 'vue'
// import './style.css'
import { createPinia } from 'pinia'
import App from './App.vue'
// import router from './router'
import GlobalComponents from './views/12-components/GlobalComponents.vue'

const app = createApp(App)
// app.use(router)
app.component('GC',GlobalComponents)
app.use(createPinia())
app.mount('#app')
