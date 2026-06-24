import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Класс для работы с главной страницей интернет‑магазина (Sauce Demo).

    Предназначен для выполнения действий,
    связанных с добавлением товаров в корзину
    и переходом в корзину.

    :param driver: WebDriver — экземпляр драйвера Selenium.
    """

    def __init__(self, driver):
        """
        Инициализирует объект главной страницы.

        :param driver: WebDriver — драйвер для управления браузером.
        """

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товаров в корзину")
    def add_products(self) -> None:
        """
        Добавляет в корзину три товара: рюкзак, футболку и комбинезон.

        Последовательность действий:
        1. Ожидает видимости списка товаров.
        2. Нажимает кнопку «Добавить в корзину» для рюкзака.
        3. Нажимает кнопку «Добавить в корзину» для футболки.
        4. Нажимает кнопку «Добавить в корзину» для комбинезона.

        :return: None — метод не возвращает значение.
        """
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

    @allure.step("Переход в корзину")
    def open_cart(self) -> None:
        """
        Переходит на страницу корзины интернет‑магазина.

        Выполняет переход по URL `https://www.saucedemo.com/cart.html`.

        :return: None — метод не возвращает значение.
        """
        self.driver.get('https://www.saucedemo.com/cart.html')
