from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://seleniumbase.io/demo_page")

wait = WebDriverWait(driver, 10)

dropbox = Select(driver.find_element(By.ID, "mySelect"))

dropbox.select_by_index(2)
time.sleep(3)
dropbox.select_by_value("100%")
time.sleep(3)
dropbox.select_by_visible_text("Set to 25%")
time.sleep(3)

list1 = dropbox.options
print(list1)
