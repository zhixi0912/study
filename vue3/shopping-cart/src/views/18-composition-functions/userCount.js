import {ref} from 'vue'
const userCount = ()=>{
    const count = ref(0)
    const handelClick = () => {
        count.value ++
    }
    return {
        count,
        handelClick
    }
}
export default userCount