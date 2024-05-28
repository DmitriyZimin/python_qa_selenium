from selenium.webdriver.common.by import By


class CatalogPage:
    HEADER = (By.CSS_SELECTOR, "h2")
    LEFT_COLUMN = (By.CSS_SELECTOR, "#column-left")
    PRODUCT_LIST = (By.CSS_SELECTOR, "#product-list")
    SORT_INPUT = (By.CSS_SELECTOR, "#input-sort")
    INPUT_LIMIT = (By.CSS_SELECTOR, "#input-limit")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency>div")
    CURRENCY_EURO = (By.CSS_SELECTOR, "[href='EUR']")
    ELEMENT_PRICE = (By.CSS_SELECTOR, "[class='price-new']")
