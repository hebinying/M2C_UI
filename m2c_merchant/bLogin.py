#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO

def bLogin():

    driver=DR.openfile()
    driver=BO.DriverBase(driver,"http://b.m2c2017test.com")

    ele=driver.findElementsByTagName("input")
    driver.send(ele[0],"13500000046")
    driver.send(ele[1], "123456")
    cm=driver.findElementsByTagName("button")[1]
    driver.click(cm)

    print "商家登录"

bLogin()