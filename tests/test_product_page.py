from page_objects.product_page import ProductPage


def test_product_page(browser):
    browser.get(browser.url + "/product/smartphone/htc-touch-hd")
    browser.find_element(*ProductPage.HEADER)
    browser.find_element(*ProductPage.PRODUCT_PRICE)
    browser.find_element(*ProductPage.NAVIGATION_TAB)
    browser.find_element(*ProductPage.CART_BUTTON)
    browser.find_element(*ProductPage.QUANTITY_INPUT)
