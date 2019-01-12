#!/usr/bin/env python
# coding: utf-8

# In[145]:


import pandas as pd
import pymysql
import json


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


# 打开数据库连接
db = create_con_r()

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 查询语句

sql = "SELECT aad.`collect` ,aad.`hot_read`,aad.`hot_read_chaps`,aad.`recharge` FROM `aa_anid` aad WHERE aad.`day_t` " \
      "= '2019-01-06'"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    dic1 = json.loads(results[0][0])
except Exception as e:
    print(e, "Error: unable to fetch data")

# 关闭数据库连接
db.close()

# In[148]:




# In[149]:


df1 = pd.DataFrame(dic1)

# In[150]:


df11 = df1[['anime_title', 'num']]

# In[151]:


df111 = df11.rename(columns={'anime_title': '小说名称', 'num': '收藏人数'})

dic2 = json.loads(results[0][1])

df2 = pd.DataFrame(dic2)

time = dic2['date']

df22 = df2[['anime_title', 'num']]

df222 = df22.rename(columns={'anime_title': '小说名称', 'num': '阅读人数', })

dic3 = json.loads(results[0][2])

df3 = pd.DataFrame(dic3)

df33 = df3[['anime_title', 'num']]
df333 = df33.rename(columns={'anime_title': '小说名称', 'num': '阅读满百章小说阅读人数'})

dic4 = json.loads(results[0][3])
df4 = pd.DataFrame(dic4)
df44 = df4[['anime_title', 'num', 'money']]
df444 = df44.rename(columns={'anime_title': '小说名称', 'num': '充值人数', 'money': '充值金额'})

writer = pd.ExcelWriter(r'D:\data_results\anids\小说排行榜（%s）.xlsx' % (time))
df111.to_excel(writer, sheet_name='收藏排行')
df222.to_excel(writer, '阅读人数排行')
df333.to_excel(writer, '阅读满百章小说排行')
df444.to_excel(writer, '小说充值排行')
writer.save()
