# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


# 从日志库中获取数据
def create_con_r():
    con = pymysql.Connect(
        host='120.79.36.32',
        port=3306,
        user='www_802k_cn',
        password='ksxGX8QfWipYte5z',
        db='novel_analysis',
        charset='utf8'
    )
    return con


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


# 测试用本地数据库连接
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


# 将sql语句写入对应的库中
def insert_to_db(sql):
    con = create_con_r()
    cursor = con.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交数据
        con.commit()
    except Exception as e:
        print(e, "Error: 插入数据时出错")
        con.rollback()
    # 关闭数据库连接
    con.close()


def judge_insert(stime,sql1,table_name):
    sql = "SELECT * FROM {0} WHERE day_t='{1}'".format(table_name, stime)
    del_sql = "DELETE FROM {0} WHERE day_t='{1}'".format(table_name, stime)
    con = create_con_r()
    cursor = con.cursor()
    jug = cursor.execute(sql)
    if jug:
        try:
            # 执行SQL语句
            print('存在，开始删除,并重新插入')
            cursor.execute(del_sql)
            print(del_sql)
            cursor.execute(sql1)
            # 提交数据
            con.commit()
        except Exception as e:
            print(e, "Error: 删除数据时出错")
            con.rollback()
    else:
        print('不存在，开始插入')
        try:
            cursor.execute(sql1)
            con.commit()
        except Exception as e:
            print(e, "Error: 插入数据时出错")
            con.rollback()
    con.close()


# json存入数据库中
def save_upadate(stime,sql,table_name):
    sql1 = "SELECT id FROM {0} WHERE day_t='{1}'".format(table_name, stime)
    con = create_con_r()
    cursor = con.cursor()
    jug = cursor.execute(sql1)
    if jug:
        try:
            print('已存在，开始更新')
            cursor.execute(sql)
            con.commit()
            print('已存在，更新成功')
        except Exception as e:
            con.rollback()
            print(e, '已存在，更新失败')
    else:
        insert_sql = 'INSERT INTO {table_name} (day_t) VALUES ("{stime}")'.format(table_name=table_name, stime=stime)
        try:
            print('开始插入')
            cursor.execute(insert_sql)
            cursor.execute(sql)
            con.commit()
            print('插入成功')
        except Exception as e:
            con.rollback()
            print(e, '插入失败')
    con.close()


# 将数据插入recharge表
def insert_to_recharge(stime,k,v):
    s = "SELECT * FROM aa_recharge WHERE day_t='{stime}' AND money = {k}"
    ssql = s.format(stime=stime, k=k)
    con = create_con_r()
    cursor = con.cursor()
    jug = cursor.execute(ssql)
    if jug:
        try:
            u = "UPDATE aa_recharge SET num = {v} WHERE day_t='{stime}' AND money = {k}"
            usql = u.format(stime=stime, k=k, v=v)
            # 执行SQL语句
            print('存在,并重新跟新')
            cursor.execute(usql)
            # 提交数据
            con.commit()
        except Exception as e:
            print(e, "Error: 删除数据时出错")
            con.rollback()
    else:
        print('不存在，开始插入')
        try:
            sqll = "insert into aa_recharge(day_t,money,num) values('{day_t}',{f_v1},{f_v2})".format(f_v1=k, f_v2=v,
                                                                                                     day_t=stime)
            cursor.execute(sqll)
            con.commit()
        except Exception as e:
            print(e, "Error: 插入数据时出错")
            con.rollback()
    con.close()


# 将数据插入aa_phone表
def insert_to_phone(stime,k,v):
    s = "SELECT * FROM aa_phone WHERE day_t='{stime}' AND phone = '{k}'"
    ssql = s.format(stime=stime, k=k)
    print(ssql)
    con = create_con_r()
    cursor = con.cursor()
    jug = cursor.execute(ssql)
    if jug:
        try:
            u = "UPDATE aa_phone SET num = {v} WHERE day_t='{stime}' AND phone = '{k}'"
            usql = u.format(stime=stime, k=k, v=v)
            # 执行SQL语句
            print('存在,并重新跟新')
            cursor.execute(usql)
            # 提交数据
            con.commit()
        except Exception as e:
            print(e, "Error: 删除数据时出错")
            con.rollback()
    else:
        print('不存在，开始插入')
        try:
            sqll = "insert into aa_phone(day_t,phone,num) values('{day_t}','{f_v1}',{f_v2})".format(f_v1=k, f_v2=v,
                                                                                                    day_t=stime)
            cursor.execute(sqll)
            con.commit()
        except Exception as e:
            print(e, "Error: 插入数据时出错")
            con.rollback()
    con.close()


def insert_to_operating(stime,k,v):
    s = "SELECT * FROM aa_operating WHERE day_t='{stime}' AND op = '{k}'"
    ssql = s.format(stime=stime, k=k)
    print(ssql)
    con = create_con_r()
    cursor = con.cursor()
    jug = cursor.execute(ssql)
    if jug:
        try:
            u = "UPDATE aa_operating SET num = {v} WHERE day_t='{stime}' AND op = '{k}'"
            usql = u.format(stime=stime, k=k, v=v)
            # 执行SQL语句
            print('存在,并重新跟新')
            cursor.execute(usql)
            # 提交数据
            con.commit()
        except Exception as e:
            print(e, "Error: 删除数据时出错")
            con.rollback()
    else:
        print('不存在，开始插入')
        try:
            sqll = "insert into aa_operating(day_t,op,num) values('{day_t}','{f_v1}',{f_v2})".format(f_v1=k, f_v2=v,
                                                                                                     day_t=stime)
            cursor.execute(sqll)
            con.commit()
        except Exception as e:
            print(e, "Error: 插入数据时出错")
            con.rollback()
    con.close()