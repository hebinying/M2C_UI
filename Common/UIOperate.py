#coding=utf-8
import baseOperator
import time


driver=baseOperator.DriverBase()
def get_elements(path):
    if "商家平台" in driver.title:
        print driver.title
        elements=driver.findElementsByPath(path)
        for i in range[0,len(elements)]:
            elements[i].click()
            try:
                elements2=elements[i].findElementsByPath("//div[@class='content_s']")
                for j in range(0, len(elements2)):
                    elements2[j].click()
                    print elements2[j].text
                    time.sleep(1)
                    '''遍历页面内容按钮，设置规则'''
            except:
                print "无下级目录"
                return

    elif "管理平台" in driver.title:
        print driver.title
        '''遍历主目录及子目录'''

    elif "场景平台" in driver.title:
        print driver.title
        '''编辑场景平台'''

    else:
        print "%s非后台项目"  %driver.title






