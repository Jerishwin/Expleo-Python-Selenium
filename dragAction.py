from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains as AC

driver = webdriver.Chrome()
driver.maximize_window()
URL = 'https://letcode.in/draggable'
driver.get(URL)
wait = WebDriverWait(driver, 10)

action = AC(driver)

drag = wait.until(EC.presence_of_element_located((By.ID, "sample-box")))

action.click_and_hold(drag).move_by_offset(-30, -30).move_by_offset(-10, -30).release().perform()
time.sleep(5)

