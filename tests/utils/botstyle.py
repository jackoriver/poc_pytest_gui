def write_in_field(web_element, text, clear=True):
    """
    This method types the provided text in a textfield.
    params:
    web_element = web element
    text = the string you need to type in the field
    """
    if clear:
        web_element.clear()
    web_element.send_keys(text)


def click_on_button_js(driver, web_element):
    """
    This method clicks on a button using JS which helps us when
    the button is hidden or behind another element.
    driver = driver instance
    web_element = web element
    returns nothing
    """
    driver.execute_script(f"arguments[0].click();", web_element)


def scroll_to_element(driver, web_element):
    """
    This method scrolls to find a web element helps us when
    the element is not visible.
    driver = driver instance
    web_element = web element
    returns nothing
    """
    driver.execute_script("arguments[0].scrollIntoView();", web_element)
