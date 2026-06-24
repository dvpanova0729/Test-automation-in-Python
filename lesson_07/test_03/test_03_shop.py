import pytest
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


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
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
