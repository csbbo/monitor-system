<template>
    <div class="files">
        <div class="fileshead">
            <h2>Sha256 Important Files</h2>
        </div>
        <table class="table table-hover">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">File Path</th>
                <th scope="col">Sha256 Value</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(file,index) in files">
                    <th scope="row">{{index+1}}</th>
                    <td>{{file.filepath}}</td>
                    <td>{{file.sha256}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data(){
        return{
            files:[]
        }
    },
    created:function(){
        let url = this.GLOBAL.host+"files/"
        this.$http({
            url:url,
            method:'GET',
            headers:{
                'token':localStorage.token
            }
        }).then(function(res){
            console.log(res.body)
            this.files = res.body
        },function(err){

        })
    }
}
</script>

<style scoped>
.fileshead{
    margin-bottom: 60px;
}
tbody tr:hover{
    background-color: black;
}
</style>