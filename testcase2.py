from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
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
    password.send_keys("1234")

loginButton = driver.find_element(By.XPATH,value="//button[@data-qa='login-button']")
loginButton.click()

username = driver.find_element(By.XPATH,value="//div[@class='shop-menu pull-right']/child::*/child::*[10]")
if username.is_displayed:
    print("User name is Displayed")

delete = driver.find_element(By.XPATH,value="//div[@class='shop-menu pull-right']/child::*/child::*[5]")
delete.click()
time.sleep(2)
deleteAcc= driver.find_element(By.XPATH,value="//div[@class='col-sm-9 col-sm-offset-1']/child::*[1]/child::*")
deleteAcc.is_displayed()
print(deleteAcc.text)
time.sleep(5)
driver.close()