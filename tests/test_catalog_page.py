import allure

from page_objects.CatalogPage import CatalogPage


@allure.feature("Catalog Page")
@allure.title("Check elements on page")
def test_catalog_page(browser):
    CatalogPage(browser).check_elements_on_page()


@allure.feature("Catalog Page")
@allure.title("Check change currency")
def test_change_currency(browser):
    CatalogPage(browser).change_currency()
