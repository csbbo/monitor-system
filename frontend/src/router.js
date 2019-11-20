import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './components/Home'
import Info from './components/Info'
import Login from './components/Login'
import NotFound from './components/404'

import BaseInfo from './components/BaseInfo'
import Cpu from './components/Cpu'
import Mem from './components/Mem'
import Files from './components/Files'
import Ports from './components/Ports'
import SuccessIP from './components/SuccessIP'
import FailIP from './components/FailIP'
import EmailSetting from './components/EmailSetting'
import SmsSetting from './components/SmsSetting'

Vue.use(VueRouter)

const routes = [
    {path:'/',component:Home},
    {path:'/login',component:Login},
    {path:'/404',component:NotFound},
    {path:'/info',redirect:'/base',component:Info,children:[
      {path:'/base',component:BaseInfo},
      {path:'/cpu',component:Cpu},
      {path:'/mem',component:Mem},
      {path:'/files',component:Files},
      {path:'/ports',component:Ports},
      {path:'/success_ip',component:SuccessIP},
      {path:'/fail_ip',component:FailIP},
      {path:'/email_setting',component:EmailSetting},
      {path:'/sms_setting',component:SmsSetting},
    ]},
    {path:'*',redirect:'/404'},
]

export default new VueRouter({
  routes,
  mode:'hash'
})