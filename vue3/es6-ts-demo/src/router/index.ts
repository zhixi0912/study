import { createRouter, createWebHashHistory } from 'vue-router'

export const constantRoutes = [

  {
    path: '/',
    redirect: '/login',
    children: [
      {
        path: 'login',
        component: () => import('../views/login/index.vue'),
        name: 'login',
      },
      {
        path: "401",
        component: () => import("@/views/error-page/401.vue"),
        meta: { hidden: true },
      },
//      {
//        path: "404",
//        component: () => import("@/views/error-page/404.vue"),
//        meta: { hidden: true },
//      }
    ]
    
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('../views/home/index.vue')
  },
  {
    path: '/clock',
    name: 'clock',
    component: () => import('../views/clock/index.vue')
  },

  {
    path: '/user',
    name: 'user',
    component: () => import('../views/user/index.vue')
  },
  {
    path: '/:catchAll(.*)',
    name: '404',
    meta: { hidden: true },
    component: () => import("@/views/error-page/404.vue"),
  }
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
