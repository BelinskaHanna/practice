import pytest

from selenium import webdriver


@pytest.fixture
def start_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def navigate_to_url(start_driver):
    driver = start_driver
    driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    yield driver
