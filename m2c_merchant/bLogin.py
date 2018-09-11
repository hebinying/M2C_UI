#coding=utf-8
from Common import driverstart as DR
from Common import baseOperator as BO
from Searchsql import GetVerifyCode as gt
import unittest
import requests

'''首页登录、修改密码
@bebinn
@20180829
'''
class BLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")

    '''登录'''
    def test_login(self):
        self.driver.ECsends("input", '13500000070',0)
        self.driver.ECsends("input", '123456', 1)
        self.driver.ECclick("button")
        #self.assertIn(u"登录成功",self.driver.findElementByCssSelector("p.el-message__content").text)

    '''忘记登录密码'''
    def test_changepwd(self):
        self.driver.ECclick("div.lost")
        self.driver.ECsend("input.public_input_phone",'13500000070')
        self.driver.ECclick("button.phone_right")
        g = gt.GetVerifyCode()
        sql = "select verify_code from t_support_verify_code WHERE created_date=(select MAX(created_date) FROM  t_support_verify_code WHERE mobile='13500000046')"
        cur = g.connect_sql("m2c_support")
        code = g.excute_sql(cur, sql)
        if code:
            self.driver.ECsend("input.hone_code",code)
        self.driver.ECsend("input.public_input_password",'123456')
        self.driver.ECclick("button.complete_button.phone_right")

    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


if __name__=='__main__':
    unittest.main()
