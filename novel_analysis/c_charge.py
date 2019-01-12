#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from tools.my_sql import update_twof_json
from tools.con_mysql import save_upadate,create_con_r
from tools.count_tools import stime
from tools.draw_chart import c_charge


sql = "SELECT user_id,create_time,anid,charge_cid,charge_money FROM dd_user_behavior WHERE `date`='{stime}'" \
      " AND `charge_status`=2".format(stime=stime)

con = create_con_r()

df = pd.read_sql(con=con, sql=sql)

result = df.groupby(df['charge_money']).size()

charge_json = result.to_json()
x = result.index
y = result.values
x = list(x)
y = list(y)
sum = 0
for a, b in list(dict(result).items()):
    sum += a * b

sql = update_twof_json(stime, field_name1='charge', fileld_name2='amount', fileld_value2=sum, user_json=charge_json,
                       table_name='aa_sundry')

save_upadate(stime, sql, table_name='aa_sundry')


c_charge(x, y, sum)
