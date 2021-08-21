from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_product_to_basket_btn.click()
        assert True, "is not" 


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
        