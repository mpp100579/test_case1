# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://192.168.1.56:81/")
        driver.find_element_by_id("uid").click()
        driver.find_element_by_id("uid").clear()
        driver.find_element_by_id("uid").send_keys("yujian")
        driver.find_element_by_id("paw").clear()
        driver.find_element_by_id("paw").send_keys("yujian612")
        driver.find_element_by_id("btnsubmit").click()
        driver.find_element_by_id("uid").click()
        driver.find_element_by_id("uid").clear()
        driver.find_element_by_id("uid").send_keys("xzx")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("paw").click()
        driver.find_element_by_id("paw").clear()
        driver.find_element_by_id("paw").send_keys("bkc123456")
        driver.find_element_by_id("btnsubmit").click()
        driver.find_element_by_link_text(u"运行巡检标准").click()
        driver.find_element_by_id("CSGW01").click()
        driver.find_element_by_id("CSBM1$CSGW01$XJQY01").click()
        driver.find_element_by_id("btnInsertInsp").click()
        driver.find_element_by_id("btnInsertInsp").click()
        driver.find_element_by_id("btnInsertInsp").click()
        driver.find_element_by_xpath("//form[@id='FormInsp']/div[2]/div/div/div").click()
        driver.find_element_by_id("SBMC").clear()
        driver.find_element_by_id("SBMC").send_keys(u"设备1")
        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_id("XMSX").click()
        driver.find_element_by_id("XMSX").clear()
        driver.find_element_by_id("XMSX").send_keys("1")
        driver.find_element_by_xpath("//div[@id='BJDM_chosen']/a/span").click()
        driver.find_element_by_xpath("//div[@id='BJDM_chosen']/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='BJDM_chosen']/a/span").click()
        driver.find_element_by_xpath("//form[@id='FormInsp']/div[2]/div/div/div").click()
        driver.find_element_by_id("SBMC").clear()
        driver.find_element_by_id("SBMC").send_keys(u"设备")
        driver.find_element_by_id("linkBtnBack").click()
        driver.find_element_by_id("uid").click()
        driver.find_element_by_id("paw").clear()
        driver.find_element_by_id("paw").send_keys("yujian612")
        driver.find_element_by_id("btnsubmit").click()
        driver.find_element_by_id("paw").click()
        driver.find_element_by_id("paw").clear()
        driver.find_element_by_id("paw").send_keys("bkc123456")
        driver.find_element_by_id("btnsubmit").click()
        driver.find_element_by_xpath("//li[@id='WorkRemind']/a/i").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

