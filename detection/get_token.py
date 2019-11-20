#!/usr/bin/python
# -*- coding: UTF-8 -*-
token_path = './token.txt'

def get_token():
    with open(token_path,'r') as f:
        token = f.read()
    return token

if __name__ == '__main__':
    print('get the token from '+token_path)
    print(get_token())