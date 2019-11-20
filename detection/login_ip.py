#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
from datetime import datetime
import subprocess

import settings
import defense

login_stay_time = 30

# if the env is in the local
if settings.IF_LOCAL == True:
    success_shell_scrip = "cat local_ip_test.txt"
    faild_shell_scrip = "cat local_ip_test.txt"
else:
    success_shell_scrip = "last -20"
    faild_shell_scrip = "lastb -20"

pattern = re.compile(r'(\w+)\s+(\w+[/|:]\w+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([A-Z][a-z]{2})\s([A-Z][a-z]{2})\s+(\d{1,2})\s+(\d{2}:\d{2}).*((\(\d{2}:\d{2}\))|(still logged in))')

def success_ip():
    temp = []
    # login_ip = os.popen(success_shell_scrip).read()
    login_ip = subprocess.check_output(success_shell_scrip,shell=True).decode('utf-8')
    list_ip = login_ip.split('\n')
    list_ip = list(filter(None,list_ip))    #remove empty string
    if len(list_ip) < 21:
        list_ip = list_ip[0:-1]
    list_ip = list_ip[0:20]
    for n in list_ip:
        ip_extract = pattern.search(n)
        if ip_extract:
            login_statu=ip_extract.group(8) 
            login_statu_dev = ip_extract.group(8) 
            login_statu_dev = re.search(r'\((.*)\)',login_statu_dev)
            if login_statu_dev:
                login_statu = login_statu_dev.group(1)
            # there will be some defensive measures
            elif not settings.IF_LOCAL:
                nowdate = datetime.now().strftime('%Y:%m:%d:')
                login_time = nowdate+ip_extract.group(7)
                login_time = datetime.strptime(login_time,'%Y:%m:%d:%H:%M')
                print(datetime.now())
                print(login_time)
                stay_time = (datetime.now()-login_time).seconds / 60
                if stay_time > login_stay_time:
                    defense.kill_ssh_process(ip_extract.group(2))
            temp.append(dict(username=ip_extract.group(1),terminal_local=ip_extract.group(2),
                ip_addr=ip_extract.group(3),week=ip_extract.group(4),month=ip_extract.group(5),date=ip_extract.group(6),
                login_time=ip_extract.group(7),login_statu=login_statu))
    temp.reverse()
    return temp

def faild_ip():
    temp = []
    # login_ip = os.popen(faild_shell_scrip).read()
    login_ip = subprocess.check_output(faild_shell_scrip,shell=True).decode('utf-8')
    list_ip = login_ip.split('\n')
    list_ip = list(filter(None,list_ip))    #remove empty string
    if len(list_ip) < 21:
        list_ip = list_ip[0:-1]
    list_ip = list_ip[0:20]
    for n in list_ip:
        ip_extract = pattern.search(n)
        if ip_extract:
            login_statu=ip_extract.group(8) 
            login_time=ip_extract.group(8) 
            login_time = re.search(r'\((.*)\)',login_time)
            if login_time:
                login_statu = login_time.group(1)
            else:
                pass
            temp.append(dict(username=ip_extract.group(1),terminal_local=ip_extract.group(2),
                ip_addr=ip_extract.group(3),week=ip_extract.group(4),month=ip_extract.group(5),date=ip_extract.group(6),
                login_time=ip_extract.group(7),login_statu=login_statu))
    temp.reverse()
    return temp

if __name__ == '__main__':
    success_ip()
    print(success_ip())
    print(faild_ip())

