from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "It is not login URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "No register form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(
            *LoginPageLocators.EMAIL_REGISTER_LINK)
        email_input.send_keys(email)
        password_input = self.browser.find_element(
            *LoginPageLocators.PASSWORD_REGISTER_LINK)
        password_input.send_keys(password)
        password_confirm = self.browser.find_element(
            *LoginPageLocators.PASSWORD_CONFIRM_REGISTER_LINK)
        password_confirm.send_keys(password)
        register_button = self.browser.find_element(
            *LoginPageLocators.BUTTON_REGISTER_LINK)
        register_button.click()
