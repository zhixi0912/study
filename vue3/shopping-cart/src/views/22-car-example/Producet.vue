<template>
    <div>
        <h1>产品列表</h1>
        <hr>
        <ul>
            <li v-for="item,index in producets" class="shop-box">
                <div><img :src="IphoneImg"/></div>
                <div>{{item.name}} -- ￥{{item.price}}  库存：{{item.inventory}}</div>
                <div><button @click="addToCart(item)" :disabled="item.inventory <= 0">加入购物车</button></div>
            </li>
        </ul>
        <Cart></Cart>
    </div>
</template>

<script setup>
 import { ref, onMounted, onBeforeMount } from 'vue';
 import IphoneImg from '../../../public/vite.svg'
 import {storeToRefs} from 'pinia'
 import Cart from './Cart.vue'
 import useProducetStore from '@/store/producetStore';
 import useCartStore from '@/store/cartStore'
 const producetStore = useProducetStore()
 const { producets } = storeToRefs(producetStore)
 const {addToCart} = useCartStore()
 onMounted(()=>{
    producetStore.loadData()
 })
 onBeforeMount(()=>{
    console.log('onBeforeMount')
 })
</script>

<style lang="css">
.shop-box{

}
.shop-box div{
    display: inline;
    margin: 0 10px;
}
</style>