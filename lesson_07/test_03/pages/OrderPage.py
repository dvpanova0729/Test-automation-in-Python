# методы для заполнения формы данными и проверки итоговой стоимости.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.CSS_SELECTOR, '#first-name'
            ).send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '#last-name'
            ).send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '#postal-code'
            ).send_keys(postal_code)
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#continue'))
        ).click()
