from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocator
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocator
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time
import pytest


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        EMAIL = str(time.time()) + "@fakemail.org"
        PASSWORD = '11asdfg22'
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(EMAIL, PASSWORD)
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_not_element_present(
            *ProductPageLocator.PRODUCT_IN_BUSKET_MESSAGE), "Элемент присутствует на странице"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    assert product_page.is_disappeared(
        *ProductPageLocator.PRODUCT_IN_BUSKET_MESSAGE), "Элемент присутствует на странице"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page = main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.is_not_element_present(
        *BasketPageLocator.ITEMS_TO_BY_NOW_LINK)
    assert basket_page.is_element_present(
        *BasketPageLocator.BASKET_IS_EMPTY_LINK)
