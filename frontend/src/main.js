import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'

import router from './router'
import store from './store'
import global from './global'

Vue.use(VueResource)

Vue.config.productionTip = false

Vue.prototype.GLOBAL = global

// 全局守卫
router.beforeEach((to,from,next)=>{
    if(store.state.islogin === false){
        if(to.path == '/login' || to.path == '/' || to.path == '/404'){
            next()
        }
        else{
            alert('还没有登录,请先登录!')
            next('/login')
        }
    }
    else{
        next()
    }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
