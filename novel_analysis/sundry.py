#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql


# In[2]:


stime = '2018-12-18'


# In[3]:


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


# In[4]:


import pandas as pd


# In[5]:


from pandas import Series,DataFrame


# In[6]:


sql = "SELECT user_id,create_time,`event`,`action`,anid,charge_cid,charge_money,charge_status FROM dd_user_behavior WHERE `date` = '2018-12-18'"


# In[7]:


con = create_con_r()


# In[8]:


df = pd.read_sql(con=con,sql=sql)


# In[9]:


visit_num = df.shape[0] ###########总点击量


# In[10]:


visit_num


# In[11]:


################################################################################## 新增用户


# In[12]:


df_join = df.copy()


# In[13]:


df_join1 = df_join[df_join['event'] =='join']


# In[14]:


df_join_num = df_join1.shape[0] ###########新增用户人数


# In[15]:


import time
def change_time(t):
    '''
    :param t: 时间戳
    :return: %Y-%m-%d %H:%M:%S格式的时间
    '''
    timeStamp = t
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


# In[16]:


join_s = [change_time(x) for x in df_join1['create_time']]


# In[17]:


df_join1['create_time'] = join_s


# In[18]:


df_join1


# In[19]:


join_dt = pd.to_datetime(df_join1['create_time'])


# In[20]:


join_dt


# In[21]:


df_join2 = df_join1.copy()


# In[22]:


df_join2.insert(0, 'date', join_dt)


# In[23]:


df_join3 = df_join2.set_index(df_join2['date'])


# In[24]:


df_join4 = df_join3.drop(['date'], axis=1)


# In[25]:


join_ss = pd.Series(df_join4['user_id'], index=df_join4.index)


# In[26]:


def trend_hour(stime,s):
    '''
    :param stime: 时间
    :param s: 一个时间序列的Series
    :return: 时间和数值的元祖
    '''
    x = []
    y = []
    for i in range(24):
        st = "%02d" % i
        x.append(st)
        ss = stime+' ' + st
        try:
            y.append(s[ss].count())
        except:
            y.append(0)
    return (x,y)


# In[27]:


join_ids = list(join_ss.values) # 新增用户id列表


# In[28]:


len(join_ids)


# In[29]:


join_x,join_y = trend_hour(stime,join_ss)
join_sum = sum(join_y) # 新增用户数


# In[30]:


join_ids


# In[31]:


##############################################################


# In[32]:


df_fans = df.copy()


# In[33]:


df_fans1 = df_fans[df_fans['event']=='subscribe']


# In[34]:


fans_ids = list(df_fans1['user_id'].values)


# In[35]:


fans_ids_unique = list(set(join_ids).intersection(set(fans_ids)))


# In[36]:


df_fans2 = df_fans1[df_fans1['user_id'].isin(fans_ids_unique)]


# In[37]:


df_fans3 = df_fans2.drop_duplicates(['user_id'],keep='last')


# In[38]:


fans_ids_finally = list(df_fans3['user_id']) #新增粉丝的id


# In[39]:


fans_ids_sum = len(fans_ids_finally) #新增粉丝的总和


# In[40]:


df_fans4 = df_fans3.copy()


# In[41]:


s = [change_time(x) for x in df_fans4['create_time']]


# 在这一步改变了df表中的原数据
df_fans4['create_time'] = s


# In[42]:


def dataframe_s(result):
    result1 = result.copy()
    dt = pd.to_datetime(result1['create_time'])
    result2 = result.copy()
    result2.insert(0, 'date', dt)
    result3 = result2.set_index(result2['date'])
    result4 = result3.drop(['date'], axis=1)
    s = pd.Series(result4['user_id'], index=result4.index)
    return s


# In[43]:


fans_s = dataframe_s(df_fans4) 


# In[44]:


fans_s.shape


# In[45]:


fans_x,fans_y = trend_hour(stime,fans_s) # 新增粉丝的x/y值


# In[46]:


##########################################################################################################


# In[47]:


df_sign = df.copy()


# In[48]:


sign_num = df_sign[df_sign['event'].isin(['websign','apisign'])].shape[0] #每日签到人数


# In[49]:


##########################################################################################################


# In[50]:


df_visit_p = df.copy()


# In[51]:


sum_visit_p = df_visit_p.drop_duplicates(['user_id']).shape[0]  #总访问人数


# In[52]:


sum_visit_p


# In[53]:


##########################################################################################################


# In[54]:


df_unsubscribe = df.copy()


# In[55]:


unsubscribe_num = df_unsubscribe[df_unsubscribe['event']=='unsubscribe'].drop_duplicates(keep='last').shape #取关人数


# In[56]:


##############################################################################################c_charge


# In[63]:


df_charge = df.copy()


# In[66]:


df_charge1 = df_charge[df_charge['charge_status']==2]


# In[67]:


#充值成功
df_charge1


# In[69]:


charge_all = df_charge1.groupby(df_charge1['charge_money']).size()


# In[70]:


charge_all


# In[71]:


charge_json_all = charge_all.to_json() # 要存储的charge_json
charge_x_all = charge_all.index
charge_y_all = charge_all.values
charge_x_all = list(charge_x_all) # 充值的类型
charge_y_all = list(charge_y_all) # 充值的金额
sum_charge_all = 0
for a, b in list(dict(charge_all).items()):
    sum_charge_all += a*b


# In[74]:


sum(charge_y_all)


# In[76]:


df_charge2 = df_charge1[df_charge1['user_id'].isin(join_ids)]


# In[78]:


df_charge2.shape


# In[79]:


charge_new = df_charge2.groupby(df_charge2['charge_money']).size()


# In[80]:


charge_json_new = charge_new.to_json() # 要存储的新用户charge_json
charge_x_new = charge_new.index
charge_y_new = charge_new.values
charge_x_new = list(charge_x_new) # 新用户充值的类型
charge_y_new = list(charge_y_new) # 新用户充值的金额
sum_charge_new = 0
for a, b in list(dict(charge_new).items()):
    sum_charge_new += a*b


# In[82]:


charge_json_all


# In[81]:


charge_json_new


# In[83]:


##########################################################################################################

