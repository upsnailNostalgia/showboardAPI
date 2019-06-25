#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !author:bruce chou

from flask import Flask, jsonify
import pymysql
import datetime

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello world!"

# @app.route("/user/<username>")
# def show_username(username):
#     return 'User %s' % username


@app.route("/repobasicinfo/<days>/")
def show_basicInfo(days):

    '''
    该函数基本信息新增的数量(一日内，七日内，一月内)
    :param days:
    :return:
    '''
    nowTime = datetime.datetime.now()
    beforeTime_str = (nowTime-datetime.timedelta(int(days))).strftime('%Y-%m-%d %H:%M:%S')
    conn = getConnection()
    cursor = conn.cursor()
    sql_select = "select count(*) from repository_java where crawl_time > '"+ beforeTime_str +"'"
    result = getCount(sql_select)
    return result


@app.route("/repoclone/<days>/")
def get_repoClone(days):
    '''
    该函数用来获取项目clone的情况（一日内，七日内，一月内）
    :param days:
    :return:
    '''
    nowTime = datetime.datetime.now()
    beforeTime_str = (nowTime - datetime.timedelta(int(days))).strftime('%Y-%m-%d %H:%M:%S')
    sql_select = "select count(*) from repository_java where scan_time > '"+ beforeTime_str +"'"

    result = getCount(sql_select)
    return result

@app.route("/totalbasic/")
def getTotalBasic():
    '''
    该函数用来获取总共爬取了多少repo的基础信息
    :return:
    '''
    sql_select = "select count(*) from repository_java"
    result = getCount(sql_select)
    return result

@app.route("/totalclone/")
def getTotalClone():
    '''
    该函数用来获取总共服务器上有多少repo
    :return:
    '''
    sql_select = "select count(*) from repository_java where is_downloaded=1"
    result = getCount(sql_select)
    return result


@app.route("/repocloneinfo/")
@app.route("/repocloneinfo/<int:page>/")
def getRepoCloneInfo(page=1):
    '''
    该函数用来得到已经clone的repo的基本信息情况
    :return:
    '''
    start = str((int(page)-1)*15)

    sql_select = "select repos_name,owner_name,git_address,pushed_at,scan_time from repository_java where is_downloaded=1 limit "+start+",15"
    result = getRepoInfo(sql_select)
    # data = {}
    index = 0
    repoData = []
    print(result)
    for repoObject in result:
        data = {}
        data['repos_name'] = repoObject[0]
        data['owner_name'] = repoObject[1]
        data['git_address'] = repoObject[2]
        data['pushed_at'] = repoObject[3]
        data['scan_time'] = repoObject[4]
        repoData.append(data)
    return str(repoData)

def getRepoInfo(sql_select):
    '''
    该函数用来获取repo的基础信息情况
    :return:
    '''
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(sql_select)
    rs = cursor.fetchall()
    repos = []
    for each in rs:
        tuple_each = ()
        if each[3] is None:
            tuple_each = each[0:3] + ('', each[4].strftime('%Y-%m-%d %H:%M:%S'))
        else:
            tuple_each = each[0:3] + (each[3].strftime('%Y-%m-%d %H:%M:%S'),each[4].strftime('%Y-%m-%d %H:%M:%S'))
        print(tuple_each)
        repos.append(tuple_each)

    return repos

def getCount(sql_select):
    '''
    该函数返回select的搜索数量
    :param sql_select:
    :return:
    '''
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(sql_select)
    rs = cursor.fetchone()
    cursor.close()
    conn.close()
    return str(rs[0])

def getConnection():
    '''
    该函数用来得到数据库连接的connection
    :return:返回connection
    '''
    # conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='zzt123456', db='github', charset='utf8')
    conn = pymysql.Connect(host='10.141.221.85', port=3306, user='root', passwd='root', db='github', charset='utf8')
    return conn


def getRepoFromMysql():
    conn = getConnection()
    cursor = conn.cursor()

    sql = "select * from repository_java limit 1,100"
    cursor.execute(sql)
    print("cursor.rowcount=",cursor.rowcount)
    rs = cursor.fetchone()
    print("rs fetch one:",rs)
    for each in cursor.fetchmany(2):
        print("===fetch many===")
        print(each)
    print("=======================")
    for each in cursor.fetchall():
        print("===fetch all===")
        print(each)
        print(type(each))

    cursor.close()
    conn.close()

def testFun():
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    print(now_str)
    yestarday = now - datetime.timedelta(1)
    yestarday_str = yestarday.strftime('%Y-%m-%d %H:%M:%S')
    print(yestarday)
    print(yestarday_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    # getRepoFromMysql()
    # testFun()
    # getRepoCloneInfo()