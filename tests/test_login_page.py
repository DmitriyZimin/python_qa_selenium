from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_page import LoginPage


def test_login_page(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(*LoginPage.CARD_HEADER)
    browser.find_element(*LoginPage.USERNAME_INPUT)
    browser.find_element(*LoginPage.PASSWORD_INPUT)
    browser.find_element(*LoginPage.SUBMIT_BUTTON)
    browser.find_element(*LoginPage.FOOTER)
    browser.find_element(*LoginPage.USERNAME_INPUT).send_keys(LoginPage.USERNAME)
    browser.find_element(*LoginPage.PASSWORD_INPUT).send_keys(LoginPage.PASSWORD)
    browser.find_element(*LoginPage.SUBMIT_BUTTON).click()
    WebDriverWait(browser, timeout=1).until(
        EC.visibility_of_element_located(LoginPage.USER_LOGIN)
    )
