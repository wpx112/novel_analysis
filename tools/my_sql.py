# !/usr/bin/env python
# -*- coding: utf-8 -*-

def insert_new_user(stime,y,y_sum):
    sql = "INSERT INTO new_user (day_t,hour0, hour1, hour2,hour3,hour4,hour5,hour6,hour7,hour8,hour9,hour10,hour11,hour12,hour13,hour14,hour15,hour16,hour17,hour18,hour19,hour20,hour21,hour22,hour23,sums)VALUES('{1}',{0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]},{0[8]},{0[9]},{0[10]},{0[11]},{0[12]},{0[13]},{0[14]},{0[15]},{0[16]},{0[17]},{0[18]},{0[19]},{0[20]},{0[21]},{0[22]},{0[23]},{2})".format(y, stime,y_sum)
    print(sql)
    return sql



def insert_newid_json(y,stime,y_sum):
    sql = "INSERT INTO new_user (day_t,hour0, hour1, hour2,hour3,hour4,hour5,hour6,hour7,hour8,hour9,hour10,hour11,hour12,hour13,hour14,hour15,hour16,hour17,hour18,hour19,hour20,hour21,hour22,hour23,sums)VALUES('{1}',{0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]},{0[8]},{0[9]},{0[10]},{0[11]},{0[12]},{0[13]},{0[14]},{0[15]},{0[16]},{0[17]},{0[18]},{0[19]},{0[20]},{0[21]},{0[22]},{0[23]},{2})".format(y, stime,y_sum)
    print(sql)
    return sql