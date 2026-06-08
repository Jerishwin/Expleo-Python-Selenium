import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.execute_script("alert('Welcome')")
time.sleep(4)

prompt = driver.switch_to.alert
print("Prompt text:", prompt.text)  # Enter your name
prompt.send_keys("Jerishwin")       # type into the prompt box
time.sleep(2)
prompt.accept()                     # click OK
time.sleep(2)

confirm = driver.switch_to.alert
print("Confirm text:", confirm.text)  # Do you want to proceed
confirm.dismiss()                     # click Cancel
time.sleep(2)

driver.quit()