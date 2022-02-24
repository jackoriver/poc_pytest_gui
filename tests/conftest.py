from pytest import fixture
from selenium import webdriver
import logging as logger


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


def set_browser_default_size(browser):
    try:
        logger.info("maximize browser")
        browser.maximize_window()
    except Exception as e:
        logger.warning(f"Browser could not be maximized, setting the window size to 1920x1080. More info: {e}")
        browser.set_window_size(1920, 1080)

