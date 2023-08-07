"""Open “Dropdown”, select “Option 2”."""
from selenium.webdriver.support.ui import Select


def test_dropdown(navigate_to_url):
    driver = navigate_to_url
    dropdown = driver.find_element("xpath", '//*[@id="content"]/ul/li[11]/a')
    dropdown.click()
    select_dropdown = driver.find_element("xpath", '//*[@id="dropdown"]')
    select = Select(select_dropdown)
    select.select_by_index(2)
