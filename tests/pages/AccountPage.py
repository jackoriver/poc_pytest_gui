from selenium.webdriver.common.by import By
from tests.pages.BasePage import BasePage


class AccountPage(BasePage):
    # Selectors
    GREET_MESSAGE = By.CSS_SELECTOR, '.woocommerce-MyAccount-content > p:nth-child(2)'

    @property
    def get_greet_message(self):
        return self.find_element(*self.GREET_MESSAGE)

