#coding=utf-8
from Common import driverstart as DR
from Common import baseOperator as BO
from Searchsql import GetVerifyCode as gt

'''检查：登录，退出，修改登录密码'''


dr = DR.openfile()
driver = BO.DriverBase(dr)
driver.get_url("http://b.m2c2017test.com")
def bLogin(username,password):
    driver.ECsend("input",username,0)
    driver.ECsend("input",password,1)
    driver.ECclick("button")

    print "商家登录"


def bQuit():
    driver.ECclick("right_title_quit")
    print "退出登录"

def bChange(mobile,npwd):
    driver.ECclick("span.el-dropdown-link.ellipsis.el-dropdown-selfdefine")
    driver.ECclick("div[path='/s/updatePass']")
    driver.EIclick("sendVer")
    g = gt.GetVerifyCode()
    sql="select verify_code from t_support_verify_code WHERE created_date=(select MAX(created_date) FROM  t_support_verify_code WHERE mobile=%s)" %mobile
    cur=g.connect_sql("m2c_support")
    code=g.excute_sql(cur,sql)
    if code:
        driver.EIsend("verifyCode",code)

    '''设置新的密码'''
    driver.EIsend("newPass",npwd)
    driver.EIsend("confirmNewPass",npwd)
    driver.ECclick("button.el-button.el-button--primary")



