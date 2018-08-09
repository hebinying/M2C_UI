from selenium import webdriver

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

    '''设置窗口为最大'''
    driver.maximize_window()
    return  driver
