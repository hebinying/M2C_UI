#coding=utf-8
from unittest import TestLoader
from unittest import TestSuite
import logging
import re
import m2c_merchant
from m2c_merchant import BULogin
#通过文件路径及py的文件名过滤，并返回TestSuite
def getTestSuite_by_dicover(filename=None,keys='*.py'):
    try:
        # suite=TestLoader().discover(filename,keys)
        # print suite
        suit=TestLoader().discover(filename,keys)
        logging.info("Found testcase in %s" %filename)
        return suit
    except:
        logging.info("Did not found %s in %s" %keys %filename)

def getTestSuite_by_CaseClass(testCaseClasses):
    case=[]
    suite = TestLoader().loadTestsFromTestCase(testCaseClasses)
    # for i in range(0, len(testCaseClasses)):
    #     #cls=re.findall(r"'([^']+)'",testCaseClasses[i])
    #     #cls=testCaseClasses[i].split('\'')
    #     #m = re.findall('"([^"]+)"', str1)
    #     #print cls[0]
    #     cls=testCaseClasses[i]
    #     # print cls,type(cls)
    #     suite=TestLoader().loadTestsFromTestCase(cls)
    #     case.append(suite)
    #     # try:
    #     #     suit.append(TestLoader.loadTestsFromTestCase(testCaseClasses[i]))
    #     #     logging.info("Found testcaseclass throud %s" % testCaseClasses[i])
    #     # except:
    #     #     logging.info("Not found testcaseclass throud %s" %testCaseClasses[i])
    #     #     continue
    # suit = TestSuite(case)
    # print suit
    return suite
    # try:
    #     for i in range(0,len(testCaseClasses)):
    #         print testCaseClasses[i]
    #         case.append(TestLoader.loadTestsFromTestCase(testCaseClasses[i]))
    #         print case
    #         # try:
    #         #     suit.append(TestLoader.loadTestsFromTestCase(testCaseClasses[i]))
    #         #     logging.info("Found testcaseclass throud %s" % testCaseClasses[i])
    #         # except:
    #         #     logging.info("Not found testcaseclass throud %s" %testCaseClasses[i])
    #         #     continue
    #     suit=TestSuite(case)
    #     print suit
    #     return suit
    # except:
    #     logging.info("testcaseclass %s is None" %testCaseClasses)

#通过文件名来获取suit集合 module=[]
def getTestSuite_by_Module(module):
    suit=[]
    try:
        for m in range(0,len(module)):
            print module[m]
            suit1=TestLoader().loadTestsFromModule(module[m])
            print suit1
            suit.append(suit1)

        return suit
    except:
        logging.info("module not found" )

#通过名称集合
# loadTestsFromName 通过单一name查找

def getTestSuite_by_Name(names=None):
    suite=[]
    try:
        for i in range(0,len(names)):
            try:
                suite.append(TestLoader().loadTestsFromNames(names[i][0],names[i][1]))

            except:
                #日志标记，有可能出错
                logging.info("%s not found" %names[i])
                continue
        return suite
    except:
        logging.info("names not found")












