import allure

from page_objects.MainPage import MainPage


@allure.feature("Main Page")
@allure.title("Check elements on page")
def test_main_page(browser):
    MainPage(browser).check_elements_on_page()


@allure.feature("Main Page")
@allure.title("Check empty cart")
def test_empty_cart(browser):
    MainPage(browser).empty_cart()


@allure.feature("Main Page")
@allure.title("Check change currency")
def test_change_currency(browser):
    MainPage(browser).change_currency()


@allure.feature("Main Page")
@allure.title("Check add product to cart")
def test_add_product_to_cart(browser):
    MainPage(browser).add_product_to_cart()
