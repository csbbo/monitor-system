#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from multiprocessing import Process
import os
import time
import sys
import signal

# 引入本地模块
import settings
import regist                   #注册
import get_token                 #获取token
import baseinfo                 #系统基本信息
import get_process               #进程信息
import open_port                 #检查端口
import sha256_file                 #检查文件
import login_ip                 #登录ip
import defense

host = settings.HOST_DOMAIN
headers = {'token':get_token.get_token()}

# 退出监测系统
def quit(signum,frame):
    # print('\nServer monitoring system stopped\n')
    sys.exit()

# 是否开启Debug模式
def is_debug(r):
    if settings.DEBUG_INFO:
        try:
            print(r.json())
        except Exception as e:
            print(e)

# 非DeBug模式打印的信息
def background_running():
    if not settings.DEBUG_INFO:
        print(' Compiled successfully')
        print(' Programming is running')
        print(' Test message sent to %s' % host)

# 基本信息
def post_baseinfo():
    url = host+'server/baseinfo/'
    data=baseinfo.collect_monitor_data()
    r = requests.post(url,headers=headers,data=data)
    is_debug(r)

# 消耗CPU高的进程
def post_top_cpu():
    url = host+'server/topcpu/'
    for i in get_process.top_cpu():
        data = i
        r = requests.post(url,headers=headers,data=data)
        is_debug(r)

# 消耗Mem高的进程
def post_top_mem():
    url = host+'server/topmem/'
    for i in get_process.top_mem():
        data = i
        r = requests.post(url,headers=headers,data=data)
        is_debug(r)

# 开放的端口
def post_open_port():
    url = host+'server/openport/'
    ports,port_list = open_port.scan_port()
    for i in ports:
        data = i
        r = requests.post(url,headers=headers,data=data)
        is_debug(r)

    url = host+'server/openport_list/'
    r = requests.post(url,headers=headers,data={'port_list':port_list})

# 文件散列值
def post_sha256_file():
    url = host+'server/shafile/'
    for i in sha256_file.getFileHash():
        data = i
        r = requests.post(url,headers=headers,data=data)
        is_debug(r)

# 登录成功的IP
def post_success_ip():
    url = host+'server/successip/'
    for i in login_ip.success_ip():
        data = i
        r = requests.post(url,headers=headers,data=data)
        is_debug(r)

# 登录失败的IP
def post_faile_ip():
    url = host+'server/faileip/'
    for i in login_ip.faild_ip():
        data = i
        r = requests.post(url,headers=headers,data=data)
        try:
            text = r.json()
            if text['code'] == 1004:
                defense.deny_bad_ip(text['ip_addr'])
        except Exception as e:
            pass
        is_debug(r)

if __name__ == '__main__':
    background_running()
    signal.signal(signal.SIGINT,quit)       # 键盘中 Ctrl-C 组合键信号
    signal.signal(signal.SIGTERM,quit)      # 命令行数据 kill pid 时的信号
    while True:
        post_baseinfo()
        post_open_port()
        post_sha256_file()
        post_success_ip()
        post_faile_ip()
        
        p1 = Process(target=post_top_cpu)
        p2 = Process(target=post_top_mem)
        p1.start()
        p2.start()
        p1.join()
        p2.join()

