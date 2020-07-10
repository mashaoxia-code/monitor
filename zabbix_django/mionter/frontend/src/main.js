import Vue from 'vue'
import App from './App.vue'
import router from './router'

// elementui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import './assets/css/style.css'

Vue.use(ElementUI)

Vue.config.productionTip = false

import publicFunc from './api/public'//引用
Vue.use(publicFunc);//将全局函数当做插件来进行注册

// 路由守卫
router.beforeEach((to, from, next) => {
  if (to.path == "/login") {
    next()
    return
  }
  if (localStorage.getItem('token')) {
    next()
  } else {
    next({
      path: '/login',
      query: { redirect: to.fullPath }
    })
  }
})
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
