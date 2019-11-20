<template>
    <div class="baseinfo">
        <!-- <button v-on:click="test">button</button> -->
        <div class="boot-time">
            开机时间
            <br>
            {{detail.boot_time}}
        </div>
        <div class="overview">
            <h6>DASHBOARDS</h6>
            <h2>Overview</h2>
        </div>
        <hr>
        <div class="servername">
            主机名:{{detail.hostname}}
        </div>
        <div class="cpu-counts">
            cpu核数: {{detail.cpu_count}}
        </div>
        <div class="rates">
            <div class="rate cpu-rate">
                <p>CPU使用率</p>
                <div class="get-rate">
                    {{detail.cpu_percent}}%
                </div>
            </div>
            <div class="rate mem-rate">
                <p>内存使用率</p>
                <div class="get-rate">
                    {{detail.mem_percent}}%
                </div>
            </div>
            <div class="rate disk-rate">
                <p>磁盘使用率</p>
                <div class="get-rate">
                    {{detail.disk_percent}}%
                </div>
            </div>
        </div>
        <hr class="memhr">
        <table class="table table-hover">
            <!-- On rows -->
            <tr>
            <td class="bg-primary">#</td>
            <td class="bg-success">内存</td>
            <td class="bg-danger">磁盘</td>
            </tr>
            <tr>
            <td class="bg-primary">使用量</td>
            <td class="bg-success">{{detail.mem_used}}</td>
            <td class="bg-danger">{{detail.disk_used}}</td>
            </tr>
            <tr>
            <td class="bg-primary">剩余量</td>
            <td class="bg-success">{{detail.mem_free}}</td>
            <td class="bg-danger">{{detail.disk_free}}</td>
            </tr>
            <tr>
            <td class="bg-primary">总大小</td>
            <td class="bg-success">{{detail.mem_total}}</td>
            <td class="bg-danger">{{detail.disk_total}}</td>
            </tr>
        </table>
    </div>
</template>


<script>
export default{
    data(){
        return{
            detail: []
        }
    },
    methods: {
        test: function(){
            let url = this.GLOBAL.host+"base/"
            this.$http({
                url:url,
                method:'GET',
                headers:{
                    'token':localStorage.token
                }
            }).then(function(res){
                console.log(res.body)
                this.detail = res.body
            },function(err){
            })
        }
    },
    created: function(){
        let url = this.GLOBAL.host+"base/"
        if(localStorage.token === ''){
            this.$router.push('/')
        }
        this.$http({
            url:url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            console.log(res.body)
            this.detail = res.body
        },function(err){

        })
    }
}
</script>

<style scoped>
.baseinfo{
    overflow:hidden;
}
.boot-time{
    color: #ffffff;
    background-color: #ffc107;
    padding: 5px;
    float: right;
    border-radius: 5px;
}
.overview h6{
    color: #434857;
    font-size: 12px;
}
.baseinfo hr{
    border-top: 1px solid #434857;
    clear: both;
}
.servername{
    background-color: #17a2b8;
    padding: 10px;
    float: left;
    border-radius: 5px;
    margin-right: 10px;
}
.cpu-counts{
    background-color: #17a2b8;
    padding: 10px;
    float: left;
    border-radius: 5px;
}
.rates{
    margin-top: 100px;
}
.rates .rate{
    width: 25%;
    height: 150px;
    background: rgba(0, 0, 255, 0.39);
    float: left;
    border-radius: 3px;
    padding: 20px;
    text-align: center;
}
.rates .rate p{
    font-size: 20px;
}
.rates .rate .get-rate{
    font-size: 45px;
}
.rates .mem-rate{
    margin: 0% 12%;
    background-color: #dc3545;
}
.rates .cpu-rate{
    background-color: #28a745;
}
.rates .disk-rate{
    background-color: #6610f2;
}
.memhr{
    margin-top: 310px;
}
.table{
    text-align: center;
    margin-top: 40px;
}
</style>
