import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        """
        Конструктор класса FormPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открытие страницы с формой")
    def open(self) -> None:
        """
        Открывает страницу с формой для тестирования.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    @allure.step("Заполнение формы тестовыми данными")
    def fill_form(self) -> None:
        """
        Заполняет все поля формы значениями из словаря fields.
        Для каждого поля ожидает появления элемента по имени (By.NAME)
        и вводит соответствующее значение.
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))
            ).send_keys(value)

    @allure.step("Отправка формы")
    def submit_form(self) -> None:
        """
        Нажимает кнопку отправки формы (элемент с type="submit").
        Ожидает, пока элемент станет кликабельным (By.CSS_SELECTOR).
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]')
            )
        ).click()

    @allure.step("Получение класса поля с ID '{field_id}'")
    def get_field_class(self, field_id: str) -> str:
        """
        Ожидает появления элемента с заданным ID (By.ID) и возвращает
        значение его атрибута class.

        :param field_id: str — ID элемента на странице (например, 'zip-code').
        :return: str — значение атрибута class элемента.
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id)
            )
        ).get_attribute("class")
        return element

    @allure.step("Проверка наличия ошибки в поле ZIP-кода")
    def check_zip_code_error(self) -> bool:
        """
        Проверяет, присутствует ли класс 'alert-danger'
        в классе поля 'zip-code'.

        :return: bool — True, если в классе поля присутствует 'alert-danger'.
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка успешного заполнения всех полей")
    def check_fields_success(self) -> bool:
        """
        Проверяет наличие класса 'success' во всех тестовых полях формы.

        :return: bool — True, если все поля имеют класс 'success';
        False, если хотя бы одно поле не имеет этого класса.
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка корректности отправки формы")
    def check_form_submission(self) -> None:
        """
        Проверяет два условия: наличие ошибки в поле ZIP-кода
        и успешное заполнение всех остальных полей.
        Если одно из условий не выполняется,
        будет вызвано исключение AssertionError.
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()
