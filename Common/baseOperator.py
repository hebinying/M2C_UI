#coding=utf-8
'''重新封装基础方法，方便调用'''
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import random


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
        print "wo be here"
        return elements


    def ECclick(self,name):

        element=self.findElementByCssSelector(name)

        WebDriverWait(self.driver, 10,0.5).until(EC.visibility_of(element))
        if element:
            element.click()

        else:
            print "元素未查找到"

    def ECsclick(self,name,num):
        elements=self.findElementsByCssSelector(name)

        if elements[num]:
            #WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of(elements[num]))
            elements[num].click()
            print "click success"
        else:
            print "元素未查找到"

    '''根据id'''
    def EIclick(self,id):
        element=self.findElementByID(id)
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of(element))
        if element:
            element.click()
        else:
            print "元素未查找到"

    def EPclick(self,path):
        element=self.findElementByPath(path)
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of(element))
        if element:
            element.click()
        else:
            print "元素未查找到"

    def EPsclick(self,path,num):
        elements=self.findElementsByPath(path)
        if elements:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of(elements[num]))
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
            element.send_keys(text)

    def EIsend(self,id,text):
        element=self.findElementByID(id)
        if element:
            element.send_keys(text)
        else:
            print "%s is not found" %id
    def EPsend(self,path,text):
        element=self.findElementByPath(path)
        if element:
            element.send_keys(text)
        else:
            print "element %s is not found" %path
    def EPsends(self,path,text,num=-1):
        elements=self.findElementsByPath(path)
        try :
            if num==-1:
                num=random.randint(0,len(elements))
                elements[num].send_keys(text)
            else:
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
