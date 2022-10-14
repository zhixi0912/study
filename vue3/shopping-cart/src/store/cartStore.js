import {defineStore} from 'pinia'

const useCartStore = defineStore('cartStore', {
    state() {
        return {
            cartList: []
        }
    },
    actions: {
        addToCart(producet){
            // console.log('producet--->', producet)
            const p = this.cartList.find((item)=>{
                return item.id === producet.id
            })
            if(p){
                p.quantity ++
                const cartProduct = producet.hasOwnProperty('quantity')
                if (!cartProduct) {
                    p.inventory --
                }
            } else {
                let inventory = producet.inventory
                inventory --
                this.cartList.push({
                    ...producet,
                    inventory: inventory,
                    quantity: 1 //购物车里商品数量+1
                })
            }
            producet.inventory --
        },
        reduceToCart(producet){
            // console.log('reduce--->', producet)
            const p = this.cartList.find((item)=>{
                return item.id === producet.id
            })
            if(p){
                p.quantity --
                p.inventory ++
                if (p.quantity < 1) {
                    let newCartList = new Set(this.cartList)
                    newCartList.delete(producet)
                    this.cartList = [...newCartList]
                }
            }
        }
    },
    getters: { //pinia的计算属性
        toAllPrice(){
            return this.cartList.reduce((sum, item)=>{
                sum += item.price * item.quantity
                return sum
            },0)
        }
    }
})
export default useCartStore