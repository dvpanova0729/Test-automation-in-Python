# методы для добавления товаров в корзину и перехода в корзину
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_products(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_list'))
        )
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'
            ).click()

    def open_cart(self):
        self.driver.get('https://www.saucedemo.com/cart.html')
