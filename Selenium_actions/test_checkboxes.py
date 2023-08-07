"""Open “Checkboxes”, check the 1st item and uncheck the 2nd one."""


def test_checkboxes(navigate_to_url):
    driver = navigate_to_url
    checkbox_link = driver.find_element("xpath", '//*[@id="content"]/ul/li[6]/a')
    checkbox_link.click()
    checkbox_1 = driver.find_element("xpath", '//*[@id="checkboxes"]/input[1]')
    checkbox_1.click()
    checkbox_2 = driver.find_element("xpath", '//*[@id="checkboxes"]/input[2]')
    checkbox_2.click()
