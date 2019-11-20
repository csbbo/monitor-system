<template>
    <div class="ports">
        <div class="portshead">
            <h2>Openning Ports</h2>
        </div>
        <table class="table table-hover">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">Number</th>
                <th scope="col">Detail</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(port,index) in ports">
                    <th scope="row">{{index+1}}</th>
                    <td>{{port.port}}</td>
                    <td>{{port.detail}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data(){
        return{
            ports:[]
        }
    },
    created:function(){
        let url = this.GLOBAL.host+"ports/"
        this.$http({
            url:url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            console.log(res.body)
            this.ports = res.body
        },function(err){

        })
    }
}
</script>

<style scoped>
.portshead{
    margin-bottom: 60px;
}
tbody tr:hover{
    background-color: black;
}
</style>