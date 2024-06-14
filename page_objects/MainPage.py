from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "[id='search']")
    NAVIGATION_BAR = (By.CSS_SELECTOR, "#narbar-menu")
    CART_BUTTON = (By.CSS_SELECTOR, "#header-cart button")
    OPENCART_TITLE = (By.CSS_SELECTOR, "[title = 'Your Store']")
    TOP_BAR = (By.CSS_SELECTOR, "#top")
    EMPTY_SHOPPING_CART = (By.CSS_SELECTOR, "[class='text-center p-4']")
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "[formaction*='checkout/cart.add']")
    NOT_EMPTY_SHOPPING_CART = (By.CSS_SELECTOR, "[class='dropdown-menu dropdown-menu-end p-2 show']")
    SHOPPING_CART_ALERT = (By.CSS_SELECTOR, "[class='alert alert-success alert-dismissible']")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency>div")
    CURRENCY_EURO = (By.CSS_SELECTOR, "[href='EUR']")
    ELEMENT_PRICE = (By.CSS_SELECTOR, "[class='price-new']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.driver.url)

    def check_elements_on_page(self):
        self.element(self.SEARCH_INPUT)
        self.element(self.NAVIGATION_BAR)
        self.element(self.CART_BUTTON)
        self.element(self.OPENCART_TITLE)
        self.element(self.TOP_BAR)

    def change_currency(self):
        self.element(self.CURRENCY_BUTTON).click()
        self.element(self.CURRENCY_EURO).click()
        self.element_text(self.ELEMENT_PRICE, "472.33€")

    def empty_cart(self):
        self.element(self.CART_BUTTON).click()
        self.element(self.EMPTY_SHOPPING_CART)
        self.element_text(self.EMPTY_SHOPPING_CART, "Your shopping cart is empty!")

    def add_product_to_cart(self):
        self.element(self.ADD_CART_BUTTON).click()
        self.element_invisibility(self.SHOPPING_CART_ALERT)
        self.element(self.CART_BUTTON).click()
        self.element(self.NOT_EMPTY_SHOPPING_CART)
