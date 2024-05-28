from page_objects.registration_page import RegistrationPage


def test_registration_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(*RegistrationPage.HEADER)
    browser.find_element(*RegistrationPage.FIRSTNAME_INPUT)
    browser.find_element(*RegistrationPage.LASTNAME_INPUT)
    browser.find_element(*RegistrationPage.EMAIL_INPUT)
    browser.find_element(*RegistrationPage.PASSWORD_INPUT)
