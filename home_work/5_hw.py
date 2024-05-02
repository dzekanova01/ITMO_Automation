from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

icon_1 = driver.find_element(By.CSS_SELECTOR, '#user-name')
icon_2 = driver.find_element(By.CSS_SELECTOR, '#password')
icon_3 = driver.find_element(By.CSS_SELECTOR, '#login-button')

if icon_1 and icon_2 and icon_3 is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')
