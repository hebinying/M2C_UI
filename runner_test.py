#! /usr/bin/env python
# coding:utf-8

import os, string, sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email import Utils
from email.mime.base import MIMEBase
from email import encoders
from xml.dom import minidom
import xml.dom.minidom
import logging
from email.mime.text import MIMEText
from Common import file_excute
import time,datetime

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
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(                                                                                                                                                                                               levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='Email.log',
                            filemode='a')

        # from conf-profile to set email-server  configure
        self.fEmailServerConfFile=emailConf

        '''
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
:
        self.tDate = Utils.formatdate(localtime=1)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='Email.log',
                            filemode='a')

        # from conf-profile to set email-server  configure
        self.fEmailServerConfFile=emailConf

        '''
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
                # print result
                self.dEmailTo.append(result)
        # print self.dEmailTo
        # CC
        # for cc in xmlEmaiCCs:
        # self.dEmailCC.append(cc.getAttribute("address"))

        # From & Subject
        self.sEmailOwner = xmlEmailFrom[0].getAttribute("address")
        self.sSubject = xmlEmailSubject[0].getAttribute("title")

        #self.emComment = open(xmlEmailComments[0].getAttribute("file")).read()
        #comment邮件内容
        for comment in xmlEmailComments:
            cfile=comment.getAttribute("file")
            results=file_excute.get_file(cfile,'.html')
            for result in results:
                self.emComment.append(open(result).read())

        # attach
        #for attach in xmlEmailattachs:
         #   self.dattach.append(attach.getAttribute("file"))
        for attach in xmlEmailattachs:
            cfile = attach.getAttribute("file")
            results = file_excute.get_file(cfile, '.html')
            for result in results:
                self.dattach.append(result)

        '''
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
                results = file_excute.get_file(cfile, '.html')
                for result in results:
                    self.emComment.append(open(result).read())

            # attach
            # for attach in xmlEmailattachs:
            #   self.dattach.append(attach.getAttribute("file"))
            for attach in xmlEmailattachs:
                cfile = attach.getAttribute("file")
                results = file_excute.get_file(cfile, '.html')
                for result in results:
                    self.dattach.append(result)

            logging.info(
                "smtp conf ====> ip: " + self.sIp + " " + "port: " + self.sPort + " " + "user: " + self.sUser + " password: " + self.sPassword)
            logging.info("init end")
        except:
            logging.warning("ERROR: EmailServerConfFile is ERROR !!!")
            logging.warning("exit(1) from __init__")
            exit(1)

    '''
    #for email-server test
    def testEmaileServer(self):
        emailHandle = smtplib.SMTP(self.sIp,int(self.sPort))
        emailHandle.login(self.sUser, self.sPassword)
        msg = "To: aaa@bb.com \nFrom: aaa@bb.com \nSubject:testing \n" #header
        msg = "\nthis is test msg\n\n"
        emailHandle.sendmail("aaa@bb.com", "aaa@bb.com", msg)
        emailHandle.quit()
        #logging.INFO(" Email for test was send." )


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
        for a in self.dattach:
            # t = MIMEBase('application', 'octet-stream')
            t = MIMEBase('html', 'base64')
            t.set_payload(open(a, 'rb').read())
            # encoders.encode_base64(t)
            t.add_header('Content-Disposition', 'attachment;filename="%s"' % os.path.basename(a))
            print t
            msg.attach(t)

        try:
            #msg.attach(emailComment)
            emailHandle = smtplib.SMTP_SSL()
            emailHandle.set_debuglevel(1)
            emailHandle.connect('smtp.exmail.qq.com', int(self.sPort))
            emailHandle.login(self.sUser, self.sPassword)
            emailHandle.sendmail(msg["From"], msg["To"].split(';'), msg.as_string())
            emailHandle.quit()
            emailHandle.close()
            logging.info("Email for test was send")
        except:
            logging.warning("Error")
            exit(1)
        '''
        #SSL加密时要用SMTP_SSL
         try:
            s = smtplib.SMTP_SSL(self.sIp, int(self.sPort))
            s.set_debuglevel(1)
            s.login(self.sUser, self.sPassword)
            s.sendmail(msg["From"], msg["To"].split(';'), msg.as_string())
            print "success"
        except:
            print "failed"
            '''


if __name__ == "__main__":

    a=CommEmail()
    a.sendHtmlEmail()
