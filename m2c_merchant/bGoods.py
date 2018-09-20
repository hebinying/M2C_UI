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
import logging
ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

#商品库测试
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
        #目录点击
        try:
            #判断二级目录是否是打开状态
            self.assertIn("display: block;",self.driver.findElementsByCssSelector("div.content_container")[1].get_attribute("style"))
            print "无需点击菜单"
        except:
            print "点击菜单"
            self.driver.ECsclick("div.public_nav", 2)
            self.driver.wait(1)
        self.driver.EPclick("//div[@path='/s/goodList']")
        self.driver.wait(1)

    #商品库测试操作
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
        self.driver.changewinton(0)

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
        # 点击虚拟商品
        datas['logisticsType.for'] = 2
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

                        price = data[0]['price']
                        marketprice = data[0]['marketprice']
                        supplyprice = data[0]['supplyprice']
                        goosdscode = data[0]['goosdscode']

                        #self.driver.ECsends("div.tabPane input", inventory, 0)
                        self.driver.ECsends("div.tabPane input", str(price), 0)
                        self.driver.ECsends("div.tabPane input", marketprice, 1)
                        self.driver.ECsends("div.tabPane input", str(supplyprice), 2)
                        self.driver.ECsends("div.tabPane input", goosdscode, 3)

                        #上传虚拟库存
                        vitualinventory = data[0]['vitualinventory']
                        path=ROOT(vitualinventory)
                        self.driver.ECclick("td>a")
                        self.driver.ECsend("div.hptczp_body>input[type='file']",path)
                        #判断有问题
                        # while self.driver.assert_exit("div.el-message--success"):
                        #     continue
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
        self.click_add_button()
        datas = comMethod.goodsdata
        # 点击虚拟商品
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
                    self.driver.menu_triple_click("div[x-placement='bottom-start'] ul[id^='cascader-menu']>li","div[x-placement='bottom-start'] ul[id^='menu']>li")
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
                    # self.driver.assert_text("div.el-message>p", "保存成功")

    #商品库查看商品详情
    def test_goods_detail(self):
        print self.driver
        self.driver.changewinton(0)
        # 获取对应点击的商品名称
        goodstitle = self.driver.findElementsByCssSelector("div.good_info  td[class^='el-table_1_column'] p[title]")
        num = random.randint(0, self.driver.get_elements_number("div.good_info i.cursor")-1)
        print num

        goodtitle = goodstitle[num*2].get_attribute("title")
        print goodtitle
        self.driver.ECsclick("div.good_info i.cursor",num)

        elements=self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
        for element in elements:
            if "display" in element.get_attribute("style"):
                print "here"
                continue
            else:
                #点击详情btn
                self.driver.ECsclick("body>ul>li",0)
                self.driver.changewinton(1)
                print self.driver
        #获取详情页的商品名称
        try:
            detailgoodtitle = self.driver.findElementsByCssSelector("td.a2>div")[0].text
            print detailgoodtitle
            self.assertEqual(goodtitle,detailgoodtitle,"打开详情页成功")
            logging.info("打开详情页成功")
            #关闭当前窗口
            self.driver.stopDriver()
        except Exception:
            logging.error("打开详情页失败")

    #商品库修改商品
    def test_goods_modify(self):
        try:
            # 获取对应点击的商品名称
            goodstitle = self.driver.findElementsByCssSelector("div.good_info  td[class^='el-table_1_column'] p[title]")

            num = random.randint(0, self.driver.get_elements_number("div.good_info i.cursor")-1)
            print num

            goodtitle = goodstitle[num * 2].get_attribute("title")
            print goodtitle
            self.driver.ECsclick("div.good_info i.cursor", num)
            elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
            for element in elements:
                if "display" in element.get_attribute("style"):
                    continue
                else:
                    # 点击编辑btn
                    self.driver.ECsclick("body>ul>li", 2)
                    self.driver.changewinton(1)
            # 分类、拍获价、供货价、新增规格需要再次审核
            #修改其他的参数
            #只改标题
            #goodNameelement=self.driver.findElementByCssSelector("label[for='goodsName']~div input")
            goodName=goodtitle+str(datetime.datetime.today().strftime("%Y.%m.%d %H%m"))
            t=0
            while t<10:
                try:
                    self.driver.clear("label[for='goodsName']~div input")
                    self.driver.ECsend("label[for='goodsName']~div input",goodName)
                    break
                except:
                    t+=1
            path = 'div.poi3 button'
            if self.driver.contain_title("商品修改新增"):
                self.driver.wait(2)
                self.driver.ECclick(path)
        except:
            logging.error("商品修改失败")
         #返回第一个标签页
        self.driver.changewinton(0)


    #商品库上架商品
    def test_goods_shelf(self):

        # 选择商品状态——仓库中
        self.driver.ECclick("div.searcWrap>div.el-select span.el-input__suffix")
        self.driver.EPsclick("//span[text()='商品状态']/parent::*/following-sibling::li", 0)
        self.driver.ECclick("button.btn-search")
        time.sleep(2)
        #判断是否有结果
        nums=self.driver.get_elements_number("tbody>tr")
        print nums
        if nums>0:
            num = random.randint(0, nums-1)
            print num
            goodtitle = self.driver.findElementsByCssSelector("div.good_info  td[class^='el-table_1_column'] p[title]")[num].get_attribute("title")
            self.driver.ECsclick("div.good_info i.cursor", num)
            elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
            for element in elements:
                if "display" in element.get_attribute("style"):
                    continue
                else:
                    # 点击上架btn
                    self.driver.ECsclick("body>ul>li", 1)
                    ele=self.driver.findElementByCssSelector("div.el-message--success p")
                    if ele.text=="操作成功":
                        print "上架成功"
                        logging.info("商品%s上架成功" %goodtitle)


    #商品库下架商品
    def test_goods_lower(self):
        # 选择商品状态——仓库中
        self.driver.ECclick("div.searcWrap>div.el-select span.el-input__suffix")
        self.driver.EPsclick("//span[text()='商品状态']/parent::*/following-sibling::li", 1)
        self.driver.ECclick("button.btn-search")
        time.sleep(2)
        # 判断是否有结果
        nums = self.driver.get_elements_number("tbody>tr")
        print nums
        if nums > 0:
            num = random.randint(0, nums - 1)
            print num
            try:
                goodtitle = self.driver.findElementsByCssSelector("div.good_info  td[class^='el-table_1_column'] p[title]")[num].get_attribute("title")
            except:
                print "title get failed"
            self.driver.ECsclick("div.good_info i.cursor", num)
            elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
            for element in elements:
                if "display" in element.get_attribute("style"):
                    continue
                else:
                    # 点击上架btn
                    self.driver.ECsclick("body>ul>li", 1)
                    try:
                        ele = self.driver.findElementByCssSelector("div.el-message--success p")
                        if ele.text == "操作成功":
                            print "下架成功"
                            logging.info("商品%s下架成功" % goodtitle)
                    except:
                        logging.info("商家下架成功")
    #商品库删除商品
    def test_goods_delete(self):
        # 判断是否有结果
        try:
            nums = self.driver.get_elements_number("tbody>tr")
            print nums
            if nums > 0:
                num = random.randint(0, nums - 1)
                print num
                goodtitle = self.driver.findElementsByCssSelector("div.good_info  td[class^='el-table_1_column'] p[title]")[num].get_attribute("title")
                self.driver.ECsclick("div.good_info i.cursor", num)
                elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
                for element in elements:
                    if "display" in element.get_attribute("style"):
                        continue
                    else:
                        # 点击列表删除btn
                        self.driver.ECsclick("body>ul>li", 3)
                        elements=self.driver.findElementsByCssSelector("div.hptczp_content")
                        for element in elements:
                            if "display" in element.get_attribute("style"):
                                continue
                            else:
                                element.find_element_by_css_selector("div.hptczp_footer button.el-button--primary").click()
                                try:
                                    ele = self.driver.findElementByCssSelector("div.el-message--success p")
                                    if ele.text == "删除成功":
                                        print "删除成功"
                                        logging.info("商品%s删除成功" % goodtitle)
                                except:
                                    logging.info("商家删除商品成功")
        except:
            logging.error("删除商品未执行")

    def tearDown(self):
        self.driver.changewinton(0)
        self.driver.refresh()
        self.driver.wait(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()

#商品审核测试
class bTestconfirmGoods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # dr = DR.driverstart()
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")
        comMethod.bloggin(cls.driver, '13500000070', '123456')
        # cls.driver.ECsends("input", '13500000070', 0)
        # cls.driver.ECsends("input", '123456', 1)
        # cls.driver.ECclick("button")

    def setUp(self):
        t=0
        try:
            self.assertIn("block",self.driver.findElementsByCssSelector("div.content_container")[1].get_attribute("style"))

            print "无需点击菜单"

        except:
            print "点击菜单成功"
            self.driver.ECsclick("div.public_nav", 2)

        self.driver.EPclick("//div[@path='/s/goodList']")
        self.driver.wait(1)
        #点击商品库tab
        self.driver.ECclick("div#tab-second")




    # 待审核商品查询
    def test_good_search(self):
        # 输入框检查
        self.driver.EPsend("//div[@id='pane-second']//input[@placeholder='输入商品名称/编码/条形码/品牌']", "test")
        self.driver.ECclick("div#pane-second button.btn-search")
        self.driver.inputclear("//div[@id='pane-second']//input[@placeholder='输入商品名称/编码/条形码/品牌']", "span")

        self.driver.wait(1)
        # 商品分类
        self.driver.ECclick("div#pane-second span.el-cascader__label")
        self.driver.menu_triple_click("ul[id^='cascader-menu']>li", "ul[id^='menu']>li")
        time.sleep(3)
        # 选择审核状态
        self.driver.ECclick("div#pane-second  div.searchWrap>div.el-select>div.el-input--suffix")
        # 选择商品审核状态
        self.driver.EPsclick("//span[text()='审核状态']/parent::*/following-sibling::li", 1)

        # 选择搜索时间，默认设置：按当天时间取前30天
        enddate = datetime.date.today()
        startdate = enddate + datetime.timedelta(days=-30)
        GSB.time_input(self.driver, " div#pane-second div.el-date-editor input", startdate, enddate)
        self.driver.ECclick("div#pane-second button.btn-search")

    # 查看待审核商品详情
    def test_goods_detail(self):
        # 获取对应点击的商品名称
        goodstitle = self.driver.findElementsByCssSelector("div#pane-second div.good_info  td[class^='el-table_1_column'] p[title]")

        num = random.randint(0, self.driver.get_elements_number("div#pane-second div.good_info i.cursor"))
        print num

        goodtitle = goodstitle[num].get_attribute("title")
        print goodtitle
        self.driver.ECsclick("div#pane-second div.good_info i.cursor", num)

        elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
        for element in elements:
            print element.get_attribute("style")
            if "none" in element.get_attribute("style"):
                continue
            else:
                # 点击详情btn
                self.driver.ECsclick("body>ul>li", 0)
                self.driver.changewinton(1)
        # 获取详情页的商品名称

        try:
            detailgoodtitle = self.driver.findElementsByCssSelector("td.a2>div")[0].text
            print detailgoodtitle
            self.assertEqual(goodtitle, detailgoodtitle, "打开详情页成功")
            logging.info("打开详情页成功")
            # 关闭当前窗口
            self.driver.stopDriver()
            self.driver.changewinton(0)
        except Exception:
            logging.error("打开详情页失败")

    # 待审核商品修改商品
    def test_goods_modify(self):
        try:
            # 获取对应点击的商品名称
            goodstitle = self.driver.findElementsByCssSelector("div#pane-second div.good_info  td[class^='el-table_1_column'] p[title]")

            num = random.randint(0, self.driver.get_elements_number("div#pane-second div.good_info i.cursor")-1)
            print num

            goodtitle = goodstitle[num].get_attribute("title")
            print goodtitle
            self.driver.ECsclick("div#pane-second div.good_info i.cursor", num)

            elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
            for element in elements:
                print element.get_attribute("style")
                if "none" in element.get_attribute("style"):
                    continue
                else:
                    # 点击编辑btn
                    self.driver.ECsclick("body>ul>li", 1)
            self.driver.changewinton(1)
            # 分类、拍获价、供货价、新增规格需要再次审核
            # 修改其他的参数
            # 只改标题
            goodName = goodtitle + str(datetime.datetime.today().strftime("%Y.%m.%d.%H.%m"))
            self.driver.clear("label[for='goodsName']~div input")
            self.driver.ECsend("label[for='goodsName']~div input", goodName)
            path = 'div.poi3 button'
            if self.driver.contain_title("商品修改新增"):
                self.driver.wait(2)
                self.driver.ECclick(path)
        except:
            logging.error("待审核商品修改失败")

    # 商品库删除商品
    def test_goods_delete(self):
        # 判断是否有结果
        try:
            nums = self.driver.get_elements_number("tbody>tr")
            print nums
            if nums > 0:
                num = random.randint(0, nums - 1)
                print num

                self.driver.findElementsByCssSelector("div#pane-second div.good_info  td[class^='el-table_1_column'] p[title]")[num].get_attribute("title")
                self.driver.ECsclick("div#pane-second div.good_info i.cursor", num)
                elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
                for element in elements:
                    if "display" in element.get_attribute("style"):
                        continue
                    else:
                        # 点击列表删除btn
                        self.driver.ECsclick("body>ul>li", 2)
                        elements = self.driver.findElementsByCssSelector("div.hptczp_content")
                        for element in elements:
                            if "display" in element.get_attribute("style"):
                                continue
                            else:
                                #点击确认btn-删除
                                element.find_element_by_css_selector("div.hptczp_footer button.el-button--primary").click()
                                try:
                                    ele = self.driver.findElementByCssSelector("div.el-message--success p")
                                    if ele.text == "删除成功":
                                        print "删除成功"
                                        logging.info("待审核商品删除成功")
                                except:
                                    logging.info("待审核商家删除商品成功")
        except:
            logging.error("删除待审核商品未执行")

    def tearDown(self):
        self.driver.changewinton(0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()

#已删除商品
class bTestdeleteGoods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # dr = DR.driverstart()
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")
        comMethod.bloggin(cls.driver, '13500000070', '123456')
        # cls.driver.ECsends("input", '13500000070', 0)
        # cls.driver.ECsends("input", '123456', 1)
        # cls.driver.ECclick("button")

    def setUp(self):
        try:
            self.assertIn("block;",self.driver.findElementsByCssSelector("div.content_container" )[1].get_attribute("style"))
        except:
            print "点击菜单,展开二级目录"
            self.driver.ECsclick("div.public_nav", 2)
        self.driver.EPclick("//div[@path='/s/goodList']")
        self.driver.wait(1)
        #点击删除tab
        self.driver.ECclick("div#tab-delete")


    # 已删除商品查询-分类和关键字搜索
    def test_good_search(self):
        # 输入框检查
        self.driver.EPsend("//div[@id='pane-delete']//input[@placeholder='输入商品名称/编码/条形码/品牌']", "test")
        self.driver.ECclick("div#pane-delete button.btn-search")
        self.driver.inputclear("//div[@id='pane-delete']//input[@placeholder='输入商品名称/编码/条形码/品牌']", "span")

        self.driver.wait(1)
        # 商品分类
        self.driver.ECclick("div#pane-delete span.el-cascader__label")
        self.driver.menu_triple_click("ul[id^='cascader-menu']>li", "ul[id^='menu']>li")
        self.driver.ECclick("div#pane-delete button.btn-search")

    # 查看待审核商品详情
    def test_goods_detail(self):
        # 获取对应点击的商品名称
        goodstitle = self.driver.findElementsByCssSelector("div#pane-delete div.good_info  td[class^='el-table_1_column'] p[title]")

        num = random.randint(0, self.driver.get_elements_number("div#pane-delete div.good_info i.cursor")-1)
        print num

        goodtitle = goodstitle[num].get_attribute("title")
        print goodtitle
        self.driver.ECsclick("div#pane-delete div.good_info i.cursor", num)

        elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
        for element in elements:
            if "display" in element.get_attribute("style"):
                continue
            else:
                # 点击详情btn
                self.driver.ECsclick("body>ul>li", 0)
                self.driver.changewinton(1)
        # 获取详情页的商品名称
        detailgoodtitle = self.driver.findElementsByCssSelector("td.a2>div")[0].text
        try:
            self.assertEqual(goodtitle, detailgoodtitle, "打开详情页成功")
            logging.info("打开详情页成功")
            # 关闭当前窗口
            self.driver.stopDriver()
            self.driver.changewinton(0)
        except Exception:
            logging.error("打开详情页失败")

    # 商品重新上架
    def test_goods_shelf_again(self):
        # 判断是否有结果
        try:
            nums = self.driver.get_elements_number("tbody>tr")
            print nums
            if nums > 0:
                num = random.randint(0, nums - 1)
                print num
                goodtitle = \
                self.driver.findElementsByCssSelector("div#pane-delete div.good_info  td[class^='el-table_1_column'] p[title]")[num].get_attribute("title")
                self.driver.ECsclick("div#pane-delete div.good_info i.cursor", num)
                elements = self.driver.findElementsByCssSelector("body>ul.el-dropdown-menu")
                for element in elements:
                    if "display" in element.get_attribute("style"):
                        continue
                    else:
                        # 点击列表删除btn
                        self.driver.ECsclick("body>ul>li", 1)
                        elements = self.driver.findElementsByCssSelector("div.hptczp_content")
                        for element in elements:
                            if "display" in element.get_attribute("style"):
                                continue
                            else:
                                #点击确认btn-删除
                                element.find_element_by_css_selector("div.hptczp_footer button.el-button--primary").click()
                                try:
                                    ele = self.driver.findElementByCssSelector("div.el-message--success p")
                                    if ele.text == "操作成功":
                                        print "重新上架成功"
                                        logging.info("商品%s重新成功" % goodtitle)
                                except:
                                    logging.info("商家重新上架商品成功")
        except:
            logging.error("删除待审核商品未执行")

    def tearDown(self):
        self.driver.changewinton(0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()




#商品评价测试
class bTestGoodAppraise(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BO.DriverBase("chrome")
        cls.driver.get_url("http://b.m2c2017final.com")
        comMethod.bloggin(cls.driver, '13500000070', '123456')
    def setUp(self):
        self.driver.ECsclick("div.public_nav", 2)
        if "display" in self.driver.findElementsByCssSelector("div.content_container")[1].get_attribute("style"):
            self.driver.EPclick("//div[@path='/s/goodAppraise']")
        self.driver.wait(1)

    #商品评价搜索
    def test_Reviews_search(self):
        try:
            # 回复状态
            self.driver.ECsclick("div.el-input--suffix",0)
            #0:未回复，1:已回复
            self.driver.EPsclick("//span[text()='回复状态']/parent::*/following-sibling::li",random.randint(0,1))
            # 评价星级
            self.driver.ECsclick("div.el-input--suffix", 1)
            # 0-5，分别是1-5星
            self.driver.EPsclick("//span[text()='评价星级']/parent::*/following-sibling::li", random.randint(0, 4))
            # 选择搜索时间，默认设置：按当天时间取前30天
            enddate = datetime.date.today()
            startdate = enddate + datetime.timedelta(days=-30)
            GSB.time_input(self.driver, "div.searcWrap>div.el-date-editor>input", startdate, enddate)
            #搜索框
            self.driver.ECsend("div.searcWrap>div.el-input>input","test")
            #点击搜索按钮
            self.driver.ECclick("button.btn-search")
        except:
            logging.error("商品评价因某种原因测试搜索失败")



    #回复商品评价
    def test_Reviews_reply(self):
        try:
            # 搜索未回复的评价
            self.driver.ECsclick("div.el-input--suffix", 0)
            # 0:未回复，1:已回复
            self.driver.EPsclick("//span[text()='回复状态']/parent::*/following-sibling::li", 0)
            # 点击搜索按钮
            self.driver.ECclick("button.btn-search")
            self.driver.wait(1)
            num=self.driver.get_elements_number("table>tbody")
            if num>1:
                self.driver.ECsclick("i.icon_hp",random.randint(0,num-1))
                #未进行校验过
                self.driver.ECsend("div.hptczp_body>textarea","UI自动回复自动回复保存")
                self.driver.ECclick("button.save")
            else:
                logging.warning("无需回复的评价")
        except:
            logging.error("不可描述的错误")

    @classmethod
    def tearDownClass(cls):
        cls.driver.stopDriver()


if __name__=='__main__':
    unittest.main()
