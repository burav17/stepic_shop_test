from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес        
        assert "login" in self.browser.current_url, "Failed to open login URL"     

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login form username field not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form password  field not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION_EMAIL), "Register form email field not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD1), "Register form password field not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD2), "Register form confirm password field not found"
        