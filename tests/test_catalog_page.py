from page_objects.CatalogPage import CatalogPage


def test_catalog_page(browser):
    CatalogPage(browser).check_elements_on_page()


def test_change_currency(browser):
    CatalogPage(browser).change_currency()
