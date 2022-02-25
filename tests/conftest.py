from pytest import fixture
from selenium import webdriver
import logging as logger

from tests.config import Config


def pytest_addoption(parser):
    """
    This method adds the ability to pass a parameter (addoption) to be used by pytest by command line.
    i.e: add --env to store the environment where the tests are running, qa/dev/prod
    user%:  pytest --env=qa or pytest --env qa

    It also allows to add custom option in the pytest.ini: url to be used to store the testing url
    [pytest]
    url = http://test-env.com
    """
    parser.addoption("--env", action="store", help="Environment to run tests against")
    parser.addini(name='env', type="string", default="dev", help="Environment to run tests against")
    parser.addini(name='url', type='string', help="URL to run tests against")


@fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    logger.info("opening browser")
    set_browser_default_size(browser)
    browser.delete_all_cookies()
    browser.implicitly_wait(30)
    browser.set_page_load_timeout(30)
    yield browser
    browser.quit()


@fixture(scope='session')
def env_cli(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def env(request):
    return request.config.getini("env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(scope='session')
def app_url(request):
    return request.config.getini("url")


def set_browser_default_size(browser):
    try:
        logger.info("maximize browser")
        browser.maximize_window()
    except Exception as e:
        logger.warning(f"Browser could not be maximized, setting the window size to 1920x1080. More info: {e}")
        browser.set_window_size(1920, 1080)

