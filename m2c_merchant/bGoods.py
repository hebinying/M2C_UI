#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO


class bTestGoods(unittest.TestCase):
    @classmethod
    def setUp(self):
        dr = DR.openfile()
        self.driver = BO.DriverBase(dr)
        self.driver.get_url("http://b.m2c2017test.com")
        self.driver.ECsend("input", '13500000046', 0)
        self.driver.ECsend("input", '123456', 1)
        self.driver.ECclick("button")
        if self.driver.contain_title("商家平台"):
            print "商家登录"




    @classmethod
    def tearDown(self):
        self.driver.stopDriver()
