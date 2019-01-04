import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
#chromedriver = "C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver


browser = webdriver.Chrome()
browser.get("http://www.python.org")
wait = WebDriverWait(browser, 10)
assert "Python" in browser.title
elem = browser.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in browser.title
browser.close()
