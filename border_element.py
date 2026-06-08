import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

def element_border(element):
    driver.execute_script("arguments[0].style.border='4px solid red'",element)
    
login_button = driver.find_element(By.XPATH, value="//input[@type='submit']")
element_border(login_button)
time.sleep(5)