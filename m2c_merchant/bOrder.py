#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO
import comMethod
import random,datetime
import  Common.getSearchBox as GSB

'''查询、查看详情、发货、导出待发货列表、批量发货'''

'''搜索待发货的订单'''

class bTestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")
        comMethod.bloggin(cls.driver, '13500000070', '123456')

    def setUp(self):
        try:
            self.assertIn("block;",self.driver.findElementsByCssSelector("div.content_container" )[0].get_attribute("style"))
        except:
            print "点击菜单,展开二级目录"
            self.driver.ECsclick("div.public_nav", 1)
        #点击二级菜单_订货单
        self.driver.EPclick("//div[@path='/s/bug']")
        self.driver.wait(1)
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


    #search
    def test_order_search(self):
        #订单状态选择
        self.driver.ECsclick("div.searcWrap>div.el-select>div.el-input--suffix",0)
        self.driver.ECsclick("//span[text()='订单状态']/parent::li/following-sibling::li",random.randint(0,self.driver.get_elements_number("//span[text()='订单状态']/parent::*/following-sibling::li")-1))
        #售后状态
        self.driver.ECsclick("div.searcWrap>div.el-select>div.el-input--suffix",1)
        self.driver.ECsclick("//span[text()='售后状态']/parent::li/following-sibling::li",random.randint(0,self.driver.get_elements_number("//span[text()='售后状态']/parent::*/following-sibling::li")-1))
        # 选择搜索时间，默认设置：按当天时间取前30天
        enddate = datetime.date.today()
        startdate = enddate + datetime.timedelta(days=-30)
        GSB.time_input(self.driver, "div.searcWrap>div.el-date-editor>input", startdate, enddate)
        #搜索输入框，搜索关键字：test
        self.driver.ECsend("div.searcWrap div[class='el-input']>input.el-input__inner","test")

        self.driver.ECclick("button.btn-search")


    #hsearch
    def test_order_search_more(self):
        pass

    #导出
    def test_order_expot(self):
        pass

    #批量发货
    def test_order_deliveries(self):
        pass

    #详情页查看
    def test_order_detail(self):
        pass

    #发货
    def test_order_delivery(self):
        pass

    #新增仅退款售后
    def test_order_addAfter_refunds(self):
        pass

    #新增退货售后
    def test_order_addAfter_Return(self):
        pass


    #新增换货
    def test_order_addAfter_Exchange(self):
        pass



class bTestAfter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dr = DR.driverstart("chrome")
        cls.driver = BO.DriverBase(dr)
        cls.driver.get_url("http://b.m2c2017test.com")
        cls.driver.ECsends("input", '13500000046', 0)
        cls.driver.ECsends("input", '123456', 1)
        cls.driver.ECclick("button")

    def setUp(self):
        self.driver.wait(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


    #搜索售后
    def test_After_search(self):
        pass

    #查看详情
    def test_After_detail(self):
        pass

    #仅退款
    def test_After_refunds(self):
        pass

    #退货
    def test_After_retun(self):
        pass

    #换货
    def test_After_exchange(self):
        pass




