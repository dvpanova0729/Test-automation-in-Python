from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.FireFox()

driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()

username_box = driver.find_element(
    By.CSS_SELECTOR, 'input#username')
username_box.send_keys('tomsmith')

password_box = driver.find_element(
    By.CSS_SELECTOR, 'input#password')
password_box.send_keys('SuperSecretPassword!')

login_but = driver.find_element(
    By.CSS_SELECTOR, 'button.radius')
login_but.click()

allert = driver.find_element(By.CSS_SELECTOR, 'div#flash').text
print(allert)

driver.quit()
