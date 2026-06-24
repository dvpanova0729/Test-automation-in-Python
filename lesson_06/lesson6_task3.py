from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 10, 0.1)
waiter.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'p#text.lead'), 'Done!'))
images = driver.find_elements(By.TAG_NAME, "img")
src_image = images[3].get_attribute('src')
print(src_image)
