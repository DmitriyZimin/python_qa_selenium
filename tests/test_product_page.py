from page_objects.LoginPage import LoginPage
from page_objects.AdminPage import AdminPage
from page_objects.ProductPage import ProductPage

PRODUCT_NAME = "iPAD 18"


def test_product_creation(browser):
    LoginPage(browser).login_user()
    AdminPage(browser).open_products_page()
    ProductPage(browser).create_new_product(PRODUCT_NAME)


def test_product_deletion(browser):
    LoginPage(browser).login_user()
    AdminPage(browser).open_products_page()
    ProductPage(browser).delete_product(PRODUCT_NAME)
