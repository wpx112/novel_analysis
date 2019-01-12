# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(dir_path)

from tools.con_mysql import create_con_r
from tools.count_tools import stime, tab_name, outer_chain
from novel_analysis.right.sundry_def import sundry1
from novel_analysis.right.anids_read import anids_read
from novel_analysis.right.new_user import new_user
from novel_analysis.right.new_visit import new_visit
from novel_analysis.right.new_fans import new_fans
from novel_analysis.right.anids_collect import anids_collect
from novel_analysis.right.page_analysis import page_analysis
from novel_analysis.right.anids_recharge import anids_recharge
from novel_analysis.right.fans_subscribe import fans_subscribe
import pandas as pd


sql = "SELECT user_id, create_time, anid,anime_title,chaps, freechaps, `event`, `action`, charge_cid, charge_money," \
      "charge_status, vip_time, chapter, sex FROM {table} WHERE `date` = '{stime}'".format(stime=stime, table=tab_name)

print(sql)
con = create_con_r()
df = pd.read_sql(con=con, sql=sql, parse_dates=['create_time'], index_col='create_time')
tz = df.index.tz_localize('UTC')
create_time2 = tz.tz_convert('Asia/Shanghai')  # 时区的转换
df.index = create_time2
mt = outer_chain()  # 用于映射外推书名

sql_anime_type = "SELECT dds.`anime_id`,dds.`chapter_type`  FROM `dd_chapter_statistics` dds where dds.`create_time` >" \
                 " UNIX_TIMESTAMP('2019-01-04') GROUP BY dds.`anime_id`"

con = create_con_r()
df_title = pd.read_sql(con=con, sql=sql_anime_type)


print(mt)
print('读取完毕，开始处理杂项')
sundry1(df)
print('开始，anids_read,小说阅读人数排行')
anids_read(df, mt, df_title)
print('开始，anids_collect,小说收藏')
anids_collect(df, mt, df_title)
print('开始,anids_recharge,小说充值排行')
anids_recharge(df, mt, df_title)
print('开始，anids_user,新增用户')
new_user(df)
print('开始，new_user,所有访客')
new_visit(df)
print('开始，new_visit,所有粉丝')
new_fans(df)
print('开始，page_analysis,页面分析')
page_analysis(df)
print('开始，fans_subscribe,关注粉丝统计')
fans_subscribe(df)
