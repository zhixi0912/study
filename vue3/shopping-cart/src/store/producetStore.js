import { defineStore } from "pinia";
import axios from 'axios'
const useProducetStore = defineStore('producetStore', {
    state() {
        return {
            producets: []
        }
    },
    actions: {
        async loadData() {
            //安装一个node服务工具来模拟接口功能 //npm i json-server -g
            //json-server查看工具命令
            //json-server ./src/data/api.json -p 9000 //运行定义好的json文件 及访问端口
            //http://localhost:9000/data   浏览器中通过该地址访问定义好的json数据
            let result = await axios.get('http://localhost:9000/data')
            // console.log('data---->', result.data)
            this.producets = result.data

            // axios.post('http://localhost:9000/data', '{id: 5, name: "iphone15", price: 1200,inventory:2}')
            //json-server服务可以通过post请求向json插入一条数据,但每次个性json数据后需求重启服务才能更新页面数据
        },
        updateProduces(producet) {
            const p = this.producets.find((item)=>{
                return item.id === producet.id
            })
            if(p){
                p.inventory = producet.inventory
            }
        }
    }
})
export default useProducetStore