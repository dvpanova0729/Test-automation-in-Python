import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    """
    Класс для работы со страницей оформления заказа в интернет‑магазине.

    Предназначен для заполнения формы с личными данными
    и продолжения процесса оформления заказа.

    :param driver: WebDriver — экземпляр драйвера Selenium.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы оформления заказа.

        :param driver: WebDriver — драйвер для управления браузером.
        """

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("""
    Заполнение формы заказа:
    имя '{first_name}',
    фамилия '{last_name}',
    почтовый индекс '{postal_code}'""")
    def fill_form(self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """
        Заполняет форму на странице оформления заказа личными данными.

        :param first_name: str — имя для заполнения формы.
        :param last_name: str — фамилия для заполнения формы.
        :param postal_code: str — почтовый индекс для заполнения формы.
        :return: None — метод не возвращает значение.
        """

        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#continue'))
        ).click()
