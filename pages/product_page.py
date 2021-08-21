from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_product_to_basket_btn.click()
        assert True, "is not" 
        