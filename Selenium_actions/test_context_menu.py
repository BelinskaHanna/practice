"""Open “Context menu”, click OK on the alert."""
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By


def test_context_menu_and_alert(navigate_to_url):
    driver = navigate_to_url
    context_menu = driver.find_element("xpath", '//*[@id="content"]/ul/li[7]/a')
    context_menu.click()
    box = driver.find_element("xpath", '//*[@id="hot-spot"]')
    actions = ActionChains(driver)
    actions.context_click(box).perform()
    alert = driver.switch_to.alert
    alert.accept()
