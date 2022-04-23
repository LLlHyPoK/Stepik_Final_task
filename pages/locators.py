from curses import BUTTON1_DOUBLE_CLICKED
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocator():
    ADD_TO_BASKET_BUTTON = (
        By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_IN_BUSKET_MESSAGE = (
        By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    PRODUCT_PRICE = (
        By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    BASKET_PRICE_MESSAGE = (
        By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]')
    BASKET_PRICE = (
        By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]//div//p//strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocator():
    BASKET_IS_EMPTY_LINK = (By.XPATH, '//div[@id="content_inner"]')
    ITEMS_TO_BY_NOW_LINK = (By.XPATH, '//h2[class="col-sm-6 h3"]')


class LoginPageLocators():
    EMAIL_REGISTER_LINK = (By.XPATH, '//input[@id="id_registration-email"]')
    PASSWORD_REGISTER_LINK = (
        By.XPATH, '//input[@id="id_registration-password1"]')
    PASSWORD_CONFIRM_REGISTER_LINK = (
        By.XPATH, '//input[@id="id_registration-password2"]')
    BUTTON_REGISTER_LINK = (
        By.XPATH, '//button[@class="btn btn-lg btn-primary"][@name="registration_submit"]')
