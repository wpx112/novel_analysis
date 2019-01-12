#!/usr/bin/env python
# coding: utf-8

# In[159]:
###计算留存率
from tools.con_mysql import create_con_r,save_upadate
from tools.count_tools import r_stime
import pandas as pd
import json


def retention(stime):
    print('开始计算留存',stime)
    sql = "SELECT join_ids FROM aa_new WHERE `day_t` = '{stime}'".format(stime=stime)
    tsql = "SELECT visit_ids FROM `aa_new` WHERE day_t BETWEEN '{t}' AND  DATE_SUB(CURDATE(), INTERVAL 1 DAY)"
    sql_v = tsql.format(t=stime)

    con = create_con_r()
    df = pd.read_sql(con=con,sql=sql_v)

    db = create_con_r()
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()[0]
    # 关闭数据库连接
    db.close()

    #data 为当日新增用户
    data = json.loads(data)

    base_ids = data['ids']
    # base = len(base_ids)
    retention = []

    for i in df['visit_ids']:
        ids = json.loads(i)['ids']
        b3=list(set(base_ids) & set(ids))
        retention.append(len(b3))

    retention_dic = {'date':stime,'data':retention}

    retention_json = json.dumps(retention_dic)

    sql_update = "UPDATE {table_name} SET `{f_n1}`='{f_v1_json}' WHERE day_t='{day_t}'"
    sql_update1 = sql_update.format(day_t=stime,f_n1='retention',f_v1_json=retention_json,table_name='aa_sundry')

    save_upadate(stime=stime,sql=sql_update1,table_name='aa_sundry')


stime = '2019-01-10'
data = r_stime(stime=stime)
for i in data:
    retention(i[0])
