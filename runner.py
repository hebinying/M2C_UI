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
from xml.dom import minidom
import xml.dom.minidom
from unittest import TestLoader
from excute.getSuite import getTestSuite_by_dicover
import logging
from email import Utils
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from Common import file_excute
import time,datetime
import os




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

CaseConfig=r"./config/casesconfig.xml"
def commTestSuite():
    xmlHeader=""
    xmlDescrip=""
    xmlmethod = ""
    xmlPath = ""
    xmlPattern = ""
    xmlCaseClass = []
    xmlToPath = ""
    xmlTestSuite = []
    xmlProducer = ""

    xmlFile = CaseConfig

    # 解析xml文件
    xmlFeed = xml.dom.minidom.parse(xmlFile)
    print "OK"
    xmlNode = xmlFeed.getElementsByTagName("Testcase")
    # xmlTestName=xmlFeed.getElementsByTagName("TestName")
    # xmlLoadMethod=xmlFeed.getElementsByTagName("LoadMethod")
    # xmlTestsuite=xmlFeed.getElementsByTagName("Testsuite")

    # print xmlNode
    for node in xmlNode:
        print node
        # xmlNode =node.getElementsByTagName("Testcase")
        xmlTestName = node.getElementsByTagName("TestName")
        xmlLoadMethod = node.getElementsByTagName("LoadMethod")
        xmlTestsuite = node.getElementsByTagName("Testsuite")
        xmlProducer = node.getElementsByTagName("Producer")
        xmlReportTo = node.getElementsByTagName("To")

        xmlHeader = xmlTestName[0].getAttribute("name")
        xmlDescrip = xmlTestName[0].getAttribute("decription")
        xmlmethod = xmlLoadMethod[0].getAttribute("method")
        print xmlmethod
        xmlProducer = xmlProducer[0].getAttribute("name")
        # 报告生成路径
        xmlToPath = xmlReportTo[0].getAttribute("path")
        path = xmlToPath + '/' + xmlHeader + '.html'
        fp = open(path, "wb")
        print xmlHeader, xmlDescrip


        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=1, title=xmlHeader, description=xmlDescrip)

        if xmlmethod == "discover":
            xmlPath = xmlTestsuite[0].getAttribute("path")
            xmlPattern = xmlTestsuite[0].getAttribute("pattern")
            suite=getTestSuite_by_dicover(filename=xmlPath,keys=xmlPattern)
            #result = runner.run(suite)
        # elif xmlmethod == "TestCase":
        #     pass
        # elif "module"==xmlmethod:
        #     print xmlTestsuite[0]
        #     xmlpath=xmlTestsuite[0].getAttribute("file")
        #     print xmlpath
        #     result=openfile(xmlpath)
        #     result1=[m2c_merchant.bLogin,m2c_merchant.BULogin]
        #     for i in result:
        #         print type(i)
        #         #存在传参类型问题
        #         suite=TestLoader().loadTestsFromModule(i)
        #         a=m2c_merchant.bLogin
        #         print type(a)
        #         print TestLoader().loadTestsFromModule(a)
        #         print suite
        #         runner.run(suite)
        #     # suite=getTestSuite_by_Module(result)
        #     # print suite
        # elif "Names" in xmlmethod:
        #     pass
        # elif "CaseNames" in xmlmethod:
        #     pass
        else:
            print "其他方法暂未实现"
            break
        runner.run(suite)
        # print result.success_count
        # print result.failure_count
        fp.close()
        #HTMLReportRun(xmlHeader,xmlDescrip,xmlToPath,suite)

    # xmlTestName =xmlFeed.getElementsByTagName("TestName")

#
# def HTMLReportRun(name,descri,RTo,suite):
#     path=RTo+'/'+name+'.html'
#     fp=file(path,"wb")
#     print suite
#     runner=HTMLTestRunner.HTMLTestRunner(fp)
#     runner.run(suite)
emailConf = r".\config/email_cofig.xml"

class CommEmail:

    def __init__(self):

        # init
        self.sIp = ""
        self.sPort = ""
        self.sUser = ""
        self.sPassword = ""
        self.fEmailServerConfFile = ""
        self.fEmailTemplateFile = ""
        self.sEmailOwner = ""
        self.dEmailTo = []
        self.dEmailCC = []
        self.dattach = []
        self.sSubject = ""
        self.emComment = []
        self.tDate = Utils.formatdate(localtime=1)
        # logging.basicConfig(level=logging.DEBUG,
        #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        #                     datefmt='%a, %d %b %Y %H:%M:%S',
        #                     filename='Email.log',
        #                     filemode='a')

        # from conf-profile to set email-server  configure
        self.fEmailServerConfFile=emailConf

        try:
            xmlFeed = xml.dom.minidom.parse(self.fEmailServerConfFile)
            xmlEmaiSMTP = xmlFeed.getElementsByTagName('smtp')
            xmlEmailFrom = xmlFeed.getElementsByTagName('From')
            xmlEmaiTos = xmlFeed.getElementsByTagName('To')
            # xmlEmaiCCs = xmlFeed.getElementsByTagName('CC')
            xmlEmailSubject = xmlFeed.getElementsByTagName('Subject')
            xmlEmailComments = xmlFeed.getElementsByTagName('comment')
            xmlEmailattachs = xmlFeed.getElementsByTagName('attach')

            # only one smtp-tag
            for smtpConf in xmlEmaiSMTP:
                self.sIp = smtpConf.getAttribute("ip")
                self.sPort = smtpConf.getAttribute("port")
                self.sUser = smtpConf.getAttribute("user")
                self.sPassword = smtpConf.getAttribute("password")

            # To
            for To in xmlEmaiTos:
                file = To.getAttribute("file")
                results = file_excute.openfile(file)
                for result in results:
                    #print result
                    self.dEmailTo.append(result)
            #print self.dEmailTo
            # CC
            # for cc in xmlEmaiCCs:
            # self.dEmailCC.append(cc.getAttribute("address"))

            # From & Subject
            self.sEmailOwner = xmlEmailFrom[0].getAttribute("address")
            self.sSubject = xmlEmailSubject[0].getAttribute("title")

            # self.emComment = open(xmlEmailComments[0].getAttribute("file")).read()
            # comment邮件内容
            for comment in xmlEmailComments:
                cfile = comment.getAttribute("file")
                results = file_excute.get_file(cfile, '.html','2018-09-12')
                for result in results:
                    print result
                    self.emComment.append(open(result).read())

            # attach
            # for attach in xmlEmailattachs:
            #   self.dattach.append(attach.getAttribute("file"))
            for attach in xmlEmailattachs:
                cfile = attach.getAttribute("file")
                #获取今天执行的报告
                results = file_excute.get_file(cfile, '.html')
                for result in results:
                    print result
                    self.dattach.append(result)

            logging.info(
                "smtp conf ====> ip: " + self.sIp + " " + "port: " + self.sPort + " " + "user: " + self.sUser + " password: " + self.sPassword)
            logging.info("init end")
        except:
            logging.warning("ERROR: EmailServerConfFile is ERROR !!!")
            logging.warning("exit(1) from __init__")
            exit(1)
    # get html commtent

    # email comment & sendmail
    def sendHtmlEmail(self):
        msg = MIMEMultipart()
        #msg["Subject"] = self.sSubject+str(time.strftime("%Y-%m-%d",time.localtime((int(time.time()*1000))/1000)))
        msg["Subject"]=self.sSubject+str(datetime.datetime.now().strftime("%Y-%m-%d"))
        msg["From"] = self.sEmailOwner
        msg["To"] = ";".join(self.dEmailTo)
        msg["CC"] = ";".join(self.dEmailCC)
        msg["Date"] = self.tDate

        # email comment
        for comment in self.emComment:
            emailComment=MIMEText(comment, _subtype="html", _charset='utf-8')
            msg.attach(emailComment)
        #emailComment = MIMEText(self.emComment, _subtype="html", _charset='base64')
        # add eamil attach
        print "ssss"
        for attach in self.dattach:
            #t = MIMEBase('application', 'octet-stream')
            print attach
            t = MIMEBase('html', 'utf-8')
            t.set_payload(open(attach, 'rb').read())
            #encoders.encode_base64(t)
            #邮件的文件名标题不能太长，否则会添加失败
            t.add_header('Content-Disposition', 'attachment;filename="%s"' % os.path.basename(attach))
            #t.add_header('Content-Disposition', 'attachment;filename="discover.html"')
            msg.attach(t)

        try:
            #msg.attach(emailComment)
            emailHandle = smtplib.SMTP_SSL()
            emailHandle.set_debuglevel(1)
            emailHandle.connect('smtp.exmail.qq.com', int(self.sPort))
            emailHandle.login(self.sUser, self.sPassword)
            #发送邮件
            emailHandle.sendmail(msg["From"], msg["To"].split(';'), msg.as_string())

            emailHandle.quit()
            emailHandle.close()
            logging.info("Email for test was send")
        except:
            logging.warning("Error")
            exit(1)




if __name__=="__main__":
    print "start"
    formater='%(asctime)s %(process)d:%(pathname)s %(filename)s[line:%(lineno)d]  %(module)s %(funcName)s %(levelname)s %(message)s'
    logname="./Report/log"+datetime.datetime.now().strftime("%Y%m%d")+".log"
    infoLogname="./Report/infolog"+datetime.datetime.now().strftime("%Y%m%d")+".log"
    errorLogname="./Report/errorlog"+datetime.datetime.now().strftime("%Y%m%d")+".log"
    logging.basicConfig(level=logging.NOTSET,
                        format=formater,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=logname,
                        filemode='a')
    #a添加，w覆盖
    # infoformat=logging.Formatter(formater)
    # infoLogger=logging.getLogger("a")
    # errorLogger=logging.getLogger("b")
    # infoLogger.setLevel(logging.DEBUG)
    # errorLogger.setLevel(logging.ERROR)
    #
    # infoHandler=logging.FileHandler(infoLogname,'w')
    # infoHandler.setLevel(logging.DEBUG)
    # infoHandler.setFormatter(infoformat)
    #
    # errorHandler=logging.FileHandler(errorLogname,'w')
    # errorHandler.setLevel(logging.ERROR)
    # errorHandler.setFormatter(infoformat)
    #
    # infoLogger.addHandler(infoHandler)
    # errorLogger.addHandler(errorHandler)

    commTestSuite()
    #发送邮件
    # a = CommEmail()
    # a.sendHtmlEmail()
