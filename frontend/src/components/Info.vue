<template>
    <div class="leftnavbar">
        
        <div class="verticalnav">
            <i class="fa fa-pagelines" style="font-size:36px"></i>
            <ul class="navbtn">
                <li class="ct">Resource</li>
                <li><router-link to="/base">Resource Utilization</router-link></li>
                <li class="ct">Top Process</li>
                <li><router-link to="/cpu">CPU</router-link></li>
                <li><router-link to="/mem">Mem</router-link></li>
                <li class="ct">Login Ip</li>
                <li><router-link to="/success_ip">Success</router-link></li>
                <li><router-link to="/fail_ip">Fail</router-link></li>
                <li class="ct">Other</li>
                <li><router-link to="/files">Important Files</router-link></li>
                <li><router-link to="/ports">Opening Ports</router-link></li>
                <li class="ct">Settings</li>
                <li><router-link to="/email_setting">Email</router-link></li>
                <li><router-link to="/sms_setting">SMS</router-link></li>
            </ul>
            <hr class="hrbottom">
        </div>
        <div class="maincontent">
            <router-view></router-view>
        </div>
    </div>
</template>

<style scoped>
.leftnavbar{
    color: #ffffff;
    margin: 2% 16%;
    overflow: hidden;
}
/* 左边导航 */
.verticalnav{
    float: left;
    width: 20%;
}
.verticalnav i{
    color: #51586a;
    margin-left: 12px;
}
.verticalnav i:hover{
    color: #f8f9fa;
}
.verticalnav .navbtn{
    margin: 20px 0%;
    padding: 0%;
}
.verticalnav .navbtn li{
    margin: 0%;
    margin-bottom: 8px;
    padding: 0%;
}
.verticalnav .navbtn .ct{
    padding: 5px 12px;
    color: #51586a;
    text-transform: uppercase;
}
.verticalnav .navbtn li a{
    display: block;
    width: 100%;
    text-decoration: none;
    color: #ffffff8a;
    padding: 8px 12px;
}
.verticalnav .navbtn li a:hover{
    background-color: #1997c6;
    color: #ffffff;
}
.verticalnav .hrbottom{
    margin-top: 30px;
    border-top: 1px solid #434857;
}


/* 右边内容 */
.maincontent{
    margin-left: 23%;
}
</style>
