from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from page_objects.BasePage import BasePage
import helpers


class ProductPage(BasePage):
    CREATE_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
    NAV_TAB_DATA = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
    SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, 'input[type=checkbox]')
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "input[id='input-name-1']")
    FILTER_NAME_INPUT = (By.CSS_SELECTOR, "input[name = 'filter_name']")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    PRODUCT_MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SEO_TAB = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(11) > a")
    SEO_INPUT = (By.CSS_SELECTOR, "input[placeholder='Keyword']")

    def click_add_new_product_button(self):
        self.element(self.CREATE_NEW_PRODUCT_BUTTON).click()

    def click_save_product_button(self):
        self.element(self.SAVE_PRODUCT_BUTTON).click()

    def click_nav_tab_data(self):
        self.element(self.NAV_TAB_DATA).click()

    def click_seo_tab_data(self):
        self.element(self.SEO_TAB).click()

    def click_filter_button(self):
        self.element(self.FILTER_BUTTON).click()

    def check_success_message(self):
        return self.element(self.SUCCESS_MESSAGE).text == "Success: You have modified products!"

    def create_new_product(self, product_name="ProductName1"):
        self.click_add_new_product_button()
        self._send_keys(self.PRODUCT_NAME_INPUT, product_name)
        self._send_keys(self.META_TAG_TITLE_INPUT, helpers.random_string())
        self.click_nav_tab_data()
        self._send_keys(self.PRODUCT_MODEL_INPUT, helpers.random_string())
        self.click_seo_tab_data()
        self._send_keys(self.SEO_INPUT, helpers.random_string())
        self.click_save_product_button()
        self.check_success_message()

    def delete_product(self, product_name):
        # self.click_filter_data()
        self._send_keys(self.FILTER_NAME_INPUT, product_name)
        self.click_filter_button()
        self.element(self.SELECT_ALL_CHECKBOX).click()
        self.element(self.DELETE_PRODUCT_BUTTON).click()
        Alert(self.driver).accept()
        self.check_success_message()
