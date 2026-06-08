from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
URL = 'http://automationexercise.com'
driver.get(URL)
wait = WebDriverWait(driver, 10)

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

def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads')   ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')       ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")
dismiss_ads(driver)
delete = driver.find_element(By.XPATH,value="//div[@class='shop-menu pull-right']/child::*/child::*[5]")
delete.click()

deleteAcc = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-sm-9 col-sm-offset-1']/child::*[1]/child::*")))

print(deleteAcc.text)

driver.close()