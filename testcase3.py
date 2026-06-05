from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
URL = 'http://automationexercise.com'
driver.get(URL)

signup = driver.find_element(By.XPATH,value="//div[@class='shop-menu pull-right']/child::*/child::*[4]")
if signup.is_displayed():
    signup.click()


mail = driver.find_element(By.XPATH,value="//form[@action='/login']/input[@name='email']")
password = driver.find_element(By.XPATH,value="//form[@action='/login']/input[3]")

if mail.is_displayed():
    mail.send_keys("jjk24@gmail.com")
    password.send_keys("123")

loginButton = driver.find_element(By.XPATH,value="//button[@data-qa='login-button']")
loginButton.click()

fail = driver.find_element(By.XPATH,value="//form[@action='/login']/child::*[4]")
fail.is_displayed()
print(fail.text)

driver.close()
