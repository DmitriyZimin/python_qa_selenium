from page_objects.LoginPage import LoginPage


def test_login_page(browser):
    LoginPage(browser).check_elements_on_page()
    LoginPage(browser).login_user()
