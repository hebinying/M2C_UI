#coding=utf-8
'''重新封装基础方法，方便调用'''
import sys
import os
from selenium import webdriver

class DriverBase:
    #初始化driver
    def __init__(self,driver,url):
        self.driver=driver
        self.driver.get(url)
        '''设置窗口为最大'''
        self.driver.maximize_window()

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

    def findElementsByClassName(self, cName):
        elements = self.driver.find_element_by_class_name(cName)
        return elements

    def findElementsByTagName(self, tag):
        elements = self.driver.find_element_by_tag_name(tag)
        return elements


    def findElementsByPath(self,path):
        elements=self.driver.find_element_by_xpath(path)
        return elements

    def findElementsByCssSelector(self,ele):
        elements=self.driver.find_element_by_css_selector(ele)
        return elements


    def click(self,element):
        if any(element):
            element.click()
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

    def send(self,name):
        self.driver.send_key(name)
