from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )
driver.maximize_window()


def input_value(driver):
    calc_delay = driver.find_element(By.CSS_SELECTOR, '#delay')
    calc_delay.clear()
    calc_delay.send_keys('45')

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()


def test_result(driver):
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert result == "15"


input_value(driver)

waiter = WebDriverWait(driver, 46, 0.1)
waiter.until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, 'span#spinner'))
    )

test_result(driver)

driver.quit()
