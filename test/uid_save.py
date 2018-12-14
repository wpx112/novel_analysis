#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pymysql


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

sql = "SELECT info FROM USER ORDER BY uid DESC LIMIT 1"

con = create_con2()
cursor = con.cursor()
s = cursor.execute(sql)
data = cursor.fetchone()[0]
print(s)
print(data[0])
print(type(data[0]))


# In[16]:


import pandas as pd


# In[17]:


import json 


# In[23]:


j_data = json.loads(data)


# In[34]:


j_data['columns']


# In[ ]:





# In[33]:


from pandas import Series,DataFrame


# In[41]:


Series(data=j_data['data'],c)


# In[42]:


DataFrame(data=j_data['data'],columns=[j_data['columns']])

