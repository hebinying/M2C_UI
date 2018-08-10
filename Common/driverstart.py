#coding=utf-8
from selenium import webdriver
from Common import file_excute

class getdriver:
    def __init__(self):
        list=file_excute.getbrowser()
        for name in range(0,len(list)):
            if self.driverstart(list[name]):
                self.driverstart(list[name])
    def driverstart(self,devices):
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
