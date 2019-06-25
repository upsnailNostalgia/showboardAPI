#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !author:bruce chou

#  print('aaa')

#  列表切片
students = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'] * 2
print(students[:])

print('aaa' in students)
print('aaa' not in students)
print(min(students))
print(max(students))
print(students.index('eee'))
print(students.insert(1, '123'))
print(students)
print(students.sort())
students[0:0] = "123456"
print(students)
count =0
for s in students:
    print(s)
    count+=1
print(count)
print(len(students))

mytuple = (1,2,3)
mytuple = 4,2
# 解包，解构
a=100
b=200
print(a,b)
a, b = b, a
print(a, b)
print(mytuple)
print(type(mytuple))

d = {1: a, 2: b, 3: 'c'}
print(d, type(d))

dic = dict([('name','zzt'),('age',22)])
print(dic)

#  浅复制，会简单复制对象内部的值


for i in range(3,12,2):
    print(i)



