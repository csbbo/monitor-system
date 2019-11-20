#!/usr/bin/python
# -*- coding: UTF-8 -*-
import getpass
import re
from termcolor import *
import requests

import settings

host = settings.HOST_DOMAIN

# 获取用户名，邮箱，密码
def get_info():
    username = input("Username:")
    while True:
        email  = input("Email address:")
        if re.match(r'.{1,30}@[0-9a-zA-Z]+.com',email):
            while True:
                passwd = getpass.getpass('Password:')
                passwd2 = getpass.getpass('Password (again):')
                if passwd == passwd2:
                    break
                print(colored("Error: Your passwords didn't match.","red"))
            break
        print(colored("Error: Enter a valid email address.","red"))
    return username,email,passwd

# 注册账号
def regist():
    url = host+'server/regist/'
    username,email,password = get_info()
    data = {'username':username,'password':password,'email':email}
    try:
        r = requests.post(url,data=data)
        text = r.json()
        if r.status_code == 200:
            if text['code'] == 1000:
                print("\nRegist success!")
                print(text)
                token = text.get('token')
                with open('./token.txt','w') as f:     #写入token
                    f.write(token)
            else:
                print(text)
        else:
            print("该用户名已经被使用!!!")
            
    except Exception as e:
        print("Sorry: Server is not response...")

if __name__ == '__main__':
    print(host)
    regist()