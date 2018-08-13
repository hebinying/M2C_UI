#coding=utf-8
'''重新封装基础方法，方便调用'''
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import time


class DriverBase:
    #初始化driver
    def __init__(self,driver):
        self.driver=driver


    def get_url(self,url):
        self.driver.maximize_window()
        self.driver.get(url)
        '''设置窗口为最大'''

    #关闭浏览器
    def stopDriver(self):
        os.system("Stop Driver")
        self.driver.close()

    def findElementByID(self,ID):
        element=self.driver.find_element_by_id(ID)
        return element

    def findElementByName(self,Name):
        element=self.driver.find_element_by_name(Name)
        return element

    def findElementByClassName(self,cName):
        element=self.driver.find_element_by_class_name(cName)
        return element

    def findElementByTagName(self,tag):
        element=self.driver.find_element_by_tag_name(tag)
        return element

    def findElementByPath(self,path):
        element=self.driver.find_element_by_xpath(path)
        return element

    def findElementByCssSelector(self,ele):
        element=self.driver.find_element_by_css_selector(ele)
        return element

    def findElementsByID(self, ID):
        elements = self.driver.find_element_by_id(ID)
        return elements

    def findElementsByName(self, Name):
        elements = self.driver.find_element_by_name(Name)
        return elements

    def findElementsByClassName(self,cName):
        time.sleep(10)
        elements = self.driver.find_elements_by_class_name(cName)
        return elements

    def findElementsByTagName(self, tag):
        elements = self.driver.find_elements_by_tag_name(tag)
        return elements


    def findElementsByPath(self,path):
        elements=self.driver.find_elements_by_xpath(path)
        return elements

    def findElementsByCssSelector(self,ele):
        elements=self.driver.find_elements_by_css_selector(ele)
        print "wo be here"
        return elements


    def ECclick(self,name):
        element=self.findElementByCssSelector(name)
        if element:
            element.click()
        else:
            print "元素未查找到"

    def ECsclick(self,name,num):
        elements=self.findElementsByCssSelector(name)
        if elements[num]:
            elements[num].click()
        else:
            print "元素未查找到"

    '''根据id'''
    def EIclick(self,id):
        element=self.findElementByID(id)
        if element:
            element.click()
        else:
            print "元素未查找到"

    def EPclick(self,path):
        element=self.findElementByPath(path)
        if element:
            element.click()
        else:
            print "元素未查找到"

    def EPsclick(self,path,num):
        elements=self.findElementsByPath(path)
        if elements:
            elements[num].click()
        else:
            print "元素未查找到"

    '''选项卡的切换'''
    def changewintofirst(self):
        self.driver.switch_to_window(self.driver.window_handles[0])

    def changewinton(self,n):
        self.driver.switch_to_window(self.driver.window_handles[n])

    '''获取浏览器的选项卡数量'''
    def get_handles(self):
        num=self.driver.window_handles()
        return num

    def ECsend(self,element,text,num):
        elements=self.findElementsByCssSelector(element)
        print elements
        if num:
            elements[num].send_keys(text)
        else:
            num=0
            elements[num].send_keys(text)

    def EIsend(self,id,text):
        element=self.findElementByID(id)
        if element:
            element.send_keys(text)
        else:
            print "%s is not founf" %id

    def get_title(self):
        title=EC.get_title()(self.driver)
        return title
    def contain_title(self,text):
        flag=EC.title_contains(text)(self.driver)
        return flag

