# !/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# coding: utf-8




from pandas import DataFrame, Series
from tools.con_mysql import create_con

# import pymysql
import pandas as pd


con = create_con()
sql = "select * from dd_user"
df = pd.read_sql(sql, con)





import time
def change_time(t):
    timeStamp = t
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


# 在这一步改变了df表中的原数据
df['join_time'] = Series([change_time(x) for x in df['join_time']])

# 创建了一个新的Serias
dt = pd.to_datetime(df['join_time'])



df2 = DataFrame(df['id'])
df2.set_index(dt)
df2.insert(0, 'date', dt)
df3 = df2.set_index(df2['date'])
df4 = df3.drop(['date'], axis=1)
df4['2018-08'].groupby('id')


s = pd.Series(df4['id'], index=df4.index)
# print(type(s))
print(s.head(2))

#此处的s可以通过日期来进行筛选需要的时间段，日，月访问数据
s['2018-08-13 00'].count()  # '2018-08-13 00'的新增人数


# 画取当日新增用户数
def draw_trend_hour(stime):
    x = []
    y = []
    for i in range(24):
        st = "%02d" % i
        x.append(st)
        ss = stime+' ' + st
        y.append(s[ss].count())
    return (x,y)

# 画取七日新增用户数
def draw_trend_weeks(stime):
    x = []
    y = []
    for i in range(29-7,29):
        st = "%02d" % i
        x.append(st)
        ss = stime+'-' + st
        y.append(s[ss].count())
    return (x,y)

stime = '2018-8-13'

x,y = draw_trend_hour(stime)
y_sum = sum(y)
# x1,y1 = draw_trend_weeks(stime)


from tools.con_mysql import judge_new_user
from tools.my_sql import insert_new_user
sql = insert_new_user(y, stime, y_sum)



judge_new_user(stime, sql)


# from tools.draw_chart import draw_new_days
# # draw_new_days(x,y)