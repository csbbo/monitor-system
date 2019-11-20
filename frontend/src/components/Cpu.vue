<template>
    <div class="cpu">

        <div class="cpuhead">
            <h2>Cpu And Process</h2>
        </div>
        <table class="table table-hover">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">Application</th>
                <th scope="col">Usage Rate</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(cpu,index) in cpus">
                    <th scope="row">{{index+1}}</th>
                    <td>{{cpu.cpu_name}}</td>
                    <td>{{cpu.cpu_use}}%</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data(){
        return{
            cpus:[]
        }
    },
    created:function(){
        let url = this.GLOBAL.host+"cpu/"
        this.$http({
            url:url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            console.log(res.body)
            this.cpus = res.body
        },function(err){

        })
    }
}
</script>


<style scoped>
.cpuhead{
    margin-bottom: 60px;
}
tbody tr:hover{
    background-color: black;
}
</style>
