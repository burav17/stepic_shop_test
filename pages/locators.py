from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    LOGIN_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_REGISTRATION_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


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


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p") # Корзина пуста
    # если в корзине есть товар
    BASKET_TITLE_ROW = (By.CSS_SELECTOR, "#content_inner div.basket-title div.row") # Заголовки в корзине
    BASKET_TOTALS = (By.CSS_SELECTOR, "#basket_totals") # Корзина готовая к оформлению
    