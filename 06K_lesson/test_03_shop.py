from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()


def auth(driver):
    wait = WebDriverWait(driver, 10)

    login = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#user-name'))
        )
    login.send_keys('standard_user')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR, '#login-button').click()


def add_products(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list')))

    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'
    ).click()

    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    wait.until(EC.url_contains('cart.html'))
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))
        )
    checkout_button.click()


def checkout(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains('checkout-step-one.html'))

    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.send_keys('Дарья')

    last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name.send_keys('Панова')

    postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    postal_code.send_keys('249039')

    continue_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#continue'))
        )
    continue_button.click()


def check_price(driver):
    wait = WebDriverWait(driver, 10)

    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))
    )

    total_text = total_element.text
    price_str = total_text.split('$')[1]
    price_value = price_str.strip()

    print(f"Получена итоговая стоимость: ${price_value}")
    assert price_value == "58.29"


auth(driver)
add_products(driver)
checkout(driver)
check_price(driver)

driver.quit()
