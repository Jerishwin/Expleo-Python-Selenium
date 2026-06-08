import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

def flash_element (element):
    for i in range(1, 30):
        driver.execute_script("arguments[0].style.background='red'",element)
        time.sleep(.2)
        default_color = element.value_of_css_property('color')
        driver.execute_script("arguments[0].style.background='"+default_color+"'",element)

login_button = driver.find_element(By.XPATH, value="//input[@type='submit']")
flash_element(login_button)
time.sleep(4)