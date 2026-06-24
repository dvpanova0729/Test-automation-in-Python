from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')

input_text = driver.find_element(
    By.CSS_SELECTOR, '#newButtonName').send_keys('SkyPro')
tab_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
new_button_name = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(new_button_name)
