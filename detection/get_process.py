#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import subprocess

pattern = re.compile(r'([a-zA-z|\-|_]*).*(\d+\.\d+)')
top_cpu_cmd = "dstat --top-cpu 1 20 | grep '^[a-z]\{2,\}'"
top_mem_cmd = "dstat --top-cpu 1 20 | grep '^[a-z]\{2,\}'"

def top_cpu():
    temp = []
    try:
        mci = subprocess.check_output(top_cpu_cmd,shell=True).decode('utf-8')
        mci_list = mci.split('\n')
        mci_list = mci_list[:-1]
        for s in mci_list:
            m = pattern.search(s)
            temp.append(dict(cpu_name=m.group(1),cpu_use=m.group(2)))
    except:
        pass
    return temp

def top_mem():
    temp = []
    try:
        mci = subprocess.check_output(top_mem_cmd,shell=True).decode('utf-8')
        mci_list = mci.split('\n')
        mci_list = mci_list[:-1]
        for s in mci_list:
            m = pattern.search(s)
            temp.append(dict(mem_name=m.group(1),mem_use=m.group(2)))
    except:
        pass
    return temp

if __name__ == '__main__':
    print(top_cpu())
    print(top_mem())