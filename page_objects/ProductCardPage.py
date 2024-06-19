from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-new")
    CART_BUTTON = (By.CSS_SELECTOR, "#header-cart button")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    NAVIGATION_TAB = (By.CSS_SELECTOR, ".nav-tabs")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.driver.url + "/product/smartphone/htc-touch-hd")

    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.PRODUCT_PRICE)
        self.element(self.CART_BUTTON)
        self.element(self.QUANTITY_INPUT)
        self.element(self.NAVIGATION_TAB)
