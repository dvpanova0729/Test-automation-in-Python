import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogInPage:
    """
    Класс для работы со страницей авторизации в интернет‑магазине (Sauce Demo).

    Предназначен для выполнения действий, связанных
    с авторизацией пользователя:
    открытие страницы, ввод логина и пароля, нажатие кнопки входа.

    :param driver: WebDriver — экземпляр драйвера Selenium.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы авторизации.

        :param driver: WebDriver — драйвер для управления браузером.
        """

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации Sauce Demo.

        Выполняет переход по URL `https://www.saucedemo.com/`.

        :return: None — метод не возвращает значение.
        """
        self.driver.get('https://www.saucedemo.com/')

    @allure.step("""
    Авторизация пользователя:
    ввод логина '{username}' и пароля '{password}',
    нажатие кнопки входа""")
    def auth(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя на сайте: вводит логин и пароль,
        затем нажимает кнопку входа.

        Последовательность действий:
        1. Ожидает доступности поля для ввода логина и вводит значение.
        2. Находит поле для ввода пароля и вводит значение.
        3. Находит и нажимает кнопку входа (`#login-button`).

        :param username: str — логин пользователя для авторизации.
        :param password: str — пароль пользователя для авторизации.
        :return: None — метод не возвращает значение.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#user-name'))
        ).send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, '#password'
            ).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
