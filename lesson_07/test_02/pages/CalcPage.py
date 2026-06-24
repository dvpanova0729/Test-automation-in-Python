from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    # Открыть страницу калькулятора
    def open(self):
        self.driver.get(
          'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
            )

    # Ввести значение 45 в поле delay
    def add_delay(self, delay_value):
        calc_delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        calc_delay.clear()
        calc_delay.send_keys(delay_value)

    # Нажать кнопки 7 + 8 =
    def click_button(self, buttons_list):
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

    # Проверить результат через 45 секунд
    def check_result(self, actual_result, expected_result):
        assert actual_result == expected_result
