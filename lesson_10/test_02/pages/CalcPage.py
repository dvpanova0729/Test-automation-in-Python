import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """
    Класс для работы с веб-страницей калькулятора.

    :param driver: WebDriver — экземпляр драйвера Selenium.
    """

    def __init__(self, driver) -> None:
        """
        Инициализирует объект страницы калькулятора.

        :param driver: WebDriver — драйвер для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        :return: None — метод не возвращает значение.
        """
        self.driver.get(
          'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
            )

    @allure.step("Установка задержки {delay_value} секунд")
    def add_delay(self, delay_value: int) -> None:
        """
        Устанавливает задержку перед выполнением операций.

        :param delay: int — время задержки в секундах.
        :return: None — метод не возвращает значение.
        """
        calc_delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        calc_delay.clear()
        calc_delay.send_keys(delay_value)

    @allure.step("Нажатие последовательности кнопок: {buttons_list}")
    def click_button(self, buttons_list: list[str]) -> str:
        """
        Нажимает последовательность кнопок на калькуляторе.

        :param buttons_list: list[str] — список строк,
        представляющих кнопки для нажатия (например, ['7', '+', '8', '=']).
        :return: str — результат вычислений после нажатия всех кнопок.
        """
        for button_value in buttons_list:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{button_value}']"
                ).click()

        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, 'span#spinner')
                )
            )
        result_text = self.driver.find_element(
            By.CSS_SELECTOR, 'div.screen').text
        return int(result_text)

    @allure.step("Проверка результата: {expected} = {result}")
    def check_result(self, result: str, expected: int) -> None:
        """
        Проверяет, что полученный результат соответствует ожидаемому.

        :param result: str — результат, полученный после выполнения
        операций на калькуляторе.
        :param expected: int — ожидаемое числовое значение результата.
        """

        assert int(result) == expected
