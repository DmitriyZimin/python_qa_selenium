from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    CARD_HEADER = (By.CSS_SELECTOR, "div.card-header")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    FOOTER = (By.CSS_SELECTOR, "#footer")
    USER_LOGIN = (By.CSS_SELECTOR, "[alt='John Doe']")
    USERNAME = "user"
    PASSWORD = "bitnami"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.driver.url + "/administration")

    def check_elements_on_page(self):
        self.element(self.CARD_HEADER)
        self.element(self.USERNAME_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.SUBMIT_BUTTON)
        self.element(self.FOOTER)

    def input_all_fields(self):
        self._send_keys(self.USERNAME_INPUT, LoginPage.USERNAME)
        self._send_keys(self.PASSWORD_INPUT, LoginPage.PASSWORD)
        self.element(self.SUBMIT_BUTTON).click()

    def login_user(self):
        self.input_all_fields()
        self.element(self.USER_LOGIN)
