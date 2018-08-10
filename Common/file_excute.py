#coding=utf-8
'''import sys,os
print __file__
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)'''
import os
ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

def getbrowser():
    f = open(ROOT('browser.txt'), 'r')
    if f:
        list=f.readlines()
        '''for line in range(0,len(list)):
            list[line]=list[line].strip()'''
        return list
    else:
        print "内容为空"
    f.close()
