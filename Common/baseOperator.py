'''重新封装基础方法，方便调用'''
import sys
import os
from selenium import webdriver

class DriverBase:
    #初始化driver
    def __init__(self,driver):
        self.driver=driver

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

    def click(self,element):
        if any(element):
            element.click()
        else:
            print "元素未查找到"




