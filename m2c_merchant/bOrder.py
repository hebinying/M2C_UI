#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO

'''查询、查看详情、发货、导出待发货列表、批量发货'''

'''搜索待发货的订单'''

class bTestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # dr = DR.driverstart()
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")
        cls.driver.ECsends("input", '13500000070', 0)
        cls.driver.ECsends("input", '123456', 1)
        cls.driver.ECclick("button")

    def setUp(self):
        self.driver.wait(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


    #search
    def test_order_search(self):
        pass

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




