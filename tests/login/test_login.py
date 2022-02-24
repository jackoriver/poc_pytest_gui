from tests.pages.AccountPage import AccountPage
from tests.pages.LoginPage import LoginPage

from pytest import mark


def test_open_login_page(browser, base_url):
    login_page = LoginPage(browser)
    login_page.navigate_to(base_url + '/my-account')
    assert login_page.get_password_input.is_displayed()
    assert login_page.get_username_input.is_displayed()
    assert login_page.get_login_button.is_displayed()


def test_login_with_correct_creds(browser, base_url):
    login_page = LoginPage(browser)
    account_page = AccountPage(browser)
    username = 'catta'
    login_page.navigate_to(base_url + '/my-account')
    login_page.login_app(username, 'Sentalf12!')
    assert f"Hello {username}" in account_page.get_greet_message.text
