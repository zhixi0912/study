<template>
    <div v-if="cartList.length > 0 && cartStore.toAllPrice > 0">
        <h2>购物车</h2>
        <hr>{{cartList}}
        <ul>
            <template v-for="item in cartList">
                <li v-if="item.quantity >= 1" class="car-shop">
                    {{item.name}} ￥{{item.price}} x <button @click="reduceToCartClick(item)" :disabled="item.quantity < 1">-</button><input type="number" :value="item.quantity" @input="handlechange" /><button @click="addToCartClick(item)" :disabled="item.inventory <= 0">+</button> = ￥{{item.price * item.quantity}}
                </li>
            </template>
        </ul>
        <hr>
        <h4 class="all">总价：￥{{cartStore.toAllPrice}}</h4>
    </div>
</template>

<script setup>
import {storeToRefs} from 'pinia'
import useCartStore from '@/store/cartStore';
import useProducetStore from '@/store/producetStore';
const producetStore = useProducetStore()
const { producets } = storeToRefs(producetStore)

const cartStore = useCartStore()
const { addToCart, reduceToCart } = useCartStore()
const {cartList} = storeToRefs(cartStore)

const handlechange = (e)=>{
    // console.log('--->',e.target.value)
}
const reduceToCartClick = (p)=>{
    reduceToCart(p)
    producetStore.updateProduces(p)
}
const addToCartClick = (p) =>{
    addToCart(p)
    producetStore.updateProduces(p)
}
</script>

<style lang="css">
.car-shop{

}
.car-shop button{
    margin: 0 5px;
    cursor: pointer;
}
.all{
    text-align: right;
    color: red;
}
</style>