# coding=utf-8
from Common import driverstart as DR
from Common import baseOperator as BO
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains

class Master(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     dr =DR.driverstart("chrome")
    #     cls.driver = BO.DriverBase(dr)
    #     cls.driver.get_url("http://master.m2c2017test.com")
    #     cls.driver.ECsends("input", "mtx1215", 0)
    #     cls.driver.ECsends("input", "123456", 1)
    #     cls.driver.ECclick("button")
    #     cls.driver.ECclick("span.icon_1")

    # 登录
    def setUp(self):
        dr = DR.driverstart("chrome")
        self.driver = BO.DriverBase(dr)
        self.driver.get_url("http://master.m2c2017test.com")
        self.driver.ECsends("input", "mtx1215", 0)
        self.driver.ECsends("input", "123456", 1)
        self.driver.ECclick("button")
        self.driver.ECclick("span.icon_1")
        self.driver.ECclick("div.el-submenu__title")
        #time.sleep(2)
        print self.driver.findElementByPath('//li[text()="角色权限"]')
        self.driver.EPclick("//li[text()='角色权限']")

    def test_user_change(self):
        element=self.driver.findElementsByCssSelector("button.el-button--mini")
        action=ActionChains(self.driver)
        action.move_to_element(element[1])
        action.click(element[1])
        #ActionChains(self.driver).click()
        #self.driver.ECsclick("button.el-button--mini",0)
    # #修改密码
    # def test_master_UpdatePwd(self):
    #     u"""运营后台修改密码"""
    #     self.driver.ECsclick("span.el-dropdown-selfdefine ",1)
    #     self.driver.ECclick("i.iconfont.icon-mima")
    #     self.driver.ECsends("input.el-input__inner","123456",0)
    #     self.driver.ECsends("input.el-input__inner","123456", 1)
    #     self.driver.ECsends("input.el-input__inner","123456", 2)
    #     self.driver.ECclick("button.el-button.el-button--primary")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.stopDriver()

if __name__=='__main__':
    unittest.main()
