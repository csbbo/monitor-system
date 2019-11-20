<template>
    <div class="emailsetting">
        <div class="emailhead">
            <h2>邮件警报</h2>
        </div>
        <div class="iplist">
            <ul>
                <li>
                    <span>基本信息邮件提醒</span>
                    <button v-on:click="mod_base" class="mbtn" v-bind:class="{close_email:baseinfocss}">{{baseinfostatue}}</button>
                </li>
                <li>
                    <span>CPU邮件提醒</span>
                    <button v-on:click="mod_cpu" class="mbtn" v-bind:class="{close_email:cpucss}">{{cpustatue}}</button>
                </li>
                <li>
                    <span>内存邮件提醒</span>
                    <button v-on:click="mod_mem" class="mbtn" v-bind:class="{close_email:memcss}">{{memstatue}}</button>
                </li>
                <li>
                    <span>端口邮件提醒</span>
                    <button v-on:click="mod_port" class="mbtn" v-bind:class="{close_email:portcss}">{{portstatue}}</button>
                </li>
                <li>
                    <span>重要文件邮件提醒</span>
                    <button v-on:click="mod_file" class="mbtn" v-bind:class="{close_email:filecss}">{{fielstatue}}</button>
                </li>
                <li>
                    <span>登录成功IP邮件提醒</span>
                    <button v-on:click="mod_successip" class="mbtn" v-bind:class="{close_email:successipcss}">{{successipstatue}}</button>
                </li>
                <li>
                    <span>登录失败IP邮件提醒</span>
                    <button v-on:click="mod_failip" class="mbtn" v-bind:class="{close_email:failipcss}">{{failipstatue}}</button>
                </li>

                <li>
                    <span>异地登录</span>
                    <button v-on:click="newip" class="mbtn" v-bind:class="{close_email:newipcss}">{{newipstatue}}</button>
                </li>
                <li>
                    <span>IP异常停留</span>
                    <button v-on:click="login_ip_stay" class="mbtn" v-bind:class="{close_email:loginipcss}">{{loginipstatue}}</button>
                </li>
                <li>
                    <span>操作记录被删除</span>
                    <button v-on:click="file_deleted" class="mbtn" v-bind:class="{close_email:historyfilecss}">{{historyfilestatue}}</button>
                </li>
            </ul>
        </div>
        <div class="guide">
            <h5>操作指南:</h5>
            <i>按钮背景为蓝色表示该项邮箱为开启状态,可点击进行关闭邮箱.当按钮背景颜色为灰色时表示邮箱处于关闭状态,可点击进行开启</i>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            open:'关闭',
            close:'开启',
            baseinfostatue:'',
            cpustatue:'',
            memstatue:'',
            portstatue:'',
            fielstatue:'',
            successipstatue:'',
            failipstatue:'',
            newipstatue:'',
            loginipstatue:'',
            historyfilestatue:'',
            
            baseinfocss:false,
            cpucss:false,
            memcss:false,
            portcss:false,
            filecss:false,
            successipcss:false,
            failipcss:false,
            newipcss:false,
            loginipcss:false,
            historyfilecss:false,
        }
    },
    methods:{
        // 基本信息
        mod_base:function(){
            let base_url = this.GLOBAL.host+"base_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.baseinfostatue = this.open
                    this.baseinfocss = false
                }else{
                    this.baseinfostatue = this.close
                    this.baseinfocss = true
                }
            },function(err){

            })
        },
        // cpu
        mod_cpu:function(){
            let base_url = this.GLOBAL.host+"cpu_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.cpustatue = this.open
                    this.cpucss = false
                }else{
                    this.cpustatue = this.close
                    this.cpucss = true
                }
            },function(err){

            })
        },
        // 内存
        mod_mem:function(){
            let base_url = this.GLOBAL.host+"mem_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.memstatue = this.open
                    this.memcss = false
                }else{
                    this.memstatue = this.close
                    this.memcss = true
                }
            },function(err){

            })
        },
        // 端口
        mod_port:function(){
            let base_url = this.GLOBAL.host+"ports_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.portstatue = this.open
                    this.portcss = false
                }else{
                    this.portstatue = this.close
                    this.portcss = true
                }
            },function(err){

            })
        },
        // 文件
        mod_file:function(){
            let base_url = this.GLOBAL.host+"files_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.fielstatue = this.open
                    this.filecss = false
                }else{
                    this.fielstatue = this.close
                    this.filecss = true
                }
            },function(err){

            })
        },
        // 登录成功IP
        mod_successip:function(){
            let base_url = this.GLOBAL.host+"successip_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.successipstatue = this.open
                    this.successipcss = false
                }else{
                    this.successipstatue = this.close
                    this.successipcss = true
                }
            },function(err){

            })
        },
        // 登录失败IP
        mod_failip:function(){
            let base_url = this.GLOBAL.host+"faileip_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.failipstatue = this.open
                    this.failipcss = false
                }else{
                    this.failipstatue = this.close
                    this.failipcss = true
                }
            },function(err){

            })
        },
        // 入侵

        // 异地登录
        newip:function(){
            let base_url = this.GLOBAL.host+"intrusionnewip_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.newipstatue = this.open
                    this.newipcss = false
                }else{
                    this.newipstatue = this.close
                    this.newipcss = true
                }
            },function(err){

            })
        },
        // 文件异常
        file_deleted:function(){
            let base_url = this.GLOBAL.host+"intrusionfile_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.historyfilestatue = this.open
                    this.historyfilecss = false
                }else{
                    this.historyfilestatue = this.close
                    this.historyfilecss = true
                }
            },function(err){

            })
        },
        // IP登录时间过长
        login_ip_stay:function(){
            let base_url = this.GLOBAL.host+"intrusionip_email/"
            this.$http({
                url:base_url,
                method:'PUT',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                if(res.body.email === true){
                    this.loginipstatue = this.open
                    this.loginipcss = false
                }else{
                    this.loginipstatue = this.close
                    this.loginipcss = true
                }
            },function(err){

            })
        },
    },
    created:function(){
        let base_url = this.GLOBAL.host+"base_email/"
        let cpu_url = this.GLOBAL.host+"cpu_email/"
        let mem_url = this.GLOBAL.host+"mem_email/"
        let ports_url = this.GLOBAL.host+"ports_email/"
        let files_url = this.GLOBAL.host+"files_email/"
        let successip_url = this.GLOBAL.host+"successip_email/"
        let faileip_url = this.GLOBAL.host+"faileip_email/"

        let new_ip = this.GLOBAL.host+"intrusionnewip_email/"
        let login_ip = this.GLOBAL.host+"intrusionip_email/"
        let file = this.GLOBAL.host+"intrusionfile_email/"
        // 基本信息
        this.$http({
            url:base_url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.baseinfostatue = this.open
                this.baseinfocss = false
            }else{
                this.baseinfostatue = this.close
                this.baseinfocss = true
            }
        },function(err){

        })
        // cpu
        this.$http({
            url:cpu_url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.cpustatue = this.open
                this.cpucss = false
            }else{
                this.cpustatue = this.close
                this.cpucss = true
            }
        },function(err){

        })  
        // 内存
        this.$http({
            url:mem_url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.memstatue = this.open
                this.memcss = false
            }else{
                this.memstatue = this.close
                this.memcss = true
            }
        },function(err){

        }) 
        // 端口
        this.$http({
            url:ports_url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.portstatue = this.open
                this.portcss = false
            }else{
                this.portstatue = this.close
                this.portcss = true
            }
        },function(err){

        }) 
        // 文件
        this.$http({
            url:files_url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.fielstatue = this.open
                this.filecss = false
            }else{
                this.fielstatue = this.close
                this.filecss = true
            }
        },function(err){

        }) 
        // 登录成功ip
        this.$http({
            url:successip_url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.successipstatue = this.open
                this.successipcss = false
            }else{
                this.successipstatue = this.close
                this.successipcss = true
            }
        },function(err){

        }) 
        // 登录失败ip
        this.$http({
            url:faileip_url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.failipstatue = this.open
                this.failipcss = false
            }else{
                this.failipstatue = this.close
                this.failipcss = true
            }
        },function(err){

        }) 
        // 入侵

        // 异地登录
        this.$http({
            url:new_ip,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.newipstatue = this.open
                this.newipcss = false
            }else{
                this.newipstatue = this.close
                this.newipcss = true
            }
        },function(err){

        }) 
        // IP长时间停留
        this.$http({
            url:login_ip,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.loginipstatue = this.open
                this.loginipcss = false
            }else{
                this.loginipstatue = this.close
                this.loginipcss = true
            }
        },function(err){

        }) 
        // 重要文件被删除
        this.$http({
            url:file,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            if(res.body.email === true){
                this.historyfilestatue = this.open
                this.historyfilecss = false
            }else{
                this.historyfilestatue = this.close
                this.historyfilecss = true
            }
        },function(err){

        }) 
    }
}
</script>

<style scoped>
.emailhead{
    margin-bottom: 60px;
}
.iplist ul{
    padding: 0%;
    margin: 0%;
}
.iplist ul li{
    padding: 5px 5px;
    list-style: none;
    overflow: hidden;
}
.iplist ul li .mbtn{
    float: right;
    background-color: #007bff;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    padding: 8px 22px;
}
.iplist ul li .mbtn:hover{
    box-shadow: 1px 1px 5px blue;
}
.guide{
    border: 1px solid #ffffff;
    padding: 15px;
    margin-top: 100px;
}

.close_email{
    background-color: #545b62 !important;
    box-shadow: none !important;
}
</style>
