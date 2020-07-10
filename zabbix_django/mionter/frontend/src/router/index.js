import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    redirect: '/sbmonitor',  //默认的路由
    children: [
      {
        path: '/sbmonitor',
        name: 'sbmonitor',
        redirect: '/host1',
        component: () => import('../views/Home/Sbmonitor.vue'),
        children: [
          {
            path: '/host1',
            name: 'host1',
            component: () => import('../views/Home/host1.vue')
          },
          {
            path: '/host2',
            name: 'host2',
            component: () => import('../views/Home/host2.vue')
          },
          {
            path: '/host3',
            name: 'host3',
            component: () => import('../views/Home/host3.vue')
          },
        ]
      },
      {
        path: '/sysmonitor',
        name: 'sysmonitor',
        component: () => import('../views/Home/Sysmonitor.vue')
      },
      {
        path: '/warning',
        name: 'warning',
        component: () => import('../views/Home/warning.vue')
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/Login.vue')
  },
  {
    path: '/detail/:hostid',
    name: 'detail',
    redirect: '/detail/:hostid/:applyid',
    component: () => import(/* webpackChunkName: "about" */ '../views/Detail/detail.vue'),
    children: [
      {
        path: '/detail/:hostid/:applyid',
        name: 'item',
        component: () => import('../views/Detail/item.vue')
      },
    ]
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
