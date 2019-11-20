<template>
    <div class="emailsetting">
        <div class="emailhead">
            <h2>短信警报</h2>
        </div>
        <div class="iplist">
            <ul>
                <li>
                    <span>基本信息短信提醒</span>
                    <button class="mbtn close_email">开启</button>
                </li>
                <li>
                    <span>CPU短信提醒</span>
                    <button class="mbtn close_email">开启</button>
                </li>
                <li>
                    <span>内存短信提醒</span>
                    <button class="mbtn close_email">开启</button>
                </li>
                <li>
                    <span>端口短信提醒</span>
                    <button class="mbtn close_email">开启</button>
                </li>
                <li>
                    <span>重要文件短信提醒</span>
                    <button class="mbtn close_email">开启</button>
                </li>
                <li>
                    <span>登录成功IP短信提醒</span>
                    <button class="mbtn close_email">开启</button>
                </li>
                <li>
                    <span>登录失败IP短信提醒</span>
                    <button class="mbtn close_email">开启</button>
                </li>
            </ul>
            
            <div style="margin-top:50px;" class="alert alert-warning alert-dismissible fade show" role="alert">
            <strong>提示!</strong> 短信功能尚未开启。
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
            </div>

        </div>
        <div class="guide">
            <h5>操作指南:</h5>
            <i>按钮背景为蓝色表示该项短信为开启状态,可点击进行关闭短信.当按钮背景颜色为灰色时表示短信处于关闭状态,可点击进行开启</i>
        </div>
    </div>
</template>

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
