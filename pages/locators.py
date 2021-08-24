from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    
    LOGIN_REGISTRATION_EMAIL = "#id_registration-email"
    LOGIN_REGISTRATION_PASSWORD1 = "#id_registration-password1"
    LOGIN_REGISTRATION_PASSWORD2 = "#id_registration-password2"


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")    
    
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    
    MESSAGE_ALERT_BASKET_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_ALERT_BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    MESSAGE_ALERT_SUCCES_DIV1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    MESSAGE_ALERT_SUCCES_DIV2 = (By.CSS_SELECTOR, "#messages > div:nth-child(2)")
    
