from selenium.webdriver.common.by import By

import helpers
from page_objects.BasePage import BasePage


class RegistrationPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    SUCCESS_MESSAGE_HEADER = (By.CSS_SELECTOR, "#content > h1")
    SUCCESS_MESSAGE_PARAGRAPH = (By.CSS_SELECTOR, "#content > p")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.driver.url + "/index.php?route=account/register")

    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.FIRSTNAME_INPUT)
        self.element(self.LASTNAME_INPUT)
        self.element(self.EMAIL_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.PRIVACY_POLICY_CHECKBOX)

    def input_all_fields(self):
        user_first_name = helpers.random_string(5)
        user_last_name = helpers.random_string(5)
        password = helpers.random_string(10)
        self._send_keys(self.FIRSTNAME_INPUT, user_first_name)
        self._send_keys(self.LASTNAME_INPUT, user_last_name)
        self._send_keys(self.EMAIL_INPUT, helpers.random_email())
        self.element(self.PRIVACY_POLICY_CHECKBOX).click()
        self._send_keys_enter(self.PASSWORD_INPUT, password)

    def check_registration_success(self):
        return self.element(self.SUCCESS_MESSAGE_HEADER) == "Your Account Has Been Created!" and \
               self.element(self.SUCCESS_MESSAGE_PARAGRAPH) == "Congratulations! Your new account has been successfully created!"

    def register_new_user(self):
        self.input_all_fields()
        self.check_registration_success()