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
        By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"]//div[@class="alertinner "]')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    PRODUCT_PRICE = (
        By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    BASKET_PRICE_MESSAGE = (
        By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]')
    BASKET_PRICE = (
        By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]//div//p//strong')
