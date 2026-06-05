from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://letcode.in/frame")

wait = WebDriverWait(driver, 10)

frame1 = wait.until(EC.presence_of_element_located((By.ID, "firstFr")))
driver.switch_to.frame(frame1)

driver.find_element(By.NAME, "fname").send_keys("jack")
driver.find_element(By.NAME, "lname").send_keys("rose")

nested_iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(nested_iframe)

driver.find_element(By.NAME, "email").send_keys("jr@gmail.com")

driver.switch_to.default_content()

time.sleep(10)
driver.quit()