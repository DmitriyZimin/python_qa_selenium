from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h2")
    LEFT_COLUMN = (By.CSS_SELECTOR, "#column-left")
    PRODUCT_LIST = (By.CSS_SELECTOR, "#product-list")
    SORT_INPUT = (By.CSS_SELECTOR, "#input-sort")
    INPUT_LIMIT = (By.CSS_SELECTOR, "#input-limit")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency>div")
    CURRENCY_EURO = (By.CSS_SELECTOR, "[href='EUR']")
    ELEMENT_PRICE = (By.CSS_SELECTOR, "[class='price-new']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.driver.url + "/catalog/desktops")

    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.LEFT_COLUMN)
        self.element(self.PRODUCT_LIST)
        self.element(self.SORT_INPUT)
        self.element(self.INPUT_LIMIT)

    def change_currency(self):
        self.element_text(self.ELEMENT_PRICE, "$110.00")
        self.element(self.CURRENCY_BUTTON).click()
        self.element(self.CURRENCY_EURO).click()
        self.element_text(self.ELEMENT_PRICE, "86.31€")
