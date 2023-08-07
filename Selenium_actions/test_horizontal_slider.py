"""Open “Horizontal Slider”, move the slider to 4.5
(use action.drag_and_drop_by_offset(slider, 50, 0).perform() and move to 3 using arrow keys."""
import time

from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By


def test_horizontal_slider(navigate_to_url):
    driver = navigate_to_url
    horizontal_slider = driver.find_element("xpath", '//*[@id="content"]/ul/li[24]/a')
    horizontal_slider.click()
    slider = driver.find_element(By.CSS_SELECTOR, ".sliderContainer input[type='range']")
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(45, 0).release().perform()
    time.sleep(1)
    actions.click(slider).send_keys(Keys.ARROW_RIGHT * 1).perform()
    time.sleep(1)
    slider_value = driver.find_element(By.ID, "range").text
    assert slider_value == "3"
