import allure

from page_objects.LoginPage import LoginPage


@allure.feature("Login Page")
@allure.title("Check login page")
def test_login_page(browser):
    LoginPage(browser).check_elements_on_page()
    LoginPage(browser).login_user()
