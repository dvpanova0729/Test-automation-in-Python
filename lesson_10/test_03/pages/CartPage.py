import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для работы со страницей корзины интернет‑магазина (Sauce Demo).

    Предназначен для выполнения действий, связанных с оформлением заказа:
    нажатие кнопки Checkout и проверка итоговой стоимости в корзине.

    :param driver: WebDriver — экземпляр драйвера Selenium,
    через который осуществляется взаимодействие с браузером.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы корзины.

        :param driver: WebDriver — драйвер для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажатие кнопки оформления заказа (Checkout)")
    def checkout_click(self) -> None:
        """
        Нажимает кнопку оформления заказа (Checkout) на странице корзины.

        Последовательность действий:
        1. Ожидает доступности кнопки Checkout.
        2. Нажимает на кнопку (CSS-селектор: #checkout).

        :return: None — метод не возвращает значение.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))
        ).click()

    @allure.step("Проверка ожидаемой стоимости {expected_price}")
    def check_price(self, expected_price: str) -> None:
        """
        Проверяет итоговую цену в корзине на соответствие ожидаемому значению.

        :param expected_price: str — ожидаемая итоговая цена ($58.29).
        :return: None
        """
        total_price_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test="total-label"]'))
            )

        total_price_txt = total_price_element.text
        cleaned_text = ''.join(total_price_txt.split())  # Убираем все пробелы
        price_str = cleaned_text[cleaned_text.index('$') + 1:]
        price_value = price_str.strip()

        print(f"Получена итоговая стоимость: ${price_value}")
        assert price_value == expected_price
