#!/usr/bin/env python
# coding: utf-8

# In[222]:


import pymysql
import pandas as pd
con = pymysql.Connect(
    host='120.79.36.32',
    port=3306,
    user='www_802k_cn',
    password='ksxGX8QfWipYte5z',
    db='www_802k_cn',
    charset='utf8'
)
sql = "select * from dd_user"
df = pd.read_sql(sql,con)



from pandas import Series,DataFrame


df1 = df[['id','mch','subscribe','subscribe_time']]


df2=df1.copy()



df2=df2[~df1['subscribe'].isin([0])]


df3 = df2.reset_index(drop=True)


import time
def change_time(t):
    xx = []
    for x in t:
        timeStamp = x
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        xx.append(otherStyleTime)
    return Series(xx)
# 在这一步改变了df表中的原数据
s = change_time(df3['subscribe_time'])


df3['subscribe_time']=s

dt = pd.to_datetime(df3['subscribe_time'])


df4=df3.copy()


df5 = df4.set_index(dt)



def draw_trend_hour(stime,s):
    x = []
    y = []
    for i in range(24):
        st = "%02d" % i
        x.append(st)
        ss = stime+' ' + st
        y.append(len(s[ss]))
    return (x,y)



stime = '2018-12-07'
x,y = draw_trend_hour(stime,df5)




y_sum = sum(y)



from tools.con_mysql import insert_to_db
from tools.my_sql import insert_new_user
sql = insert_new_user(y,stime,y_sum)

insert_to_db(sql)

