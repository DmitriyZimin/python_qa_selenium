from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.CSS_SELECTOR, "[name='search']")
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
