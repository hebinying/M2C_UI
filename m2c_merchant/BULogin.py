#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO
from Searchsql import GetVerifyCode as gt
import time
'''检查：登录，登录后的退出，修改登录密码'''


class BULogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dr = DR.driverstart("chrome")
        cls.driver = BO.DriverBase(dr)
        cls.driver.get_url("http://b.m2c2017test.com")
        cls.driver.ECsends("input", '13500000046', 0)
        cls.driver.ECsends("input", '123456', 1)
        cls.driver.ECclick("button")

    def setUp(self):
        time.sleep(1)

    #查看账户信息
    def test_acheck(self):
        self.driver.ECclick("span.ellipsis")
        self.driver.ECclick("div[path='/s/userInfo']")
        #self.assertIn(self.driver.findElementByPath("//span[text()='管理员']").text(),"管理员",msg="进入账户信息成功")

    #修改密码
    def test_bChange(self):
        npwd='123456'
        mobile='13500000046'
        self.driver.ECclick("span.ellipsis")
        self.driver.ECclick("div[path='/s/updatePass']")
        self.driver.EIclick("sendVer")
        g = gt.GetVerifyCode()
        sql = "select verify_code from t_support_verify_code WHERE created_date=(select MAX(created_date) FROM  t_support_verify_code WHERE mobile=%s)" % mobile
        cur = g.connect_sql("m2c_support")
        code = g.excute_sql(cur, sql)
        if code:
            self.driver.EIsend("verifyCode", code)

        '''设置新的密码'''
        self.driver.EIsend("newPass", npwd)
        self.driver.EIsend("confirmNewPass", npwd)
        self.driver.EPclick("//span[text()='保存']")
    #修改交易密码
    def test_ChangecashPass(self):
        npwd = '123456'
        mobile = '13500000046'
        self.driver.ECclick("span.ellipsis")
        self.driver.ECclick("div[path='/s/cashPass']")
        self.driver.EIclick("sendVer")
        g = gt.GetVerifyCode()
        sql = "select verify_code from t_support_verify_code WHERE created_date=(select MAX(created_date) FROM  t_support_verify_code WHERE mobile=%s)" % mobile
        cur = g.connect_sql("m2c_support")
        code = g.excute_sql(cur, sql)
        if code:
            self.driver.EIsend("verifyCode", code)
        '''设置新的交易密码'''
        self.driver.EIsend("newPass", npwd)
        self.driver.EIsend("confirmNewPass", npwd)
        self.driver.EPclick("//span[text()='保存']")
        #self.driver.ECclick("button.el-button.el-button--primary")

        #退出登录
    def test_bQuit(self):
        self.driver.ECclick("div.right_title_quit")
        print "退出登录"


    #关闭浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


if __name__=="__main__":
    '''suite=unittest.TestSuite()
    suite.addTest(BULogin("test_acheck"))
    suite.addTest(BULogin("test_ChangecashPass"))
    suite.addTest(BULogin("test_bChange"))
    suite.addTest(BULogin("test_bQuit"))
    runner=unittest.TextTestRunner()
    runner.run(suite)'''
    unittest.main()
