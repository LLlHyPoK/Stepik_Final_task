import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocator
import pytest


@pytest.mark.login_page
class TestLoginFromMainPage():
    @pytest.mark.xfail
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page = main_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        assert basket_page.is_not_element_present(
            *BasketPageLocator.ITEMS_TO_BY_NOW_LINK)
        assert basket_page.is_element_present(
            *BasketPageLocator.BASKET_IS_EMPTY_LINK)
