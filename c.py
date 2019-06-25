#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !author:bruce chou

from hello import b
import sys
import pprint
print(sys.modules)
pprint.pprint(sys.modules)
pprint.pprint(sys.path)

filename = 'g:/hello.txt'
# filename = 'hello.txt'

try:
    with open(filename, encoding='utf-8') as fileobj:
        print(fileobj.read())
except FileNotFoundError:
    print(f'{filename}''文件不存在')



def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        print ('Prepare and say...',)
        func(*args, **kwargs)
        print('heool everyone')
        return func
    return wrapper  # 返回

@debug
def say(something):
    print ("hello {}!".format(something))

say("zzt")

