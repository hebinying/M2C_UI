#coding=utf-8
import unittest
from Common import driverstart as DR
from Common import baseOperator as BO
import comMethod
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time,datetime
import  Common.getSearchBox as GSB
import random,os
ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

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
                handles=self.driver.get_handles()
                print handles
                self.driver.changewinton(len(handles)-1)
                break
    #新增商品测试
    def test_add_goods(self):
        datas = comMethod.goodsdata
        print datas['addgoogstype.int']
        for data in datas['addgoogstype.int']:
            if data ==0:
                self.good_add_physical()
            elif data==1:
                self.good_add_vitual()
            elif data==2:
                self.good_add_selfR()
            else:
                print "addgoogstype setting in the range(0,2)"

    # 增加实物商品
    def good_add_physical(self):
        self.click_add_button()
        datas=comMethod.goodsdata
        #点击实物商品
        if datas['logisticsType.for']==0:
            self.driver.ECsclick("label[for='logisticsType']+div label",datas['logisticsType.for'])

        keys=comMethod.goodsdata.keys()
        for i in range(0,len(keys)):
            names = keys[i].split('.')
            print names
            data = datas[keys[i]]

            if "for" in keys[i]:
                path="label["+names[1]+"='"+names[0]+"']~div input"
                print path
                #使用local环境
                if names[0]=="goodsPerMaxNum":
                    print len(data)
                    for i in range(0,len(data)):
                        self.driver.ECsends(path,data[i],i)
                elif names[0]=="goodsPostageId":
                    path="label["+names[1]+"='"+names[0]+"']~div div.el-input--suffix"
                    print path
                    self.driver.ECclick(path)
                    self.driver.menu_triple_click("body>div.el-select-dropdown ul>li")
                elif "logisticsType" in keys[i]:
                    pass
                else:
                    self.driver.ECsend(path,data)
            if "selected" in names[1]:
                path = "label[for='" + names[0] + "']~div span"
                print path
                self.driver.ECclick(path)
                #商品分类
                if names[0]=='goodsClassifyId':
                        self.driver.menu_triple_click("ul[id^='cascader-menu']>li", "ul[id^='menu']>li")
                #商品品牌
                if names[0]=="goodsBrandId":
                    self.driver.menu_triple_click("ul>div.resize-triggers~li")
                #商品分组
                if names[0]=="goodsGroups":
                    self.driver.menu_triple_click("div[x-placement='bottom-start'] ul[id^='cascader-menu']>li","ul[id^='menu']>li")
            if "id" in names[1]:
                #文本编辑
                if names[0]=='videoContainer':
                    path = "div#" + names[0] + " input"
                    videopath=ROOT(data)
                    self.driver.ECsend(path, videopath)
            if "iframe" in names[1]:
                self.driver.switch_to_iframe(names[2])
                self.driver.excute_js(data)

            if "class" in names[1]:
                if names[0]=='graySpan':
                    path="div."+names[0]+" div.el-col>label"
                    print path
                    elenum=self.driver.get_elements_number(path)
                    number=random.randint(0,elenum)
                    for i in range(0,number):
                        num=random.randint(0,elenum)
                        print num
                        #self.driver.ECsclick(path,num)
                        elements=self.driver.findElementsByCssSelector(path+'>span')
                        elements[0].click()
                if names[0]=='skuFlag':
                    pass
                if names[0]=='tabPane':

                    elenum=self.driver.get_elements_number("div.tabPane tr")
                    #单一规格输入
                    if elenum==2:
                        inventory=data[0]['inventory']
                        kg=data[0]['kg']
                        price=data[0]['price']
                        marketprice=data[0]['marketprice']
                        supplyprice=data[0]['supplyprice']
                        goosdscode=data[0]['goosdscode']
                        self.driver.ECsends("div.tabPane input",inventory,0)
                        self.driver.ECsends("div.tabPane input", kg, 1)
                        self.driver.ECsends("div.tabPane input", str(price), 2)
                        self.driver.ECsends("div.tabPane input", marketprice, 3)
                        self.driver.ECsends("div.tabPane input", str(supplyprice), 4)
                        self.driver.ECsends("div.tabPane input", goosdscode, 5)
                if names[0]=='mainImg':
                    path='div.'+names[0]+'~div input'

                    for i in range(0,len(data)):
                        #data的路径有问题，需要调整未绝对路径
                        filepath = ROOT(data[i])
                        print filepath
                        self.driver.ECsend(path,filepath)

                if names[0]=='commit':
                    path='div.poi3 button'
                    self.driver.ECclick(path)
                    #判断有问题
                    #self.driver.assert_text("div.el-message>p","保存成功")
    #增加虚拟商品 todayhere
    def good_add_vitual(self):
        self.click_add_button()
        datas = comMethod.goodsdata
        # 点击实物商品
        datas['logisticsType.for'] = 1
        self.driver.ECsclick("label[for='logisticsType']+div label", datas['logisticsType.for'])

        keys = comMethod.goodsdata.keys()
        for i in range(0, len(keys)):
            names = keys[i].split('.')
            print names
            data = datas[keys[i]]
            if "for" in keys[i]:
                path = "label[" + names[1] + "='" + names[0] + "']~div input"
                print path
                # 使用local环境
                if names[0] == "goodsPerMaxNum":
                    print len(data)
                    for i in range(0, len(data)):
                        self.driver.ECsends(path, data[i], i)
                elif names[0] == "goodsPostageId":
                   pass
                elif "logisticsType" in keys[i]:
                    pass
                else:
                    self.driver.ECsend(path, data)
            if "selected" in names[1]:
                path = "label[for='" + names[0] + "']~div span"
                print path
                self.driver.ECclick(path)
                # 商品分类
                if names[0] == 'goodsClassifyId':
                    self.driver.menu_triple_click("ul[id^='cascader-menu']>li", "ul[id^='menu']>li")
                # 商品品牌
                if names[0] == "goodsBrandId":
                    self.driver.menu_triple_click("ul>div.resize-triggers~li")
                # 商品分组
                if names[0] == "goodsGroups":
                    self.driver.menu_triple_click("div[x-placement='bottom-start'] ul[id^='cascader-menu']>li",
                                                  "ul[id^='menu']>li")
            if "id" in names[1]:
                # 文本编辑
                if names[0] == 'videoContainer':
                    path = "div#" + names[0] + " input"
                    videopath = ROOT(data)
                    self.driver.ECsend(path, videopath)
            if "iframe" in names[1]:
                self.driver.switch_to_iframe(names[2])
                self.driver.excute_js(data)

            if "class" in names[1]:
                if names[0] == 'graySpan':
                    path = "div." + names[0] + " div.el-col>label"
                    print path
                    elenum = self.driver.get_elements_number(path)
                    number = random.randint(0, elenum)
                    for i in range(0, number):
                        num = random.randint(0, elenum)
                        print num
                        # self.driver.ECsclick(path,num)
                        elements = self.driver.findElementsByCssSelector(path + '>span')
                        elements[0].click()
                if names[0] == 'skuFlag':
                    pass
                if names[0] == 'tabPane':

                    elenum = self.driver.get_elements_number("div.tabPane tr")
                    # 单一规格输入
                    if elenum == 2:
                        inventory = data[0]['inventory']
                        kg = data[0]['kg']
                        price = data[0]['price']
                        marketprice = data[0]['marketprice']
                        supplyprice = data[0]['supplyprice']
                        goosdscode = data[0]['goosdscode']
                        self.driver.ECsends("div.tabPane input", inventory, 0)
                        self.driver.ECsends("div.tabPane input", kg, 1)
                        self.driver.ECsends("div.tabPane input", str(price), 2)
                        self.driver.ECsends("div.tabPane input", marketprice, 3)
                        self.driver.ECsends("div.tabPane input", str(supplyprice), 4)
                        self.driver.ECsends("div.tabPane input", goosdscode, 5)
                if names[0] == 'mainImg':
                    path = 'div.' + names[0] + '~div input'

                    for i in range(0, len(data)):
                        # data的路径有问题，需要调整未绝对路径
                        filepath = ROOT(data[i])
                        print filepath
                        self.driver.ECsend(path, filepath)

                if names[0] == 'commit':
                    path = 'div.poi3 button'
                    if self.driver.contain_title("商品修改新增"):
                        self.driver.wait(2)
                        self.driver.ECclick(path)
                    # 判断有问题
                    #self.driver.assert_text("div.el-message>p", "保存成功")

    #增加自提商品
    def good_add_selfR(self):
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
