import ElementPlus from 'element-plus'

export default {
    install: (app) => {
        app.config.globalProperties['ElementPlus'] = ElementPlus
    }
}