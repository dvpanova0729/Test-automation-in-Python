import pytest
import allure
from selenium import webdriver
from pages.CalcPage import CalcPage


@allure.suite("Тестирование калькулятора")
class TestCalc:
    """
    Класс с тестами для проверки работы калькулятора.
    """

    @pytest.fixture
    def driver(self):
        """
        Фикстура для инициализации и завершения работы драйвера.

        :yield: WebDriver — объект драйвера для тестов.
        """
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Проверка сложения чисел 7 и 8 на калькуляторе")
    @allure.description("""Тест проверяет, что калькулятор корректно
    выполняет операцию сложения 7 + 8 и возвращает результат 15.""")
    @allure.feature("Калькулятор")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calc(self, driver):
        """
        Тест проверяет корректность работы калькулятора
        на примере сложения 7 + 8.

        :param driver: WebDriver — драйвер, переданный фикстурой.
        """

        calc_page = CalcPage(driver)
        calc_page.open()
        calc_page.add_delay(45)
        click_buttons = ['7', '+', '8', '=']
        result = calc_page.click_button(click_buttons)
        calc_page.check_result(result, 15)
