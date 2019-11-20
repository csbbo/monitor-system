#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re


def scan_port():
    rep1 = []
    rep2 = []
    open_list = []
    try:
        open_ports = os.popen("nmap 127.0.0.1 | grep '^[0-9]\{2,5\}.*'").read()
        open_list = open_ports.split('\n')[:-1]
    except Exception as e:
        pass

    for p in open_list:
        reg_exp = re.search(r'([0-9]{2,5})/(.*)',p)
        rep1.append(dict(port=reg_exp.group(1),detail=reg_exp.group(2)))
        rep2.append(reg_exp.group(1))
    rep2 = ",".join(rep2)
    return rep1,rep2

if __name__ == '__main__':
    print(scan_port())