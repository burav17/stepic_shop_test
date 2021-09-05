# pytest -v --tb=line test_main_page.py
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
url_star_95 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('offer_num', ['0', '1', '2', '3', '4', '5', '6',
                                       pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_message_about_adding()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url_star_95)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, url_star_95)
    page.open()
    page.go_to_login_page()
    
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    

@pytest.mark.login_product_page_guest
class TestLoginFromProductPage():
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, url_star_95)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_can_go_to_login_page(self, browser):
        page = ProductPage(browser, url_star_95)
        page.open()
        page.should_be_login_link()


@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link_login = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link_login)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"      
        login_page.register_new_user(email, 'qwe123!@#')
        login_page.should_be_authorized_user()
        

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

  
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url)
        page.open()
        page.add_product_to_basket()
        page.should_be_add_to_basket()
        