"""Open “Frames”, click on “iFrame”, switch to the iframe, type text to the field."""
import time

from selenium.webdriver.common.by import By


def test_frames(navigate_to_url):
    driver = navigate_to_url
    frames = driver.find_element("xpath", '//*[@id="content"]/ul/li[22]/a')
    frames.click()
    iframe_point = driver.find_element(By.LINK_TEXT, "iFrame")
    iframe_point.click()
    iframe = driver.find_element(By.ID, "mce_0_ifr")
    driver.switch_to.frame(iframe)
    text = driver.find_element(By.ID, "tinymce")
    text.clear()
    text.send_keys("Hello")
    driver.switch_to.default_content()
