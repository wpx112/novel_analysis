# !/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# coding: utf-8

# In[37]:
from tools.con_mysql import create_con_r,insert_to_phone,insert_to_operating
import pandas as pd
from user_agents import parse
from tools.count_tools import map_phone,func_map

dtime = '2018-12-25'
t_name = '`aa_ip_useragent`'
sql = "SELECT useragent FROM {table} WHERE `date` = '{dtime}'".format(dtime=dtime, table=t_name)


def parse_user_agent(results):
    """
    只能解析今天以前的数据
    :param results: phone、operation
    :return:
    """
    phone = []
    # juge_pc = []
    operating = []
    print('开始解析user_agent')
    for us in results:
        if us[0]:
            user_agent = parse(us[0])
            op = user_agent.os.family  # 操作系统
            # j_pc = user_agent.is_pc #判断是不是桌面系统
            ph = user_agent.device.brand
            if ph == 'Generic_Android':
                phone.append(user_agent.device.family)
            else:
                phone.append(ph)
            # juge_pc.append(j_pc)
            operating.append(op)

    ss_p = pd.Series(phone)
    ss_p = ss_p.map(func_map)
    ph_sort = ss_p.value_counts()
    top9 = ph_sort[:9]

    for k, v in top9.to_dict().items():
        insert_to_phone(stime=dtime, k=k, v=v)
        print(k, v)

    other = ph_sort[9:]
    print(other)
    other_num = sum(other.values)
    insert_to_phone(stime=dtime, k='other', v=other_num)

    op = pd.Series(operating)     # 插入操作系统信息

    for k, v in op.value_counts().to_dict().items():
        insert_to_operating(stime=dtime, k=k, v=v)


if __name__ == '__main__':

    db = create_con_r()
    cursor = db.cursor()

    try:
        # 执行SQL语句
        print(sql)
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('读取完毕')
        parse_user_agent(results)
    except Exception as e:
        print(e,"Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
