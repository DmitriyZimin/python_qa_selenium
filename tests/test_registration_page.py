import allure

from page_objects.RegistrationPage import RegistrationPage


@allure.feature("Registration Page")
@allure.title("Check register new user")
def test_registration_page(browser):
    RegistrationPage(browser).check_elements_on_page()
    RegistrationPage(browser).register_new_user()
