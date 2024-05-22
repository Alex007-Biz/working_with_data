import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://plitkanadom.ru/svet/lyustry"
driver.get(url)
time.sleep(3)

liustry = driver.find_elements(By.CLASS_NAME, 'bx_catalog_item_container')

for liustra in liustry:
    link = liustra.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    print(link)
