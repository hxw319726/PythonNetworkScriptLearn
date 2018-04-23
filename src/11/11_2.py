# 利用phantomjs模仿用户在浏览器上的操作
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.implicitly_wait(10)
driver.find_element_by_id('form_email').clear()
driver.find_element_by_id('form_email').send_keys('账号')
driver.find_element_by_id('form_password').clear()
driver.find_element_by_id('form_password').send_keys('密码')
driver.find_element_by_class_name('bn-submit').click()
print(driver.page_source)