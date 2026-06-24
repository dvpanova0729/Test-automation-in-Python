from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
driver.maximize_window()

button = driver.find_element(
    By.CSS_SELECTOR, 'button.btn-primary')
button.click()

alert = driver.switch_to.alert
alert.accept()

driver.quit()
