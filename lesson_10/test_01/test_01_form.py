import allure
import pytest
from selenium import webdriver
from pages.FormPage import FormPage


@allure.suite("Тестирование формы для заполнения")
class TestForm:

    @pytest.fixture
    def driver(self):
        """
        Фикстура для инициализации и завершения работы драйвера.
        Инициализирует Chrome-драйвер, устанавливает неявное ожидание 3 сек,
        разворачивает окно на весь экран.
        После выполнения теста закрывает драйвер.
        """
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Проверка заполнения формы")
    @allure.description("""Тест проверяет последовательное выполнение
    всех этапов работы с формой: открытие страницы, заполнение полей,
    отправка формы и проверка корректности результатов.""")
    @allure.feature("Форма данных")
    @allure.severity(allure.severity_level.NORMAL)
    def test_form_submission_flow(self, driver):
        """
        Тест проверяет работу с формой —
        от открытия страницы до проверки результатов отправки.

        :param driver: WebDriver — объект драйвера, переданный фикстурой.
        """

        form_page = FormPage(driver)
        form_page.open()
        form_page.fill_form()
        form_page.submit_form()
        form_page.check_form_submission()
