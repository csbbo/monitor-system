import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        username:localStorage.username,
        islogin: localStorage.loginstatue
    },
    mutations:{
        login(state){
            state.username = localStorage.username
            state.islogin = localStorage.loginstatue
        },
        logout(state){
            localStorage.clear()
            state.username = '',
            state.islogin = false
        }
    }
})