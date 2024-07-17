import allure

from page_objects.ProductCardPage import ProductPage


@allure.feature("Product Card Page")
@allure.title("Check elements on page")
def test_product_page(browser):
    ProductPage(browser).check_elements_on_page()
