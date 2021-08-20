from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    
    LOGIN_REGISTRATION_EMAIL = "#id_registration-email"
    LOGIN_REGISTRATION_PASSWORD1 = "#id_registration-password1"
    LOGIN_REGISTRATION_PASSWORD2 = "#id_registration-password2"
    