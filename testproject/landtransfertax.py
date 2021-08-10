from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"
driver = webdriver.Chrome(PATH)

try:
    driver.get(URL)
    driver.maximize_window()

    go_btn = driver.find_element_by_class_name("btn-go")
    input_property = driver.find_element_by_id("price")
    input_fee = driver.find_element_by_id("tax")

    # TC 01
    go_btn.click()
    time.sleep(1)
    disclaimer = driver.find_element_by_css_selector("div[class='content'] p strong")
    assert_text = disclaimer.text
    assert input_fee.text == ""
    assert assert_text == "Enter the property value before clicking Go button."

    # TC 02
    input_property.send_keys("33333")
    go_btn.click()
    assert input_fee.get_attribute("value") == "166.665"

finally:
    driver.quit()
