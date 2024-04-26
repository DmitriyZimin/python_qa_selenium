from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage


def test_main_page(browser):
    browser.get(browser.url)
    browser.find_element(*MainPage.SEARCH_INPUT)
    browser.find_element(*MainPage.NAVIGATION_BAR)
    browser.find_element(*MainPage.CART_BUTTON)
    browser.find_element(*MainPage.OPENCART_TITLE)
    browser.find_element(*MainPage.TOP_BAR)


def test_empty_cart(browser):
    browser.find_element(*MainPage.CART_BUTTON).click()
    WebDriverWait(browser, timeout=1).until(
        EC.visibility_of_element_located(MainPage.EMPTY_SHOPPING_CART)
    )
    WebDriverWait(browser, timeout=1).until(
        EC.text_to_be_present_in_element(MainPage.EMPTY_SHOPPING_CART, "Your shopping cart is empty!")
    )


def test_change_currency(browser):
    browser.find_element(*MainPage.CURRENCY_BUTTON).click()
    browser.find_element(*MainPage.CURRENCY_EURO).click()
    WebDriverWait(browser, timeout=1).until(
        EC.text_to_be_present_in_element(MainPage.ELEMENT_PRICE, "472.33€")
    )


def test_add_product_to_cart(browser):
    WebDriverWait(browser, timeout=1).until(
        EC.element_to_be_clickable(MainPage.ADD_CART_BUTTON)
    )
    browser.find_element(*MainPage.ADD_CART_BUTTON).click()
    WebDriverWait(browser, timeout=7).until(
        EC.invisibility_of_element(MainPage.SHOPPING_CART_ALERT)
    )
    browser.find_element(*MainPage.CART_BUTTON).click()

    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(MainPage.NOT_EMPTY_SHOPPING_CART)
    )
