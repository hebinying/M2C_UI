#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO
from Searchsql import GetVerifyCode as gt

'''检查：登录，退出，修改登录密码'''


class BULogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        dr = DR.openfile()
        self.driver = BO.DriverBase(dr)
        self.driver.get_url("http://b.m2c2017test.com")
    def bLogin(self,username,password):
        self.driver.ECsend("input",username,0)
        self.driver.ECsend("input",password,1)
        self.driver.ECclick("button")
        if self.driver.contain_title("商家平台"):
            print "商家登录"

    def bChange(self,mobile, npwd):
        self.driver.ECclick("span.el-dropdown-link.ellipsis.el-dropdown-selfdefine")
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
        self.driver.ECclick("button.el-button.el-button--primary")

    "退出登录"
    def bQuit(self):
        self.driver.ECclick("right_title_quit")
        print "退出登录"


    "关闭浏览器"
    @classmethod
    def tearDown(self):
        self.driver.stopDriver()


if __name__=="__main__":
    unittest.main()





