#coding=utf-8
import pymysql
import sys



class GetVerifyCode:

    def __init__(self):
        self.host='mysql.m2c2017test.com'
        self.user='testuser'
        self.password='FLOjMJ!SY123'
        self.LibraryName=''
        self.charset = 'utf-8'
    '''def set_sql(self,host,user,password,LName):
        self.host=host
        self.user=user
        self.password=password
        self.LibraryName=LName
        self.charset = 'utf-8'''

    def connect_sql(self,liName):
        self.LibraryName=liName
        try:
            conn=pymysql.connect(self.host,self.user,self.password,self.LibraryName,charset='utf8')
            cur=conn.cursor()
            return cur
        except:
            print "未找到%s库" %self.LibraryName
            conn.close()

    def excute_sql(self,cur,sql):
       try:
           cur.execute(sql)
           result = cur.fetchone()
           return result
       except:
           print "执行失败"


    def close_sql(self,cur):
        cur.close()

    def close_connect(self,conn):
        conn.close()

