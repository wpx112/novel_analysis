# !/usr/bin/env python
# -*- coding: utf-8 -*-

from pyecharts import Line
from pyecharts import Map


china_map = ['北京','天津','上海','重庆','河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','海南','四川','贵州','云南','陕西','甘肃','青海','台湾','内蒙古','广西','西藏','宁夏','新疆','香港','澳门']


def draw_new_days(x,y):
    line = Line("每日访问量")
    line.add("新增用户数", x, y, is_smooth=True, mark_line=["max", "average"])
    line.render('../my_result/trend_day.html')


def draw_new_weeks(x,y):
    line = Line("最近七日访问量")
    line.add("新增用户数", x, y, is_smooth=True, mark_line=["max", "average"])
    line.render('../my_result/trend_weeks.html')


def draw_map(x,y):
    v_r=[0]
    v_r.append(max(y))
    map = Map("Map 结合 VisualMap 示例", width=1200, height=600, )
    map.add(
        '所有粉丝分布图',
        attr=x,
        value=y,
        # 文本颜色的取值范围
        visual_range=v_r,
        # is_more_utils=True,   #更多工具按钮
        maptype="china",
        is_visualmap=True,
        visual_text_color="#000",
        # 显示各区域名称
        is_label_show=True
    )
    map.render('../my_result/map.html')