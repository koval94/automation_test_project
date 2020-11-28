import time

import pytest
from selenium import webdriver


@pytest.mark.skip
def test_gecko(browser):
    browser.get("https://rozetka.com.ua/")
    time.sleep(2)
    assert False


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
