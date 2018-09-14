#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO
import comMethod
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time,datetime
import  Common.getSearchBox as GSB

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
        #print "第二次点击"
        #self.driver.ECclick("button.btn-search")
        self.driver.wait(1)
        #商品状态、商品类型
        self.driver.ECclick("div.searcWrap>span.el-cascader")
        #self.driver.ECsclick("div#pane-first div.searcWrap div.el-input--suffix>input.el-input__inner",0)
        # for i in range(0,1):
        #     self.driver.wait(1)
        self.driver.menu_triple_click("ul[id^='cascader-menu']>li", "ul[id^='menu']>li")
        time.sleep(3)
        # 选择商品分类
        self.driver.ECclick("div.searcWrap>div.el-select>div.el-input--suffix")

        #选择商品状态
        self.driver.EPsclick("//span[text()='商品状态']/parent::*/following-sibling::li",1)

        #选择搜索时间，默认设置：按当天时间取前30天
        enddate=datetime.date.today()
        startdate=enddate+datetime.timedelta(days=-30)
        GSB.time_input(self.driver,"div.searcWrap>div.el-date-editor>input",startdate,enddate)
        self.driver.ECclick("button.btn-search")

        # self.driver.ECsclick("ul[id^='cascader-menu']>li",2)
        # time.sleep(3)
        # self.driver.ECsclick("ul[id^='menu']>li",0)
        # elements=self.driver.findElementsByCssSelector("ul[id^='menu']")
        # if len(elements)>1:
        #     # time.sleep(1)
        #     # self.driver.EPsclick("//ul[3]/li",0)
        #     # eles[0].click()
        #     print elements[0].get_attribute("id")
        #     ids=elements[0].get_attribute("id").split('-')
        #     ids2=""
        #     for i in range(0,len(ids)-1):
        #         print ids[i]
        #         if i==0:
        #             ids2=ids[i]
        #         else:
        #             ids2+='-'+ids[i]
        #     print ids2
        #     ids2+='-2'
        #     print ids2
        #     name="ul#"+ids2+">li"
        #     self.driver.ECsclick(name,0)


        # self.driver.action_perfom(elements[1])
    #点击新增btn
    def click_add_button(self):
        elements=self.driver.findElementsByCssSelector("div.btnBox>button")
        for i in range(0,len(elements)):
            if elements[i].text=="新增":
                elements[i].click()
                #获取选项卡数
                num=self.driver.get_handles
                self.driver.changewinton(num-1)
                break
    #增加实物商品
    def test_good_add_physical(self):
        self.click_add_button()
        datas=comMethod.goodsdata
        #点击实物商品
        if datas['logisticsType.for']==0:
            self.driver.ECsclick("div[for='logisticsType']+div label",datas['logisticsType.for'])

        keys=comMethod.goodsdata.keys()
        for i in range(0,len(keys)):
            if "logisticsType" in keys[i]:
                pass
            names=keys.split('.')
            data=datas[keys[i]]
            self.driver.ECsclick("div.el-radio-group>label",0)

            #today here




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
