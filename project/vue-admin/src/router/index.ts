import { createRouter, createWebHashHistory } from 'vue-router'

export const constantRoutes = [
    {
        path: '/',
        name: 'login',
        component: () => import('@/views/login/index.vue')
    },
]


const router = createRouter({
    history: createWebHashHistory(),
    routes: constantRoutes,
    // 刷新时，滚动条位置还原
    scrollBehavior: () => ({ left: 0, top: 0 }),
});


export function resetRouter() {
    router.replace({ path: "/login" });
}
// 重置路由
export default router