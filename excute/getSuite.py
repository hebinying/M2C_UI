#coding=utf-8
from unittest import TestLoader


#通过文件路径及py的文件名过滤，并返回TestSuite
def getTestSuite(filename,keys):
    suit=TestLoader().discover(filename,keys)
    return suit









