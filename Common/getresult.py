#coding=utf-8

import datetime


'''为时间控件获取时间，开始时间跟结束时间'''
def gettime():
    now = datetime.datetime.now()
    d = datetime.timedelta(days=30)
    n = now - d
    n = n.strftime("%Y-%m-%d")
    now = now.strftime("%Y-%m-%d")
    return (n,now)

