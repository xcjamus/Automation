from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://hc1pc.bigangwan.com')
driver.find_element(By.LINK_TEXT,'登录').click()
driver.find_element(By.ID,'nick').send_keys('13362185609')
driver.find_element(By.ID,'password').send_keys('123321')
driver.find_element(By.ID,'login_submit').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,'body > div.header > div.nav_bottom > div > div.header_main_nav > ul > li:nth-child(2) > a').click()
sleep(2)
js = 'window.scrollTo(0,200)'
driver.execute_script(js)
driver.find_element(By.CSS_SELECTOR,'body > div.main > div.main_down > ul:nth-child(1) > li:nth-child(1) > div > div > div.md_btn > a').click()
sleep(1)
driver.find_element(By.ID,'money').send_keys('1000')
driver.find_element(By.ID,'gotobuy_btn').click()
# print(driver.find_element(By.CSS_SELECTOR,'#toast > span').text)
sleep(2)
js = 'window.scrollTo(0,350)'
driver.execute_script(js)
driver.find_element(By.CSS_SELECTOR,'body > div.main > div > div > div.Use_redbtn > a').click()
sleep(2)
driver.find_element(By.ID,'mobileCode').send_keys('1111')
sleep(2)
driver.find_element(By.CSS_SELECTOR,'#alert_listthree_three > div > div.alert_listthree_btnd > a').click()
sleep(3)
print(driver.find_element(By.CSS_SELECTOR,'#toast > span').text)
# driver.quit()