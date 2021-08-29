from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE_ROW, timeout=1), "Basket not empty"

    def should_not_be_product_in_basket(self):
        text_empty = {
            "en-gb": "Your basket is empty",
            "en": "Your basket is empty",
            "ru": "Ваша корзина пуста",
            "es": "Tu carrito esta vacío",
            "fr": "Votre panier est vide",
            "de": "Ihr Warenkorb ist leer"}
        
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTALS), "Product in basket, but should not be"
        text_empty_basket = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        language = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
        assert text_empty[language] in text_empty_basket, "Empty basket text not found"
        