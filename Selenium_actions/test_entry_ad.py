"""Open “Entry Ad”, close the ad, click on the “click here” link"""
import time


def test_entry_ad(navigate_to_url):
    driver = navigate_to_url
    entry_ad = driver.find_element("xpath", '//*[@id="content"]/ul/li[15]/a')
    entry_ad.click()
    click_here = driver.find_element("xpath", '//*[@id="restart-ad"]')
    click_here.click()
    time.sleep(1)
    pop_up = driver.find_element("xpath", '//*[@id="modal"]/div[2]/div[3]/p')
    pop_up.click()
