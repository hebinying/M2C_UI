#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO


class bTestGoods(unittest.TestCase):
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

    #商品查询
    def test_good_search(self):
        pass

    #增加实物商品
    def test_good_add_physical(self):
        pass
    #增加虚拟商品
    def test_good_add_vitual(self):
        pass

    #增加自提商品
    def test_good_add_selfR(self):
        pass

    #查看商品详情
    def test_goods_detail(self):
        pass

    #修改商品
    def test_goods_modify(self):
        pass

    #上架商品
    def test_goods_shelf(self):
        pass

    #下架商品
    def test_goods_lower(self):
        pass

    #删除商品
    def test_goods_delete(self):
        pass

    #删除商品重新上架
    def test_goods_shelfagainst(self):
        pass

    #删除待审核商品
    def test_goods_delete_audited(self):
        pass


    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


class bTestGoodAppraise(unittest.TestCase):
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

    #商品评价搜索
    def test_Reviews_search(self):
        pass

    #回复商品评价
    def test_Reviews_reply(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


if __name__=='__main__':
    unittest.main()
