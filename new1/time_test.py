# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def change_time(t):
    timeStamp = t
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    return otherStyleTime


