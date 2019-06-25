#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !author:bruce chou


# def fn(a,b,*c):
#     print(a)
#     print(b)
#     print(c)
#
# mytuple = (1, 2, 3, 4)
#
# fn(1,mytuple)

# class MyClass():
#     pass
#
# mc = MyClass()
# result = isinstance(mc,MyClass)
# print(result, end="")
# print(123)
# print(type(mc))
# print(type(MyClass))


def begin_end(fun):
    def wrapper(*args,**kwargs):
        print("this is begin:")
        fun(*args,**kwargs)
        print("this is end")
    return wrapper


@begin_end
def fun(a,b):
    print(a+b)
    print("this is fun()!")


# print("{var}this is my life[{other}]".format(var="变量",other="其他"))

print('%sadfg'%'ad')


class Person:
    def __init__(self,name,age,nation):
        self.__name = name
        self.__age = age
        self._nation = nation

    def getAge(self):
        print("age is",self.__age)

    def getName(self):
        print("name is",self.__name)

    def setAge(self,age):
        self.__age = age

    def setName(self,name):
        self.__name = name

    @property
    def nation(self):
        print("nation method return the nation")
        return self._nation

    @nation.setter
    def nation(self,nation):
        self._nation = nation


person = Person('zzt',22,'China')
person.setAge(18)
person.setName("bruce")
person._Person__age = 23
person._Person__name = 'Bruce'
person.getAge()
person.getName()
print(person.nation)
person.nation = 'USA'
print(person.nation)

print(Person.__bases__)

print(2**36)


class Dog:
    def __init__(self,name,age,sex):
        self._name = name
        self._age = age
        self._sex = sex

    #  实例方法
    def test(self):
        print("这是实例方法test")


    #  类方法
    @classmethod
    def test2(cls):
        print("这是类方法test2")

    #  静态方法
    @staticmethod
    def test3():
        print("这是静态方法test3")


if __name__=='__main__':
    d = Dog("wangzai",4,"male")
    d.test()
    d.test2()
    d.test3()
    #Dog.test()
    Dog.test2()
    Dog.test3()

