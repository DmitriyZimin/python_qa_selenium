from page_objects.ProductCardPage import ProductPage


def test_product_page(browser):
    ProductPage(browser).check_elements_on_page()
