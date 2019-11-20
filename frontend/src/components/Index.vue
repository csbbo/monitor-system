<template>
<div class="index">
    <nav class="navbar navbar-light bg-light">
    <router-link class="navbar-brand" to="/">服务器入侵检测警报系统</router-link>
    <div>
        <span v-show="this.$store.state.islogin" class="username">{{this.$store.state.username}}</span>
        <router-link to="/login" v-show="!this.$store.state.islogin" class="floatright">登录</router-link>
        <a v-show="this.$store.state.islogin" v-on:click="logout" class="logout">注销</a>
    </div>
    </nav>

    <div class="maincontent">
        <router-view></router-view>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return{
            // islogin: this.$store.state.islogin,
            // uname: this.$store.state.username
        }
    },
    methods: {
        logout: function(){
            localStorage.clear()
            this.$store.commit('logout')
            this.$router.push('/')
        }
    }
}
</script>


<style scoped>
.navbar{
    background-color: #333 !important;
    overflow: hidden;
}
.navbar .navbar-brand{
    font-size: 1.4em;
    color: #ffffff;
}
.navbar .navbar-brand:hover{
    color: #ffffff;
}
.navbar .username{
    color: #e2dfe7a1;
    margin-right: 18px;
}
.navbar .floatright{
    text-decoration: none;
    color: #e2dfe7a1;
}
.navbar .floatright:hover{
    color: #ffffff;
}
.navbar .logout{
    text-decoration: none;
    color: #e2dfe7a1;
}
.navbar .logout:hover{
    color: #ffffff;
}
input{
    border-radius: 0%;
}
</style>

<style>
body{
    width: 100%;
    height: 100%;
    background-color: #252830;
}
</style>

