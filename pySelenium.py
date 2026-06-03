from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
URL = "https://www.google.co.in"
driver.get(URL)
print(driver.title)
search = driver.find_element(By.ID,value="APjFqb")
if search.is_enabled():
    search.send_keys("Selenium")
time.sleep(2)
key = driver.find_element(By.XPATH,value="//button[@class='plR5qb Y5MKCd Sw4CSc']")
if key.is_enabled():
    key.click()
time.sleep(3)
driver.close()

