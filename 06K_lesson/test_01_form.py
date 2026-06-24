from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
driver.maximize_window()


def test_complete_form(driver):
    first_name = driver.find_element(
        By.CSS_SELECTOR, 'input[name="first-name"]'
        )
    first_name.send_keys('Иван')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.send_keys('Петров')

    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys('Ленина, 55-3')

    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys('Москва')

    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys('Россия')

    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.send_keys('test@skypro.com')

    phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone_number.send_keys('+7985899998787')

    job_position = driver.find_element(
        By.CSS_SELECTOR, 'input[name="job-position"]'
        )
    job_position.send_keys('QA')

    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.send_keys('SkyPro')

    submit_but = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_but.click()


def test_zip_code(driver):
    waiter = WebDriverWait(driver, 10)

    zip_alert = waiter.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.alert.py-2.alert-danger')
            ))

    assert 'alert-danger' in zip_alert.get_attribute('class')

    success_alerts = waiter.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.alert.py-2.alert-success")
            ))
    for alert in success_alerts:
        assert 'alert-success' in alert.get_attribute('class')


test_complete_form(driver)
test_zip_code(driver)

driver.quit()
