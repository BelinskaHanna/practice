"""Open “Inputs”, type any number to the field."""


def test_inputs(navigate_to_url):
    driver = navigate_to_url
    inputs = driver.find_element("xpath", '//*[@id="content"]/ul/li[27]/a')
    inputs.click()
    input_field = driver.find_element("xpath", '//*[@id="content"]/div/div/div/input')
    input_field.send_keys("123456789")
    assert input_field.get_attribute("value") == "123456789"
