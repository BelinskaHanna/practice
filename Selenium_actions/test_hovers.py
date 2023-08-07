"""Open “Hovers”, hover on the 2nd photo, click on “View profile”, verify that “Not Found” is on the page."""
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By


def test_hovers(navigate_to_url):
    driver = navigate_to_url
    hovers = driver.find_element("xpath", '//*[@id="content"]/ul/li[25]/a')
    hovers.click()
    photo_element = driver.find_element(By.CSS_SELECTOR, ".figure:nth-child(4)")
    actions = ActionChains(driver)
    actions.move_to_element(photo_element).perform()
    view_profile = driver.find_element("xpath", '//*[@id="content"]/div/div[2]/div/a')
    view_profile.click()
    assert "Not Found" in driver.page_source
