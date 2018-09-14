#coding=utf-8

import baseOperator
import datetime

def getSearchBox(driver):
    element=driver.findElementByCssSelector("高级搜索")
    element.click()

def clickBoxelement(driver):
    elements=driver.findElementsByCssSelector()


#时间控件输入,设置默认时间为今天，前一天
def time_input(driver,cssname,startdate=datetime.date.today()-datetime.timedelta(days=-1),enddate=datetime.date.today()):
    driver.ECsends(cssname,str(startdate),0)
    driver.ECsends(cssname,str(enddate),1)
