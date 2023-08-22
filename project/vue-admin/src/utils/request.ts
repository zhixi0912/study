import axios from 'axios';
// import { useUserStoreHook } from '@/store/modules/user';

// 创建 axios 实例
const service = axios.create({
    baseURL: import.meta.env.VITE_APP_BASE_API,
    timeout: 50000,
    headers: { 'Content-Type': 'application/json;charset=utf-8' }
});

// 请求拦截器
service.interceptors.request.use(
async config => {
    // 每次发送请求之前判断vuex中是否存在token
    // 如果存在，则统一在http请求的header都加上token，这样后台根据token判断你的登录情况
    // 即使本地存在token，也有可能token是过期的，所以在响应拦截器中要对返回状态进行判断
    // config.headers.token = sessionStorage.getItem('token')
    return config;
},
error => {
    return Promise.error(error);
})

// 响应拦截器
service.interceptors.response.use(
    (response) => {
        if (response.status === 200) {
            return Promise.resolve(response); //进行中
        } else {
            return Promise.reject(response); //失败
        }
    },
    (error: any) => {
        if (error.response.status) {
            console.log('error.response--------------->', error.response)
        //     const { code, msg } = error.response.data;
        //     // token 过期，跳转登录页
        //     if (code === 'A0230') {
        //         ElMessageBox.confirm('当前页面已失效，请重新登录', '提示', {
        //             confirmButtonText: '确定',
        //             type: 'warning'
        //         }).then(() => {
        //             localStorage.clear(); // @vueuse/core 自动导入
        //             window.location.href = '/';
        //         });
        //     }else{
        //         ElMessage.error(msg || '系统出错');
        //     }
        }
        return Promise.reject(error.message);
    }
);

// 导出 axios 实例
export default service;