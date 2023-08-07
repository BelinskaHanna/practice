from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


def test_open_an_alert(navigate_to_url):
    driver = navigate_to_url
    open_an_alert = driver.find_element(By.XPATH, '//*[@id="alert"]')
    open_an_alert.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    ActionChains(driver)
    alert = driver.switch_to.alert
    assert "I got opened after 5 secods" in alert.text
    alert.accept()


def test_change_text(navigate_to_url):
    driver = navigate_to_url
    change_text = driver.find_element(By.XPATH, '//*[@id="populate-text"]')
    change_text.click()
    wait = WebDriverWait(driver, 15)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="h2"]'), "Selenium Webdriver"))


def test_display_button(navigate_to_url):
    driver = navigate_to_url
    display_button = driver.find_element(By.XPATH, '//*[@id="display-other-button"]')
    display_button.click()
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="hidden"]')))
    button.click()


def test_enable_button(navigate_to_url):
    driver = navigate_to_url
    enable_button = driver.find_element(By.XPATH, '//*[@id="enable-button"]')
    enable_button.click()
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="disable"]')))
    button.click()


def test_check_checkbox(navigate_to_url):
    driver = navigate_to_url
    check_checkbox = driver.find_element(By.XPATH, '//*[@id="checkbox"]')
    check_checkbox.click()
    wait = WebDriverWait(driver, 15)
    check = wait.until(EC.element_located_selection_state_to_be((By.XPATH, '//*[@id="ch"]'), True))
    assert check
