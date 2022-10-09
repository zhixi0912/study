import {defineStore} from 'pinia'

const useCounterStore  = defineStore('counterStore',{
    state(){
        return {
            count: 0
        }
    }
})

export default useCounterStore