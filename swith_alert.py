#-*-coding:utf-8-*-
#@Time      :2018/11/14  15:10
#@Author    ;河鱼不眠
#@Filename  :swith_alert.py
#@Software  ;PyCharm
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get(r'C:\Users\河鱼不眠\Desktop\login.html')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_id('user_name').send_keys('123456')
driver.find_element_by_id('user_pas').send_keys('112233')
driver.find_element_by_id('user_btn').click()

WebDriverWait(driver,2).until(EC.alert_is_present())
alert=driver.switch_to.alert

res=alert.text
print(res)
alert.accept()
driver.quit()




