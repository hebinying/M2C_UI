from unittest import TestLoader,TestCase,TestSuite,TestResult
import unittest
import HTMLTestRunner
from m2c_merchant import bLogin
from m2c_merchant import BULogin
from excute import getSuite as be
import m2c_merchant


def sendEmail():
    file="./config/sendToEmail.txt"
    fp=open(file).readlines()

    '''email=[]
    print fp
    for line in range(0,len(fp)):
        a=fp[line].split('<'or '>')
        print a[1]
        email.append(a[1])

    print email'''





if __name__=="__main__":
   sendEmail()

   """
    fp=file("./Report/htmlreport.html","wb")
test_runner=HTMLTestRunner.HTMLTestRunner(fp)
case=be.getTestSuite("m2c_merchant",'*.py')

test_runner.run(case)
 names=['m2c_merchant.BULogin.BULogin.test_acheck','m2c_merchant.BULogin.BULogin.test_ChangecashPass']
 test_case=TestLoader().loadTestsFromNames(names)
 
 test_case=TestLoader().loadTestsFromModule(BULogin)
print test_case
suite1 = TestLoader().loadTestsFromTestCase(bLogin.BLogin)
    suite2 = TestLoader().loadTestsFromTestCase(BULogin.BULogin)
    case = TestSuite([suite1, suite2])

   
    print suite1
    print suite2
    
    print case'''"""


