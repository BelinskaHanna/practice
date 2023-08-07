"""Open “Key Presses”, press any key, verify that the key name is presented on the page."""


def test_key_presses(navigate_to_url):
    driver = navigate_to_url
    key_presses = driver.find_element("xpath", '//*[@id="content"]/ul/li[31]/a')
    key_presses.click()
    input_field = driver.find_element("xpath", '//*[@id="target"]')
    input_field.send_keys(" ")
    result = driver.find_element("id", "result").text
    assert "You entered: SPACE" in result
