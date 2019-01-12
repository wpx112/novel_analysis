# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pymysql


def insert_new_user(stime, y, y_sum):
    sql = "INSERT INTO new_user (day_t,hour0, hour1, hour2,hour3,hour4,hour5,hour6,hour7,hour8,hour9,hour10,hour11,hour12,hour13,hour14,hour15,hour16,hour17,hour18,hour19,hour20,hour21,hour22,hour23,sums)VALUES('{1}',{0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]},{0[8]},{0[9]},{0[10]},{0[11]},{0[12]},{0[13]},{0[14]},{0[15]},{0[16]},{0[17]},{0[18]},{0[19]},{0[20]},{0[21]},{0[22]},{0[23]},{2})".format(
        y, stime, y_sum)
    # print(sql)
    return sql


def insert_new_fans(stime, y, y_sum):
    sql = "INSERT INTO aa_new_fans (day_t,hour0, hour1, hour2,hour3,hour4,hour5,hour6,hour7,hour8,hour9,hour10,hour11,hour12,hour13,hour14,hour15,hour16,hour17,hour18,hour19,hour20,hour21,hour22,hour23,sums)VALUES('{1}',{0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]},{0[8]},{0[9]},{0[10]},{0[11]},{0[12]},{0[13]},{0[14]},{0[15]},{0[16]},{0[17]},{0[18]},{0[19]},{0[20]},{0[21]},{0[22]},{0[23]},{2})".format(
        y, stime, y_sum)
    # print(sql)
    return sql


def insert_uid_json(stime, user_json):
    tsql = "insert into user(day_t,info) values('{day_t}','{json}')"
    s = json.dumps(user_json)
    sql1 = tsql.format(day_t=stime, json=pymysql.escape_string(s))
    # print(sql1)
    return sql1


def update_json(stime, field_name, user_json, table_name):
    tsql = "UPDATE {table_name} SET {field_name}={field_value} WHERE day_t='{day_t}'"
    field_value = json.dumps(user_json)
    sql1 = tsql.format(day_t=stime, field_name=field_name, field_value=field_value, table_name=table_name)
    # print(sql1)
    return sql1


def update_twof_json(stime, f_n1, f_n2, f_v1, f_v2, table_name):
    tsql = "UPDATE {table_name} SET `{f_n1}`='{f_v1_json}',`{f_n2}`={f_v2} WHERE day_t='{day_t}'"
    sql1 = tsql.format(day_t=stime, f_n1=f_n1, f_n2=f_n2, f_v1_json=f_v1, f_v2=f_v2, table_name=table_name)
    # print(sql1)
    return sql1


def update_threef_json(stime, f_n1, f_n2, f_n3, f_v1, f_v2, f_v3, table_name):
    tsql = "UPDATE {table_name} SET `{f_n1}`='{f_v1_json}',`{f_n3}`='{f_v3}',`{f_n2}`={f_v2} WHERE day_t='{day_t}'"
    sql1 = tsql.format(day_t=stime, f_n1=f_n1, f_n2=f_n2, f_v1_json=f_v1, f_v2=f_v2, f_n3=f_n3, f_v3=f_v3,
                       table_name=table_name)
    # print(sql1)
    return sql1
