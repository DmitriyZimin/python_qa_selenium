from selenium.webdriver.common.by import By


class ProductPage:
    HEADER = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-new")
    CART_BUTTON = (By.CSS_SELECTOR, "#header-cart button")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    NAVIGATION_TAB = (By.CSS_SELECTOR, ".nav-tabs")
