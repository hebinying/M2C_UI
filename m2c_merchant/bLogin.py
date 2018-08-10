#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO

def bLogin():
    driver=DR.getdriver()
    lg=BO.DriverBase(driver,"http://b.m2c2017test.com")
    lg.findElementsByTagName("input")[0]
    lg.send("13500000046")
    lg.findElementsByTagName("input")[1]
    lg.send("123456")
    cm=lg.findElementsByTagName("button")[1]
    lg.click(cm)

    print "商家登录"

bLogin()