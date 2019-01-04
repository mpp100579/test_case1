#coding=utf-8

from selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys  #需要引入keys包

driver = webdriver.Firefox()
driver.get("http://192.168.1.56:81/")
driver.find_element_by_id("uid").click()
driver.find_element_by_id("uid").clear()
driver.find_element_by_id("uid").send_keys("yujian")
driver.find_element_by_id("paw").clear()
driver.find_element_by_id("paw").send_keys("bkc123456")
#driver.find_element_by_id("btnsubmit").click()
driver.find_element_by_id('paw').send_keys(Keys.ENTER)#定位到需要enter键的地方
driver.maximize_window()

#driver.find_element_by_xpath('//*[@class=\'fa icon-cc-home\']').click()
driver.find_element_by_css_selector('html.k-ff.k-ff59 body div.b-content div.b-side nav.menu-wrap div.menu-header span.menu-toggle cite').click()
#ele = driver.find_element_by_xpath('//div[@cite=\'系统导航\']')
#ele.click()
ele1 = driver.find_element_by_link_text('点检系统管理')
ActionChains(driver).move_to_element(ele1).perform()
driver.find_element_by_link_text('工作岗位设置').click()
print(ele1.tag_name)
print(ele1.get_attribute('name'))




