import { createApp } from 'vue'
// import './style.css'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './views/20-router/router'
import GlobalComponents from './views/12-components/GlobalComponents.vue'
import myDirective from './views/19-directive-plugin/myDirective'
import myPlugin from './views/19-directive-plugin/myPlugin'
 
const app = createApp(App)
app.use(router)
app.component('GC',GlobalComponents)
// app.directive('focus',myDirective) //19
// app.use(myPlugin, 'hello') //19
app.use(createPinia())
app.mount('#app')
