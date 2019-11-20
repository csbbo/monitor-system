#!/usr/bin/python
# -*- coding: UTF-8 -*-

IF_LOCAL = False

if IF_LOCAL == True:
    HOST_DOMAIN = 'http://127.0.0.1:8000/'
else:
    HOST_DOMAIN = 'https://monitor.shaobo.fun/'

DEBUG_INFO = True        # if open Debug mode

SHA256_FILE = [
                '/etc/passwd','/etc/group','/etc/nginx/nginx.conf',
                '/etc/mysql/my.cnf','/home/chen/.bashrc',
                '/home/chen/.zshrc','/var/log/wtmp','/home/chen/.bash_history'
            ]