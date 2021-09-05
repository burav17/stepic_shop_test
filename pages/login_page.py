from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Failed to open login URL"     


    def should_be_login_form(self):
       assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION_EMAIL), "Email field not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD1), "Pass field not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD2), "Confirm pass field not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION_BTN), "Register button not presented"

        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_BTN).click()

