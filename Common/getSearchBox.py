#coding=utf-8

import baseOperator


driver=baseOperator.DriverBase()
def getSearchBox():
    element=driver.findElementByCssSelector("高级搜索")
    element.click()

def clickBoxelement():
    elements=driver.findElementsByCssSelector()
