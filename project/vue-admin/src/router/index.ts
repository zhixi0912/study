import { createRouter, createWebHashHistory } from 'vue-router'
export const Layout = () => import("@/layout/index.vue");
export const constantRoutes = [
    {
        path: '/login',
        name: 'login',
        component: () => import('@/views/login/index.vue')
    },
    {
        path: "/",
        component: Layout,
        meta: { hidden: true },
        children: [
            {
                path: "/dashboard",
                component: () => import("@/views/dashboard/index.vue"),
                meta: {
                    title: "dashboard",
                    icon: "homepage",
                    affix: true,
                    keepAlive: true,
                },
            },
            {
                path: "401",
                component: () => import("@/views/error-page/401.vue"),
                meta: { hidden: true },
            },
            {
                path: "404",
                component: () => import("@/views/error-page/404.vue"),
                meta: { hidden: true },
            }
        ],
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