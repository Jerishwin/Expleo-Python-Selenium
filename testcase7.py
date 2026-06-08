from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

URL = 'http://automationexercise.com'
driver.get(URL)

wait = WebDriverWait(driver, 10)

test = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='shop-menu pull-right']/child::*/child::*[5]")))
test.click()

testTitle = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@id='form']/child::*/child::*/child::*/child::h2")))

print(testTitle.text)