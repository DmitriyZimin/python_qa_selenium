from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    MENU = (By.CSS_SELECTOR, "#menu")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCT_MENU_ITEM = (By.LINK_TEXT, 'Products')

    def open_products_page(self):
        catalog = self.element(self.CATALOG)
        catalog.click()
        product_item = catalog.find_element(*self.PRODUCT_MENU_ITEM)
        product_item.click()
