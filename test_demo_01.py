# -- coding: utf-8 --
# @Time : 2022/6/10 13:35
# @Author : siyu.yang
# @Software: PyCharm
# import selenium
# from appium import webdriver
# des = {
#     'platformName':'Android',
#     'platformVersion':'11.1',
#     'deviceName':'OPPO K5',
#     'appPackage':'com.windfindtech.junemeet',
#     'appActivity':'com.junyao.MainActivity',
#     'udid':'b1e7d9b4',
#     'noReset':'True',
#     'unicodeKeyboard':'True',
#     'resetKeyboart':'True'
# }
# driver = webdriver.Remote('http://127.0.0.1/wd/hub',des)


importseleniumfromappiumimportwebdriverdes={'platformName':'Android','platformVersion':'9.0',#填写android虚拟机的系统版本'deviceName':'SamsungGalaxyS9',#填写安卓虚拟机的设备名称'appPackage':'com.ibox.calculators',#填写被测试包名'appActivity':'.CalculatorActivity',#填写被测试app入口'udid':'192.168.56.101:5555',#填写通过命令行adbdevices查看到的uuid'noReset':True,'unicodeKeyboard':True,'resetKeyboard':True,}driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
