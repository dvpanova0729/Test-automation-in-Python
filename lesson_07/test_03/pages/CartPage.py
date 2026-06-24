# методы для нажатия кнопки Checkout и проверки содержимого корзины
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout_click(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))
            ).click()

    def check_price(self, expected_price):
        total_price_txt = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'summary_total_label')
            )
        ).text
        price_str = total_price_txt.split('$')[1]
        price_value = price_str.strip()

        print(f"Получена итоговая стоимость: ${price_value}")
        assert price_value == expected_price
