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
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
    yield driver
