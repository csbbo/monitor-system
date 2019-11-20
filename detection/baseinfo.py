#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
import socket
from datetime import datetime
import psutil
import re
import defense

    
# CPU信息
def get_cpu_info():
    cpu_count = psutil.cpu_count()
    top = os.popen("top -n 1 | grep %Cpu").read()
    top = top.split('\n')[0]
    m = re.search(r'%Cpu\(s\):.*(\d\.\d).*mus,.*',top)
    # if int(m.group(1)) > 95:
    #     defense.shutdow()
    return dict(cpu_count = cpu_count,cpu_percent=m.group(1))

# 内存信息
def get_memory_info():
    virtual_mem = psutil.virtual_memory()

    mem_total = round(virtual_mem.total/(1024.0*1024.0*1024.0), 2)
    mem_percent = virtual_mem.percent
    mem_used = round(mem_total * mem_percent / 100,2)
    mem_free = round(mem_total-mem_used,2)
    mem_total = str(mem_total)+'G'
    mem_used = str(mem_used)+'G'
    mem_free = str(mem_free)+'G'
    if mem_percent > 95:
        defense.shutdow()
    return dict(mem_total=mem_total,mem_percent=mem_percent,
        mem_free=mem_free,mem_used=mem_used)

# 磁盘信息
def get_disk_info():
    disk_usage = psutil.disk_usage('/')

    disk_total = round(disk_usage.total/(1024.0*1024.0*1024.0),2)
    disk_percent = disk_usage.percent
    disk_used = round(disk_total*disk_percent/100,2)
    disk_free = round(disk_total-disk_used,2)
    disk_total = str(disk_total)+'G'
    disk_free = str(disk_free)+'G'
    disk_used = str(disk_used)+'G'

    return dict(disk_total=disk_total,disk_percent=disk_percent,
            disk_free=disk_free,disk_used=disk_used)

# 开机时间
def get_boot_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return dict(boot_time=boot_time)

# 总信息
def collect_monitor_data():
    data = {}
    hostname = socket.gethostname()
    data.update(dict(hostname=hostname))
    data.update(get_boot_info())
    data.update(get_cpu_info())
    data.update(get_memory_info())
    data.update(get_disk_info())
    return data

if __name__ == '__main__':
    print(collect_monitor_data())