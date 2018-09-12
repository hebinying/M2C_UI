#coding:utf-8
from Common import baseOperator as BO
import logging

def bloggin(driver,name,password):
    try:
        driver.ECsends("input", name, 0)
        driver.ECsends("input", password, 1)
        driver.ECclick("button")
        assert("成功"in driver.findElementByClassName("div.el-message").findElementByTagName('p').text)
        logging.log(logging.INFO, "登录成功")
    except Exception:
        #logging.log(logging.ERROR,"登录失败")
        logging.info("登录失败，密码或用户名错误")
