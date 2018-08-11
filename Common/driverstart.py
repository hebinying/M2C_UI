#coding=utf-8
from selenium import webdriver
from Common import file_excute
def openfile():
    list=file_excute.getbrowser()
    for name in range(0,len(list)):
        list[name]=list[name].strip()
        if driverstart(list[name]):
            driver=driverstart(list[name])
            return driver
def driverstart(devices):
    if devices=='firefox'or devices=='Firefox':
        driver=webdriver.Firefox()


    elif devices=='chrome'or devices=='Chrome':
        driver=webdriver.Chrome()

    elif devices=='ie'or devices=='IE'or    devices=='IE':
        driver=webdriver.Ie()
    else:
        print "Not found suitable browser"
        return
    return driver
