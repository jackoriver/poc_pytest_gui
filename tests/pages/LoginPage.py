from selenium.webdriver.common.by import By
from tests.pages.BasePage import BasePage
from tests.utils.botstyle import write_in_field


class LoginPage(BasePage):
    # Locators
    USERNAME = By.ID, 'username'
    PASSWORD = By.ID, 'password'
    LOGIN_BUTTON = By.CSS_SELECTOR, '.woocommerce-form-login__submit'
    ERROR_MESSAGE = By.CSS_SELECTOR, '.woocommerce-error'

    # Functions
    @property
    def get_username_input(self):
        return self.find_element(*self.USERNAME)

    @property
    def get_password_input(self):
        return self.find_element(*self.PASSWORD)

    @property
    def get_error_login_message(self):
        return self.find_element(*self.ERROR_MESSAGE)

    @property
    def get_login_button(self):
        return self.find_element(*self.LOGIN_BUTTON)

    def login_app(self, username, password):
        write_in_field(self.get_username_input, username)
        write_in_field(self.get_password_input, password)
        self.get_login_button.click()

