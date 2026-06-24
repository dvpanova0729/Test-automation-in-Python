from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.FireFox()

driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()

text_box = driver.find_element(
    By.CSS_SELECTOR, 'input')

text_box.send_keys('12345')
text_box.clear()
text_box.send_keys('54321')

driver.quit()
