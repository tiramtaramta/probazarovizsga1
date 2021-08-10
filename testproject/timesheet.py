from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html"
driver = webdriver.Chrome(PATH)

try:
    driver.get(URL)
    driver.maximize_window()

    email_input = driver.find_element_by_xpath("//input[@placeholder='artist@moviemakr.com']")
    hours_input = driver.find_element_by_xpath("//input[@placeholder='hours']")
    minutes_input = driver.find_element_by_xpath("//input[@placeholder='minutes']")
    textarea = driver.find_element_by_tag_name("textarea")
    types_of_work = driver.find_element_by_id("dropDown")
    next_btn = driver.find_element_by_xpath("//input[@value='Next']")

    # TC 1
    email_input.send_keys("")
    assert not next_btn.is_enabled()

    email_input.send_keys("testbela.hu")
    assert not next_btn.is_enabled()
    email_input.clear()

    # TC 2
    email_input.send_keys("test@bela.hu")
    hours_input.send_keys("2")
    minutes_input.send_keys("0")
    textarea.send_keys("working hard")
    types_of_work.send_keys("Time working on visual effects for movie")
    next_btn.click()

    time.sleep(3)

    hour_for_assert = driver.find_element_by_css_selector("p:nth-child(2) span:nth-child(1)")
    minutes_for_assert = driver.find_element_by_css_selector("section[id='section-thankyou'] span:nth-child(2)")

    assert hour_for_assert.text == "2", "Test Failed: Nem jó érték szerepel az óra helyén."
    assert minutes_for_assert.text == "0", "Test Failed: Nem jó érték szerepel a perc helyén."

finally:
    driver.quit()
