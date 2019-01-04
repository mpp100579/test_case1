# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox() #webdriver打开浏览器
#driver.get('https://huilansame.github.io')
driver.get("http://www.baidu.com")#get方法浏览器打开网页
driver.maximize_window()           #浏览器打开之后设置全屏
sleep(3)  # 强制等待3秒再执行下一步
print (driver.current_url)     #判断打印当前网页
print (driver.title)          #判断打印标题
ele1 = driver.find_element_by_class_name("s_ipt") #浏览器定位元素
print (ele1.id)                           #打印id元素
ele1.send_keys("123").click()  #操作元素，输入方法输入

driver.get("http://www.maiziedu.com/")#get方法浏览器打开网页
driver.maximize_window()          #网页打开后设置全屏
ele2 = driver.find_element_by_link_text("机器学习")
ele2.click()

driver.get("http://www.baidu.com")#get方法浏览器打开网页
ele3 =driver.find_element_by_name("wd")
ele3.send_keys("dsgsf")
print (ele3.id)

driver.back()                          #浏览器返回

