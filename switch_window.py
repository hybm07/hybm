#-*-coding:utf-8-*-
#@Time      :2018/11/13  9:53
#@Author    ;河鱼不眠
#@Filename  :switch_window.py
#@Software  ;PyCharm
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get('http://www.ketangpai.com')
driver.maximize_window()

# res=driver.current_window_handle
# print(res)

driver.find_element_by_xpath('//a[@class="login"]').click()
driver.find_element_by_xpath('//input[@name="account"]').send_keys('15837373314')
driver.find_element_by_xpath('//input[@name="pass"]').send_keys('xq361246')
driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]').click()

# WebDriverWait(driver,10)
# time.sleep(10)#显性等待，死等
# driver.implicitly_wait(10)#隐性等待，只要有find_element_by_xx方法在就会自动去调取这个动作
locator=(By.XPATH,'//span//a[contains(text(),"===元素定位小练习====")]')
WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value(locator))  #这个等待时间的方法在这里使用不成功
driver.find_element_by_xpath('//span//a[contains(text(),"===元素定位小练习====")]').click()


driver.quit()





