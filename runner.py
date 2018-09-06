#coding=utf-8
from unittest import TestLoader,TestCase,TestSuite,TestResult
import unittest
import HTMLTestRunner
from m2c_merchant import bLogin
from m2c_merchant import BULogin
from excute import getSuite as be
import m2c_merchant
import smtplib
import Report
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





def sendEmail():
    sender='heby@m2c2017.com'
    passwd='UZw3WKwVHetaABBm'
    #passwd = '080608Hby'
    receivers='heby@m2c2017.com'
    subject='邮件测试'
    msg=MIMEMultipart()
    msg['Subject']=subject
    msg['From']=sender
    msg['To']=receivers

    msg.attach(MIMEText('Python发送附件邮件测试','plain','utf-8'))
    file='Report/htmlreport.html'
    print file
    attr1=MIMEText(open(file,'rb').read(),'html','base64')
    attr1["Content-Deisposition"]='attachment;filename="text.html"'
    msg.attach(attr1)
    attr2=MIMEText(open(file,'rb').read(),'html','base64')
    attr1["Content-Deisposition"] = 'attachment;filename="text2.html"'
    msg.attach(attr2)
    try:
        s=smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
        s.set_debuglevel(1)
        s.login(sender,passwd)
        s.sendmail(sender,receivers,msg.as_string())
        print "success"
    except:
        print "failed"

        '''file="./config/sendToEmail.txt"
    fp=open(file).readlines()

    email=[]
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


