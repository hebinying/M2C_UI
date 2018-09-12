#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO
import comMethod


class bTestGoods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # dr = DR.driverstart()
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")
        comMethod.bloggin(cls.driver,'13500000070','123456')
        # cls.driver.ECsends("input", '13500000070', 0)
        # cls.driver.ECsends("input", '123456', 1)
        # cls.driver.ECclick("button")

    def setUp(self):
        self.driver.ECsclick("div.public_nav",2)
        self.driver.EPclick("//div[@path='/s/goodList']")
        self.driver.wait(1)

    #商品查询
    def test_good_search(self):
        #输入框检查
        self.driver.EPsend("//input[@placeholder='输入商品名称/编码/条形码/品牌']","test")
        self.driver.ECclick("button.btn-search")
        self.driver.inputclear("//input[@placeholder='输入商品名称/编码/条形码/品牌']","span")
        #self.driver.EPclick("//input[@placeholder='输入商品名称/编码/条形码/品牌']/following-sibling::span")
        print "第二次点击"
        self.driver.ECclick("button.btn-search")
        #商品状态、商品类型
        elements=self.driver.findElementsByCssSelector("div.el-input.el-input--suffix")
        for i in range(0,1):
            self.driver.ECsclick("div.el-input.el-input--suffix",i)
            #增加鼠标移动操作
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


    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.stopDriver()


class bTestGoodAppraise(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")
        cls.driver.ECsends("input", '13500000070', 0)
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
