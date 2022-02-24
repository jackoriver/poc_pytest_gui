import logging as logger


class BasePage:

    def __init__(self, browser):
        self.driver = browser
        self.logger = logger
        self.logger.info("initialize bas page object")

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, by, value, verbose=True):
        try:
            return self.driver.find_element(by, value)
        except Exception as e:
            self.logger.warning(e) if verbose else None
            return None

    def find_elements(self, by, value):
        try:
            return self.driver.find_elements(by, value)
        except Exception as e:
            self.logger.warning(e)
            return None

    def find_element_from_element(self, base_element, by, value):
        try:
            return base_element.find_element(by, value)
        except Exception as e:
            self.logger.warning(e)
            return None

    def find_elements_from_element(self, base_element, by, value):
        try:
            return base_element.find_elements(by, value)
        except Exception as e:
            self.logger.warning(e)
            return None