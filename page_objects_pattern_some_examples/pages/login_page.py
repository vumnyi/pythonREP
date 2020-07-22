from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), 'Не найден элемент для ввода логина'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'Не найден элемент для ввода пароля'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), 'Не найден элемент для ввода почты'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), 'Не найден элемент для ввода пароля'
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM), 'Не найден элемент для ввода пароля повторно'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def assert_user_login(self):
        assert self.is_element_present(*BasePageLocators.ACCOUNT_LINK), 'Не найдено ссылки на аккаунт'
