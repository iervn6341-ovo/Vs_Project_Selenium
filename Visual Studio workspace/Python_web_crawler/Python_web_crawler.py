from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys as key
import time,re

driver= webdriver.Chrome()
driver.get('https://wateroff.water.gov.tw/city/%E8%87%BA%E4%B8%AD%E5%B8%82/index.html')
location_position = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-input")))
location_position.send_keys('東區')
time.sleep(5)
location_position.send_keys(key.ENTER)

case_num = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[4]/a/div[2]/div[2]/div[2]/div')
for num in case_num:
	print("Result: ",num.text)
input()