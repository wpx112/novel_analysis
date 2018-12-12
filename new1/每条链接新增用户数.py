#!/usr/bin/env python
# coding: utf-8

# In[18]:


from  pyecharts import Bar


# In[2]:


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
sql = "select * from dd_chapter"
df = pd.read_sql(sql,con,index_col="id")
df


# In[13]:


x =df['mch'].index


# In[14]:


y = df['pernums'].values


# In[20]:


attr = ["{}条".format(i) for i in x]
# v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("每条链接引入人数")
bar.add(
    "",
    attr,
    y,
    is_datazoom_show=True,
    datazoom_type="inside",
    datazoom_range=[10, 25],
)
bar.render('show_increase.html')




