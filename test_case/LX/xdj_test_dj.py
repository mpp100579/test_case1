#coding=utf-8
from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get("http://cn.bing.com/")
keywords = 'MrLevo520 CSDN'
send_keywords=keywords.decode('utf-8')#中英混输入可防止乱码
browser.find_element_by_id("sb_form_q").send_keys(send_keywords)

time.sleep(1)
#----------操作一：进行对关键字MrLevo520 CSDN搜索----------------
browser.find_element_by_id("sb_form_go").click()#执行此操作会进行搜索，但是没有弹出新窗口，所以句柄不用重定位
time.sleep(3)
#----------操作二：对搜索页面"我的CSDN"进行点击操作--------------
browser.find_element_by_xpath("/html/body/div/ol/li/h2/a").click()#进行当前页面点击第一项

#--------操作三：对新弹出的页面再点击"贡献的资源"选项-----
browser.switch_to_window(browser.window_handles[1])
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/a[3]").click()

time.sleep(5)