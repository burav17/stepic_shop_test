from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_product_to_basket_btn.click()


    def should_be_add_to_basket(self):
        self.should_be_match_product_name()
        self.should_be_match_price_product()


    def should_be_match_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert product_name == message_name, f"{product_name} is not {message_name}"


    def should_be_match_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert product_price == message_price, f"{product_price} not equal {message_price}"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


    def should_disappeared_message_about_adding(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should has dissapeared"        
    