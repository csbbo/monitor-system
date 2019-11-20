<template>
    <div class="fialip">
        <div class="successip">
        <div class="iphead">
            <h2>Login Fail IP</h2>
        </div>
        <div class="iplist">
            <ul>
                <li class="head_info">
                    <span class="order">序号</span>
                    <span class="login_way">登录方式</span>
                    <span class="ipaddr">IP地址</span>
                    <span class="login_time">登录时间</span>
                    <span class="login_statu">登录状态</span>
                </li>
                <li class="item" v-for="(ip,index) in ips">
                    <span class="order">{{index+1}}</span>
                    <span class="login_way">{{ip.terminal_local}}</span>
                    <span class="ipaddr">{{ip.ip_addr}}</span>
                    <span class="login_time">{{ip.login_time}}</span>
                    <span class="login_statu">{{ip.login_statu}}</span>
                    <!-- <span>{{index+1}}</span>{{ip.ip_addr}} -->
                </li>
            </ul>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            ips:[]
        }
    },
    created:function(){
        let url = this.GLOBAL.host+"faileip/"
        this.$http({
            url:url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            console.log(res.body)
            this.ips = res.body
        },function(err){

        })
    }
}
</script>

<style scoped>
.iphead{
    margin-bottom: 60px;
}
.iplist ul{
    padding: 0%;
    margin: 0%;
}
.iplist ul li{
    padding: 8px 20px;
    margin: 10;
    list-style: none;
    border: 1px solid #ffffff;
}
.iplist ul li span{
    margin-right: 15px;
}
.iplist ul li:hover{
    background-color: #ffffff;
    color: black;
}
</style>
