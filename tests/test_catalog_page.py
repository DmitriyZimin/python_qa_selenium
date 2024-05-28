from page_objects.catalog_page import CatalogPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser):
    browser.get(browser.url + "/catalog/desktops")
    browser.find_element(*CatalogPage.HEADER)
    browser.find_element(*CatalogPage.LEFT_COLUMN)
    browser.find_element(*CatalogPage.PRODUCT_LIST)
    browser.find_element(*CatalogPage.SORT_INPUT)
    browser.find_element(*CatalogPage.INPUT_LIMIT)


def test_change_currency(browser):
    WebDriverWait(browser, timeout=1).until(
        EC.text_to_be_present_in_element(CatalogPage.ELEMENT_PRICE, "$110.00")
    )
    browser.find_element(*CatalogPage.CURRENCY_BUTTON).click()
    browser.find_element(*CatalogPage.CURRENCY_EURO).click()
    WebDriverWait(browser, timeout=1).until(
        EC.text_to_be_present_in_element(CatalogPage.ELEMENT_PRICE, "86.31€")
    )
