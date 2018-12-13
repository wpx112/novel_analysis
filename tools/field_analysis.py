# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def get_ip_info(ip):

    r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
    print(r.json())
    if r.json()['code'] == 0:
        i = r.json()['data']
        # print(i)
        country = i['country']  # 国家
        area = i['area']  # 区域
        region = i['region']  # 地区
        city = i['city']  # 城市
        isp = i['isp']  # 运营商

        print(u'国家: %s\n区域: %s\n省份: %s\n城市: %s\n运营商: %s\n' % (country, area, region, city, isp))
    else:
        print("ERROR! ip: %s" % ip)

def get_ip_info1(ip,dic):
    try:
        r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
        print(r.json())

        if r.json()['code'] == 0:
            i = r.json()['data']
             # print(i)
            country = i['country']  # 国家
            region = i['region']  # 省份
            city = i['city']  # 城市
            isp = i['isp']  # 运营商

            print(u'国家:  %s\n省份: %s\n城市: %s\n运营商: %s\n' % (country, region, city, isp))
            dic['country'].append(country)
            dic['region'].append(region)
            dic['city'].append(city)

        else:
            print("ERROR! ip: %s" % ip)
    except:
        print('访问出错')
        dic['country'].append('1')
        dic['region'].append('2')
        dic['city'].append('3')

ips =[ '123.125.115.110',
 '120.236.174.129',
 '120.197.11.5',
 '183.233.19.49',
 '211.136.207.185',
'221.183.26.125',
'221.176.24.242',
'221.183.23.74',
'219.158.38.213',
'219.158.5.129',
'202.96.12.118',
'124.65.58.54',
'123.125.248.126']


dic = {"country":[],'region':[],'city':[]}
for ip in ips:
    get_ip_info1(ip,dic)

print(dic)