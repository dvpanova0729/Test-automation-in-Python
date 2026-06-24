import pytest
import allure
from selenium import webdriver
from pages.LogInPage import LogInPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage


data_for_test = {
    'username': 'standard_user',
    'password': 'secret_sauce',
    'first_name': 'Дарья',
    'last_name': 'Панова',
    'postal_code': '249039',
    'expected_price': '58.29'
}


@allure.suite("Тестирование сценария работы интернет-магазина:")
class TestShop:
    """
    Класс с тестами для проверки сквозного сценария работы интернет-магазина:
    авторизация → добавление товаров → оформление заказа.
    """

    @pytest.fixture
    def driver(self):
        """
        Фикстура для инициализации и завершения работы драйвера Firefox.

        Создаёт экземпляр драйвера Firefox,
        устанавливает неявное ожидание 3 сек,
        разворачивает окно на весь экран.
        После выполнения теста закрывает браузер.

        :yield: WebDriver — объект драйвера Firefox
        для взаимодействия с браузером.
        """
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Тестирование сценария работы интернет-магазина")
    @allure.description("""
    Тест проверяет последовательное выполнение всех этапов работы с формой:
    - открытие страницы авторизации;
    - ввод логина и пароля;
    - добавление товаров на главной странице;
    - переход в корзину;
    - оформление заказа через форму с личными данными;
    - проверка итоговой цены в корзине.""")
    @allure.feature("Интернет-магазин")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop(self, driver):
        """
        Тест проверяет сквозной сценарий работы интернет-магазина:
        авторизация,
        добавление товаров в корзину,
        оформление заказа и проверка итоговой цены.

        :param driver: WebDriver — драйвер браузера, переданный фикстурой.
        """

        login_page = LogInPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        order_page = OrderPage(driver)
        login_page.open()
        login_page.auth(data_for_test['username'], data_for_test['password'])
        main_page.add_products()
        main_page.open_cart()
        cart_page.checkout_click()

        order_page.fill_form(
            data_for_test['first_name'],
            data_for_test['last_name'],
            data_for_test['postal_code']
        )
        cart_page.check_price(data_for_test['expected_price'])
