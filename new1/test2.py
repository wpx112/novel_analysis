# ss = '2018-08-13'+' '+'00'
import time
t = 1544150531
timeStamp = t
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)