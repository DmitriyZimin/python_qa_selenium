from selenium.webdriver.common.by import By


class LoginPage:
    CARD_HEADER = (By.CSS_SELECTOR, "div.card-header")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    FOOTER = (By.CSS_SELECTOR, "#footer")
    USER_LOGIN = (By.CSS_SELECTOR, "[alt='John Doe']")
    USERNAME = "user"
    PASSWORD = "bitnami"
