import { ref, onMounted, onUpdated  } from 'vue';
const userTitle =(count)=>{
    onMounted(()=>{
        document.title = count.value
     })
     onUpdated(()=>{
        document.title = count.value
     })
}
export default userTitle