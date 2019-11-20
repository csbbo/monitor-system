<template>
<div class="homepage">
    <!-- 轮播图 -->
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
    </ol>
    <div class="carousel-inner">
        <div class="carousel-item active">
        <img class="d-block w-100" src="../assets/images/carousel/3.jpg" alt="First slide">
        </div>
        <div class="carousel-item">
        <img class="d-block w-100" src="../assets/images/carousel/2.jpg" alt="Second slide">
        </div>
        <div class="carousel-item">
        <img class="d-block w-100" src="../assets/images/carousel/1.jpg" alt="Third slide">
        </div>
        <div class="carousel-item">
        <img class="d-block w-100" src="../assets/images/carousel/6.jpg" alt="Four slide">
        </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
    </div> 
    <!-- 介绍文本   -->
    <div class="introduce">
        <div class="introduce-sys">
            <div class="intitle">
                <h5>系统简介</h5>
            </div>
            <hr>
            <p>本项目基于Linux操作平台和Web服务器，通过shell脚本自动化编程，
            对非法入侵服务器用户进程动态监控。通过检测用户操作行为，收集异
            常进程信息，监听日志、常用端口访问情况，封锁试图通过ssh登陆的
            异常IP等手段，收集被判定为非法入侵的用户和进程的操作信息</p>
        </div>
        <div class="background">
            <h5 id="bg_bg" v-on:click="background" v-bind:class="{activetable:bg_isactivate}">研究背景</h5>
            <h5 id="bg_main" v-on:click="main_content" v-bind:class="{activetable:main_isactivate}">主要内容</h5>
            <hr>
            <p>{{message}} </p>
        </div>
    </div>
    <!-- 表格 -->
    <table class="table">
        <tbody>
        <tr>
            <td class="table_td">
                <div class="photo" :style="{'background-image':'url('+img1+')'}"><p>支持多终端查看信息</p></div>  
            </td>
            <td class="table_td">
                <div class="photo" :style="{'background-image':'url('+img2+')'}"><p>以绿色纯净为宗旨</p></div>  
            </td>
            <td class="table_td">
                <div class="photo" :style="{'background-image':'url('+img3+')'}"><p>最及时警报信息</p></div>  
            </td>
        </tr>
        <tr>
            <td class="table_td">
                <div class="photo" :style="{'background-image':'url('+img4+')'}"><p>一个为安全而生的平台</p></div>  
            </td>
            <td class="table_td">
                <div class="photo" :style="{'background-image':'url('+img5+')'}"><p>用户自主控制</p></div>  
            </td>
            <td class="table_td">
                <div class="photo" :style="{'background-image':'url('+img6+')'}"><p>完善的多端处理</p></div>  
            </td>
        </tr>
        </tbody>
    </table> 


    <!-- item -->
    <div class="allitem">
        <div class="item_title">
            <h2>创新特色</h2>
        </div>
        <div class="upitem">
            <div class="item"><div class="icons"><img src="../assets/images/footer/8.png" alt=""></div><p>切合痛点</p></div>
            <div class="item"><div class="icons"><img src="../assets/images/footer/6.png" alt=""></div><p>系统纯净</p></div>
            <div class="item"><div class="icons"><img src="../assets/images/footer/7.png" alt=""></div><p>技术新颖</p></div>
            <div class="item"><div class="icons"><img src="../assets/images/footer/5.png" alt=""></div><p>分级检测</p></div>
        </div>
        <div class="downitem">
            <div class="item"><div class="icons"><img src="../assets/images/footer/2.png" alt=""></div><p>三级警报</p></div>
            <div class="item"><div class="icons"><img src="../assets/images/footer/4.png" alt=""></div><p>高效及时</p></div>
            <div class="item"><div class="icons"><img src="../assets/images/footer/3.png" alt=""></div><p>多方防卫</p></div>
            <div class="item"><div class="icons"><img src="../assets/images/footer/1.png" alt=""></div><p>全自动化</p></div>
        </div>
    </div>
    <!-- footer -->
    <div class="footer">
        <div class="words"><span>© 2018 shaobo.fun</span><span>桂ICP备 17011922号</span></div>
    </div>
</div>
</template>

<script>
import img1 from '../assets/images/middle/2.jpg'
import img2 from '../assets/images/middle/1.jpg'
import img3 from '../assets/images/middle/3.jpg'
import img4 from '../assets/images/middle/6.jpg'
import img5 from '../assets/images/middle/4.jpg'
import img6 from '../assets/images/middle/8.jpg'
var m = {message_bg : '随着互联网技术高速发展，海量的信息在因特网上传输。基于C/S(Client to Server)架构的请求响应模式使用尤为广泛。但也因此也带来了一些严峻的问题，服务器如果遭受入侵，运维工程师未能及时处理，可能会导致用户信息的泄露，服务器遭受恶意破坏，用户无法正常使用服务等问题。\
            我们的项目正是基于这些问题所研发的入侵检测系统，将所检测到的可疑、非法、恶意破坏信息发送给服务器管理人员，帮助服务器管理人员及时高效的进行漏洞修补和防火墙的加固。',
            message_main : '研究Linux操作系统，sha256等散列函数，通过对Linux系统中文件散列值的计算实现文件监控\
            研究Linux进程服务，查看所有进程信息，分析异常进程信息,\
            研究ssh传输协议，通过监控ssh登陆信息封锁异常IP,  \
            常进程信息，监听日志、常用端口访问情况，封锁试图通过ssh登陆的,   \
            研究web服务器的搭建、前端用户界面的设计开发、数据库设计，完成各模块信息的交互。',}
export default{
    
    data(){
        return{
            // navimg:navimg, 
            message : m.message_bg,
            bg_isactivate:true,
            main_isactivate:false,
            img1: img1,
            img2: img2,
            img3: img3,
            img4: img4,
            img5: img5,
            img6: img6,
        }
    },
    methods:{
        background:function(){
            this.message = m.message_bg;
            this.bg_isactivate = true;
            this.main_isactivate = false;
        },
        main_content:function(){
            this.message = m.message_main;
            this.bg_isactivate = false;
            this.main_isactivate = true;
        },
    },
    created:function(){
        this.$store.commit('logout')
    }
}
</script>

<style scoped>
.carousel-inner{
    border: none;
}
.carousel-indicators{
    border: none;
}
/* introduce */
.introduce{
    color: #ffffff;
    overflow: hidden;
    margin: 60px auto;
    width: 1113px;
}
@media only screen and (max-width: 1113px){
    .introduce{
        width: 100%;
    }
}
.introduce-sys{
    width: 333px;
    height: 310px;
    float: left;
    padding: 20px;
    border: 8px solid #666666;
}
@media only screen and (max-width: 1113px){
    .introduce-sys{
        float: none;
        width: 100%;
        height: auto;
    }
}
.introduce-sys .intitle{
    text-align: center;
}
.introduce-sys hr{
    border-top: 1px solid #434857;
}
.background{
    margin-left: 370px;
    width: 742px;
    height: 310px;
    padding: 20px;
    border: 8px solid #666666;
    /* margin: 0%; */
}
@media only screen and (max-width: 1113px){
    .background{
        margin-top: 20px;
        width: 100%;
        margin-left:0%;
        height: auto;
    }
}
.background hr{
    margin-top: 29px;
    border-top: 1px solid #434857;
}
.background #bg_bg{
    float: left;
    padding-bottom: 4px;
    color: #ffffffc5;
}
.background #bg_main{
    float: left;
    padding-bottom: 4px;
    margin-left: 20px;
    color: #ffffffc5;
}
.activetable{
    color: #ffffff !important;
    border-bottom: 3px solid #ffffff;
}

/* table */
.table{
    color: #ffffff;
    border: none;
}
.table tr td{
    width: 33%;
    height: 300px;
    padding: 0%;
    text-align: center;
    vertical-align:bottom;
    border: 1px solid #00000018;
}
@media only screen and (max-width: 800px){
    .table tr td{
        height: 150px;
    }
}
.table td div{
    font-size: 20px;
    line-height: 300px;
    border: none;
    height: 100%;
    width: 100%;
}
@media only screen and (max-width: 1200px){
    .table td div{
        line-height: normal;
    }
}

/* item */
.allitem{
    color: #ffffff;
    width: 100%;
    margin-top: 40px;
    margin: 30px 0%;
    padding: 20px 15%;
}
.item_title{
    text-align: center;
    margin-bottom: 25px;
}
.upitem{
    width: 100%;
    overflow: hidden;
}
.downitem{
    width: 100%;
    clear: both;
    overflow: hidden;
    margin-top: 40px;
}
.item{
    width: 25%;
    float: left;
    text-align: center;
}
.item p{
    margin-top: 5px;
    color: #1997c6;
}
.icons{
    width: 105px;
    height: 105px;
    margin: auto;
}
.icons img{
    width: 100px;
    height: 100px;
    border-radius: 100%;
    border: 3px solid #1997c6;
    background-color: #ffffff;
}
.icons img:hover{
    border: 2px solid #1997c6;
}
/* footer */
.footer{
    background-color: #101010;
    padding: 20px 37%;
    color: #666666;
}
.footer span{
    margin: 0% 5%;
}
</style>
