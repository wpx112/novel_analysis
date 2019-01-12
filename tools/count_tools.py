# !/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import time
import datetime
import pandas as pd
from tools.con_mysql import create_con_r

today = str(date.today())
# stime = '2019-01-09'
stime = today
sundry = 'aa_sundry'
table_Suffix = ''.join(stime.split('-'))
tab_name1 = 'dd_user_behavior'
tab_name = 'dd_user_behavior_' + table_Suffix

time1 = datetime.datetime.strptime(stime, "%Y-%m-%d").timetuple()
n_time = str(time1.tm_year) + '-' + str(time1.tm_mon) + '-' + str(time1.tm_mday)
n_time1 = str(time1.tm_year) + '-' + str(time1.tm_mon) + '-' + str(time1.tm_mday - 1)


def trend_hour(stime, s):
    """
    :param stime: 时间
    :param s: 一个时间序列的Series
    :return: 时间和数值的元祖
    """

    x = []
    y = []
    for i in range(24):
        st = "%02d" % i
        x.append(st)
        ss = stime + ' ' + st
        try:
            y.append(s[ss].count())
        except Exception as e:
            print(e)
            y.append(0)

    res = (x, y)
    return res


def change_time(t):
    """
    :param t: 时间戳
    :return: %Y-%m-%d %H:%M:%S格式的时间
    """
    time_stamp = t
    time_array = time.localtime(time_stamp)
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return other_style_time


def dataframe_s(result):
    s = pd.Series(result['user_id'], index=result.index)
    return s


def r_stime(st):
    sql = " SELECT day_t FROM `aa_sundry` WHERE day_t BETWEEN DATE_SUB('{time}', INTERVAL 30 DAY) AND '{time}'". \
        format(time=st)
    print(sql)
    con = create_con_r()
    try:
        cursor = con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        print(type(data))
        con.commit()
        return data
    except Exception as e:
        con.rollback()
        print(e, '查询失败')
    con.close()


def outer_chain():
    """
    返回外推小说名称用来映射小说名称
    :return: list
    """
    db = create_con_r()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    wt_sql = "SELECT DISTINCT ds.`anime_title` FROM `dd_chapter_statistics` ds WHERE FROM_UNIXTIME(ds.`shelf_time`," \
             "'%Y-%m-%d') > DATE_SUB('{stime}', INTERVAL 2 DAY) AND FROM_UNIXTIME(ds.`shelf_time`,'%Y-%m-%d') <= " \
             "'{stime}' AND ds.`style` =2".format(stime=stime)

    nt_sql = "SELECT DISTINCT anime_title FROM dd_chapter_statistics WHERE chapter_title = CONCAT('客服消息群发','{0}')" \
             " OR chapter_title =CONCAT('客服消息群发','{1}')".format(n_time, n_time1)
    print(wt_sql)
    print(nt_sql)
    w_t = []
    n_t = []
    try:
        # 执行SQL语句
        cursor.execute(wt_sql)
        # 获取所有记录列表
        wt_res = cursor.fetchall()
        cursor.execute(nt_sql)
        nt_res = cursor.fetchall()
        for i in range(len(wt_res)):
            w_t.append(wt_res[i][0])
        for i in range(len(nt_res)):
            n_t.append(nt_res[i][0])
    except Exception as e:
        print(e, "获取外推,内推数据失败")
    # 关闭数据库连接
    db.close()
    res = (w_t, n_t)
    return res


map_phone = {'Apple': 'Apple', 'KIW-AL10': 'Huawei', 'PRA-TL10': 'Huawei', 'BND-AL00': 'Huawei', 'XiaoMi': 'XiaoMi',
             'm1 metal': 'meizu', 'm2 note': 'meizu', 'MIX 2': 'XiaoMi', 'Oppo': 'Oppo', '  Oppo': 'Oppo',
             'Gionee': 'Gionee', 'Samsung': 'Samsung', 'PRA-AL00X': 'Huawei', 'PACM00': 'Oppo', 'PBET00': 'Oppo',
             'R7Plusm': 'Oppo', 'PAAT00': 'Oppo', 'PBAM00': 'Oppo', 'PADM00': 'Oppo', 'PAFM00': 'Oppo',
             'PBEM00': 'Oppo', 'PAAM00': 'Oppo', 'PBBM00': 'Oppo', 'PACT00': 'Oppo', 'V1809A': 'vivo', 'PBAT00': 'Oppo',
             'PADT00': 'Oppo', 'BND-TL10': 'Huawei', 'PBBT00': ' Oppo', 'PBCM10': 'Oppo', 'Mi Note 3': 'XiaoMi',
             'V1816A': 'vivo', 'V1732T': 'vivo', 'V1813A': 'vivo', 'V1732A': 'vivo', 'V1818A': 'vivo',
             'CAM-TL00': 'Huawei', 'Le X620': 'leshi', 'M6 Note': 'meizu', 'm3 note': 'meizu', 'M5': 'meizu',
             'M1 E ': 'meizu', 'BLN-AL10': 'Huawei', 'M5 Note': 'meizu', 'Meizu': 'meizu', 'PRA-AL00': 'honour',
             'LND-AL30': 'honour', 'NEM-AL10': 'honour', 'BND-AL10': 'honour', 'CAM-AL00': 'honour',
             'SCL-TL00': 'honour', 'LLD-AL30': 'honour', 'BLN-AL20': 'honour', 'AUM-AL20': 'honour',
             'JSN-AL00': 'honour', 'LLD-AL10': 'honour', 'BLN-TL10': 'honour', 'LLD-AL20': 'honour',
             'BLN-AL40': 'honour', 'MYA-AL10': 'honour', 'LLD-AL00': 'honour', 'JSN-AL00a': 'honour',
             'JMM-AL10': 'honour', 'DLI-AL10': 'honour', 'JMM-AL00': 'honour', 'V1809T': 'vivo', 'LND-AL40': 'honour',
             'PLK-AL10': 'honour', 'MX6': 'meizu', 'PLK-TL01H': 'honour', 'S9': 'Samsung', 'KIW-TL00': 'honour',
             'V1813T': 'vivo', 'Meizu S6': 'meizu', 'M2 E': 'meizu', 'M1 E': 'meizu', 'M5s': 'meizu', 'R7Plus': 'Oppo',
             'PBCM30': 'Oppo', 'AUM-AL00': 'honour', 'CAM-TL00H': 'honour', 'PBFM00': 'Oppo', 'V1818T': 'vivo',
             'AUM-TL20': 'honour', 'V1818CA': 'vivo'}


def func_map(string, m=map_phone):
    """
    :param string:
    :param m:
    :return:
    """
    if string in m.keys():
        return m[string]
    else:
        return string
