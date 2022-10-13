import {defineStore} from 'pinia'

const useCounterStore  = defineStore('counterStore',{
    state(){
        return {
            count: 0,
            title: 'hello world'
        }
    },
    actions: {
        add(){
            this.count ++
        }
    }
})

export default useCounterStore