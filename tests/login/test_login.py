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



def test_login_with_non_existent_user(browser, base_url):
    login_page = LoginPage(browser)
    username = 'non_exist'
    login_page.navigate_to(base_url + '/my-account')
    login_page.login_app(username, 'password')
    assert f"The username {username} is not registered on this site. If you are unsure of your username, try your email address instead." in login_page.get_error_login_message.text


def test_login_cannot_access_with_incorrect_password(browser, base_url):
    login_page = LoginPage(browser)
    username = 'catta'
    password = 'incorrect'
    login_page.navigate_to(base_url + '/my-account')
    login_page.login_app(username, password)
    assert f"Error: The password you entered for the username {username} is incorrect. Lost your password?" in login_page.get_error_login_message.text


def test_url_from_pytest_ini(app_config):
    assert app_config.base_url == 'http://www.fidelitasplayground.xyz/my-account'