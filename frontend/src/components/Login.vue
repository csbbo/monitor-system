<template>
<div class="m-login">
    <div class="login-pane">
        <div class="login-header">
            <h2 class="modal-title" id="exampleModalLongTitle">登录</h2>
        </div>
        <form onSubmit="text();">
        <div class="form-group">
            <label for="formGroupExampleInput">Username</label>
            <input type="text" class="form-control" ref="username" required="required" placeholder="Username">
        </div>
        <div class="form-group">
            <label for="formGroupExampleInput2">Password</label>
            <input type="password" class="form-control" ref="password" required="required" placeholder="Password">
        </div>
        <button v-on:click="login" @click.prevent="onSubmit" class="submit btn">Login</button>
        </form>
        <div class="login-footer">
            <div v-show="loginerr" class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>警告!</strong> 账号或密码错误.
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default{
    data(){
        return{
            loginerr: false
        }
    },
    methods:{
        login: function(){
            let url = this.GLOBAL.host+"login/"
            let data = new FormData()
            data.append('username',this.$refs.username.value)
            data.append('password',this.$refs.password.value)
            this.$http({
                url:url,
                method:'POST',
                body:data
            }).then(function(res){
                if(res.body.code === 1000){
                    localStorage.token = res.body.token
                    localStorage.username = res.body.username
                    localStorage.loginstatue = true
                    this.$store.commit('login')
                    this.$router.push('/base')
                }
                else{
                    this.loginerr = true
                }
            },function(err){
            })
        }
    }
}
</script>

<style scoped>
.login-pane{
    margin: 120px auto;
    width: 520px;
    border-radius: 0%;
    background-color: rgb(39, 39, 39);
    color: #ffffff;
}
.login-header{
    border: none;
    border-radius: 0%;
    background-color: #333;
    text-align: center;
    padding: 20px 0;
}
.login-footer{
    border: none;
    border-radius: 0%;
    background-color: #333;
    height: 80px;
}
form{
    padding: 20px 10px;
}
form input{
    margin-bottom: 40px;
    border-radius: 0%;
}
form .submit{
    background-color: #333;
    color: #ffffff;
    font-size: 20px;
}
form .submit:hover{
    background-color: black;
}

.alert{
    margin: 0px 20px;
}
</style>
