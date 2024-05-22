import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://plitkanadom.ru/svet/lyustry"
driver.get(url)
time.sleep(3)

liustry = driver.find_elements(By.CLASS_NAME, 'bx_catalog_item_container')
# print(liustry)
parsed_data = []

for liustra in liustry:
    try:
        title = liustra.find_element(By.CSS_SELECTOR, 'div.bx_catalog_item_title').text
        price = liustra.find_element(By.CSS_SELECTOR, 'div.bx_price').text
        link = liustra.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue
    # parsed_data.append([title, company,salary, link])
    parsed_data.append([title, price, link])

driver.quit()
with open("liustry.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'Цена', 'ссылка'])
    writer.writerows(parsed_data)