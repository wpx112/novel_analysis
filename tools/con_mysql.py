# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql


# 从测试服获取数据
def create_con():
    con = pymysql.Connect(
        host='120.79.36.32',
        port=3306,
        user='www_802k_cn',
        password='ksxGX8QfWipYte5z',
        db='www_802k_cn',
        charset='utf8'
    )
    return con


#测试用本地数据库连接
def create_con2():
    con = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        db='dbt',
        charset='utf8'
    )
    return con


#将sql语句写入对应的库中
def insert_to_db(sql):
    con = create_con2()
    cursor = con.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交数据
        con.commit()
    except:
        print("Error: 插入数据时出错")
        con.rollback()
    # 关闭数据库连接
    con.close()

def judge_new_user(stime,sql1):
    sql = "SELECT * FROM {0} WHERE day_t='{1}'".format("new_user",stime)
    print(sql)
    con = create_con2()
    cursor = con.cursor()
    jug = cursor.execute(sql)
    if jug:
        del_sql = "DELETE FROM {0} WHERE day_t='{1}'".format("new_user",stime)
        print('存在，开始删除')
        try:
            # 执行SQL语句
            cursor.execute(del_sql)
            print(del_sql)
            cursor.execute(sql1)
            # 提交数据
            con.commit()
        except:
            print("Error: 删除数据时出错")
            con.rollback()
        # 关闭数据库连接
        con.close()
    else:
        print('不存在，开始插入')
        try:
            cursor.execute(sql1)
            con.commit()
        except:
            print("Error: 插入数据时出错")
            con.rollback()
        # 关闭数据库连接
        con.close()
