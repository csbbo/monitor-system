<template>
    <div class="mem">
        <div class="memhead">
            <h2>Mem And Process</h2>
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
                <tr v-for="(mem,index) in mems">
                    <th scope="row">{{index+1}}</th>
                    <td>{{mem.mem_name}}</td>
                    <td>{{mem.mem_use}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data(){
        return{
            mems:[]
        }
    },
    created:function(){
        let url = this.GLOBAL.host+"mem/"
        this.$http({
            url:url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            console.log(res.body)
            this.mems = res.body
        },function(err){

        })
    }
}
</script>


<style scoped>
.memhead{
    margin-bottom: 60px;
}
tbody tr:hover{
    background-color: black;
}
</style>

