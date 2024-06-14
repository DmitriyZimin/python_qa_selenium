from page_objects.MainPage import MainPage


def test_main_page(browser):
    MainPage(browser).check_elements_on_page()


def test_empty_cart(browser):
    MainPage(browser).empty_cart()


def test_change_currency(browser):
    MainPage(browser).change_currency()


def test_add_product_to_cart(browser):
    MainPage(browser).add_product_to_cart()
