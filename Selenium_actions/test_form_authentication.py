"""Open “Form Authentication”, login with the credentials,
verify “You logged into a secure area!” message on the page."""
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_authentication(navigate_to_url):
    driver = navigate_to_url
    form_authentication = driver.find_element("xpath", '//*[@id="content"]/ul/li[21]/a')
    form_authentication.click()
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    login_button = driver.find_element("xpath", '//*[@id="login"]/button/i')
    login_button.click()
    success_message = driver.find_element(By. CSS_SELECTOR, ".flash.success")
    assert "You logged into a secure area!" in success_message.text
