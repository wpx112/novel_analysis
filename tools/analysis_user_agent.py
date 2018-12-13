# !/usr/bin/env python
# -*- coding: utf-8 -*-

from user_agents import parse

ua_string = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
user_agent = parse(ua_string)
bw = user_agent.browser.family #浏览器
s = user_agent.os.family #操作系统
juge_pc = user_agent.is_pc #判断是不是桌面系统
phone = user_agent.device.family
print(bw,s,phone)