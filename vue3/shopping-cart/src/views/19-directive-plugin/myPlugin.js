import Abc from './Abc.vue'

export default {
    install(app, options){
        app.component('Abc', Abc)
        app.mixin({
            mounted(){
    
            },
            data(){
                return {
                    title: 'aaa'
                }
            }
        })
    }
}