import time
import math
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(
            *ProductPageLocator.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
        button_add_to_basket.click()
        time.sleep(5)
        self.should_see_product_in_basket_message()
        self.product_name_in_basket_should_be_wright()
        self.should_be_basket_price_message()
        self.product_price_should_be_equal_basket_price()

    def should_see_product_in_basket_message(self):
        # проверка на то, что появляется сообщение о добавлении товара в корзину
        book_in_busket_message = self.browser.find_element(
            *ProductPageLocator.PRODUCT_IN_BUSKET_MESSAGE).is_displayed()

    def product_name_in_basket_should_be_wright(self):
        # проверка на то, что имя товара в корзине совпадает с тем, что закинули в корзину:
        book_name = self.browser.find_element(
            *ProductPageLocator.PRODUCT_NAME).text
        book_in_busket_message = self.browser.find_element(
            *ProductPageLocator.PRODUCT_IN_BUSKET_MESSAGE).text
        assert book_name + ' has been added to your basket.' == book_in_busket_message

    def should_be_basket_price_message(self):
        # проверка на то, что есть сообщение с ценой корзины
        book_price_message = self.browser.find_element(
            *ProductPageLocator.BASKET_PRICE_MESSAGE).is_displayed()

    def product_price_should_be_equal_basket_price(self):
        # проверка на то, что цена товара совпадает с ценой в корзине
        book_price = self.browser.find_element(
            *ProductPageLocator.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(
            *ProductPageLocator.BASKET_PRICE).text
        assert book_price == basket_price

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(1)
        alert.accept()
        time.sleep(1)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
