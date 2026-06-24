import pytest
from selenium import webdriver
from pages.CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.add_delay(45)
    click_buttons = ['7', '+', '8', '=']
    result = calc_page.click_button(click_buttons)
    calc_page.check_result(result, 15)
