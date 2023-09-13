import { defineStore } from 'pinia'

export const useFoldSideberStore = defineStore('setting', {
    state: () => {
        return {
            isCollapse: false
        }
    },
    getters: {
        
    },
    actions: {
        foldSideber(isCollapse) {
            return this.isCollapse = !isCollapse
        }
    }
})