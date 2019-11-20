#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess

def kill_ssh_process(virterminal):
    cmd = 'pkill -kill -t '+virterminal
    subprocess.call(cmd,shell=True)

def deny_bad_ip(ip_addr):
    cmd_find_ip = "grep '%s' /etc/hosts.deny" % ip_addr
    ip_exist = subprocess.call(cmd_find_ip,shell=True) #if the command execute sucess return 0 or return 1
    if ip_exist == 1:           
        cmd = "echo 'sshd : %s' >> /etc/hosts.deny" % ip_addr
        subprocess.call(cmd,shell=True)

def shutdow():
    cmd = "shutdown now"
    subprocess.call(cmd,shell=True)