#coding=utf-8
'''重新封装基础方法，方便调用'''
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import random,logging


class DriverBase:
    #初始化driver
    def __init__(self,devices):

        if devices == 'firefox' or devices == 'Firefox':
            driver = webdriver.Firefox()
        elif devices == 'chrome' or devices == 'Chrome':
            driver = webdriver.Chrome()
        elif devices == 'ie' or devices == 'IE' or devices == 'IE':
            driver = webdriver.Ie()
        else:
            print "Not found suitable browser"
            exit(0)
        self.driver=driver
        self.action=ActionChains(driver)
    def get_url(self,url):
        self.driver.maximize_window()
        self.driver.get(url)
        '''设置窗口为最大'''

    #关闭浏览器
    def stopDriver(self):
        os.system("Stop Driver")
        self.driver.close()


    def findElementByID(self,ID):
        #self.driver.timeouts().implicitlyWait(10)
        element=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_id(ID))
        #element=self.driver.find_element_by_id(ID)
        return element

    def findElementByName(self,Name):
        '''locater=(By.NAME,Name)
        WebDriverWait(self.driver,20,1).until(EC.presence_of_element_located(locater))'''
        element=self.driver.find_element_by_name(Name)
        return element

    def findElementByClassName(self,cName):
        '''locater = (By.CLASS_NAME, cName)
        WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located(locater))'''
        element=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_class_name(cName))
        #element=self.driver.find_element_by_class_name(cName)
        return element

    def findElementByTagName(self,tag):
        '''locater = (By.TAG_NAME, tag)
        WebDriverWait(self.driver, 20, 2).until(EC.presence_of_element_located(locater))'''
        element=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_tag_name(tag))
        #element=self.driver.find_element_by_tag_name(tag)
        return element

    def findElementByPath(self,path):
        element=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath(path))
        #element=self.driver.find_element_by_xpath(path)
        return element

    def findElementByCssSelector(self,ele):
        '''str=ele.split('.')
        if len(str)>1:
            locater=(By.CLASS_NAME,str[1])
        else:
            locater=(By.CLASS_NAME,ele)
        WebDriverWait(self.driver, 20, 2).until(EC.presence_of_element_located(locater))'''
        element=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_css_selector(ele))
        #element=self.driver.find_element_by_css_selector(ele)
        return element

    def findElementsByID(self, ID):
        '''locater=(By.ID,ID)
        WebDriverWait(self.driver, 20, 2).until(EC.presence_of_element_located(locater))'''
        elements = self.driver.find_element_by_id(ID)
        return elements

    def findElementsByName(self, Name):
        elements = self.driver.find_element_by_name(Name)
        return elements

    def findElementsByClassName(self,cName):
        elements=WebDriverWait(self.driver,10).until(lambda x:x.find_elements_by_class_name(cName))
        #elements = self.driver.find_elements_by_class_name(cName)
        return elements

    def findElementsByTagName(self, tag):
        elements = self.driver.find_elements_by_tag_name(tag)
        return elements


    def findElementsByPath(self,path):
        elements=WebDriverWait(self.driver,10).until(lambda x:x.find_elements_by_xpath(path))

        #elements=self.driver.find_elements_by_xpath(path)
        return elements

    def findElementsByCssSelector(self,ele):
        elements=WebDriverWait(self.driver,10).until(lambda x:x.find_elements_by_css_selector(ele))
        #elements=self.driver.find_elements_by_css_selector(ele)
        #print "wo be here"
        return elements


    def ECclick(self,name):

        element=self.findElementByCssSelector(name)

        WebDriverWait(self.driver, 10,0.5).until(EC.visibility_of(element))
        if element:
            self.action.move_to_element(element)
            element.click()

        else:
            print "元素未查找到"

    def ECsclick(self,name,num):
        elements=self.findElementsByCssSelector(name)

        if elements[num]:
            self.action.move_to_element(elements[num])
            #self.wait(WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable(elements[num])))
            elements[num].click()
            print "click success"
        else:
            print "元素未查找到"

    '''根据id'''
    def EIclick(self,id):
        element=self.findElementByID(id)
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of(element))
        if element:
            self.action.move_to_element(element)
            element.click()
        else:
            print "元素未查找到"

    def EPclick(self,path):
        element=self.findElementByPath(path)
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of(element))
        if element:
            self.action.move_to_element(element)
            element.click()
        else:
            print "元素未查找到"

    def EPsclick(self,path,num):
        elements=self.findElementsByPath(path)
        if elements:
            WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of(elements[num]))
            try:
                self.action.move_to_element(elements[num])
                elements[num].click()
            except WebDriverException:
                pass
        else:
            print "元素未查找到"

    #获取元素的数量 @bebinn @0915
    def get_elements_number(self,name,method='css'):
        if method=='css':
            elements=self.driver.find_elements_by_css_selector(name)
        elif method=='path':
            elements=self.driver.find_elements_by_xpath(name)
        elif method=='tagname':
            elements=self.driver.find_elements_by_tag_name(name)
        elif method=='classname':
            elements=self.driver.find_elements_by_class_name(name)
        else:
            print "method error,now can find elements by css,path,tagname,classname"

        return len(elements)
    '''选项卡的切换'''
    def changewintofirst(self):
        self.driver.switch_to_window(self.driver.window_handles[0])

    def changewinton(self,n):
        self.driver.switch_to_window(self.driver.window_handles[n])

    '''获取浏览器的选项卡数量'''
    def get_handles(self):
        handles=self.driver.window_handles
        return handles
    '''
    @bebinn
    @0915
    切换iframe、脚本执行'''
    def switch_to_iframe(self,name):
        self.driver.switch_to_frame(name)

    def excute_js(self,js):
        try:
            self.driver.execute_script(js)
        except:
            print "执行失败"
    def ECsends(self,element,text,num):
        elements=self.findElementsByCssSelector(element)
        print elements
        if elements:
            elements[num].send_keys(text)
        else:
            print "element %s is not found" % element
    def ECsend(self,element,text):
        element=self.findElementByCssSelector(element)
        if element:
            self.action.move_to_element(element)
            element.send_keys(text)

    def EIsend(self,id,text):
        element=self.findElementByID(id)
        if element:
            self.action.move_to_element(element)
            element.send_keys(text)
        else:
            print "%s is not found" %id
    def EPsend(self,path,text):
        element=self.findElementByPath(path)
        if element:
            self.action.move_to_element(element)
            element.send_keys(text)
        else:
            print "element %s is not found" %path
    def EPsends(self,path,text,num=-1):
        elements=self.findElementsByPath(path)
        try :
            if num==-1:
                num=random.randint(0,len(elements))
            self.action.move_to_element(elements[num])
            elements[num].send_keys(text)
        except:
            print "element %s is not found" %path


    def get_title(self):
        title=EC.get_title()(self.driver)
        return title
    def contain_title(self,text):
        flag=EC.title_contains(text)(self.driver)
        return flag

    def wait(self,s):
        time.sleep(s)
    def back(self):
        self.driver.back()

    #模拟鼠标操作点击'x'btn，xpath方法查找元素
    def inputclear(self,p,name):
        path=p+'/following-sibling::'+name
        #激活输入框
        self.EPclick(p)
        #点击删除icon
        self.EPclick(path)
        # element.click()
        # element.clear()

    #鼠标悬停
    def action_perfom(self,ele):
        action = ActionChains(self.driver)
        action.click(ele).perform()

    def click(self,ele,num=-1):
        if num==-1:
            num=random(len(ele))
            ele[num].click()
        ele[num].click()

    '''三级联动点击
    缺少超边框后的的数据添加
    @bebinn
    @20180913'''
    def menu_triple_click(self,first,second=None):

        firstnum=self.findElementsByCssSelector(first)
        randnum = random.randint(0,len(firstnum)-1)
        action=ActionChains(self.driver)
        #方法二：通过判断class是否包含el-cascader-menu__item--extensible，有：含下一级，无：无下一级
        if firstnum[randnum].is_displayed()==True:
            action = ActionChains(self.driver)
            action.move_to_element(firstnum[randnum]).perform()
            firstnum[randnum].click()
        else:
            WebDriverWait(self.driver,10,0.5).until(EC.visibility_of(firstnum[randnum]))
            firstnum[randnum].click()
        if "el-cascader-menu__item--extensible" in firstnum[randnum].get_attribute("class"):

            secondnum=self.findElementsByCssSelector(second)
            randnum2=random.randint(0,len(secondnum)-1)
            WebDriverWait(self.driver,10).until(EC.visibility_of(secondnum[randnum2]))
            self.ECsclick(second,randnum2)
            if "el-cascader-menu__item--extensible" in secondnum[randnum2].get_attribute("class"):
                thirdnum=self.findElementsByCssSelector(second)
                randnum3=random.randint((len(thirdnum)-len(secondnum)),len(thirdnum)-1)
                self.ECsclick(second,randnum3)
        #方法一
        # if firstnum>1:
        #     self.ECsclick(first,random(0,len(firstnum)))
        #     secondnum=self.findElementsByCssSelector(second)
        #     if secondnum>1:
        #         self.ECsclick(second,random(0,len(secondnum)))
        #     third=second.split('>')
        #     elements = self.findElementsByCssSelector(third[0])
        #     if len(elements) > 1:
        #         ids = elements[0].get_attribute("id").split('-')
        #         ids2 = ""
        #         for i in range(0, len(ids) - 1):
        #             print ids[i]
        #             if i == 0:
        #                 ids2 = ids[i]
        #             else:
        #                 ids2 += '-' + ids[i]
        #         print ids2
        #         ids2 += '-2'
        #         print ids2
        #         name = "ul#" + ids2 + ">li"
        #         thirdnum=self.findEle mentsByCssSelector(name)
        #         self.ECsclick(name, random(len(thirdnum)))

    '''
    #增加页面刷新
    @bebinn
    @20180914'''
    def refresh(self):
        self.driver.refresh()

    #判断是否包含某个元素的内容
    def assert_text(self,path,text):
        WebDriverWait(self.driver, 10, 0.5).until(EC.text_to_be_present_in_element(self.driver.findElementsByCssSelector("div.el-message>p").text),text)

