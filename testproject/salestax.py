from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html"
driver = webdriver.Chrome(PATH)

try:
    driver.get(URL)
    driver.maximize_window()

    subtotal_btn = driver.find_element_by_id("subtotalBtn")
    subtotal_btn.click()

    subtotal_input = driver.find_element_by_id("subtotal")
    subtotal_value = subtotal_input.get_attribute("value")
    assert subtotal_value == "0.00", "Test Failed: Nem jó érték szerepel subtotal."

    gtotal_btn = driver.find_element_by_id("gtotalBtn")
    gtotal_btn.click()

    total_input = driver.find_element_by_id("gtotal")
    total_value = total_input.get_attribute("value")
    assert total_value == "4.95", "Test Failed: Nem jó érték szerepel a total mezőben."

    driver.find_element_by_xpath("//option[normalize-space()='6\" x 6\" Volkanik Ice']").click()
    driver.find_element_by_id("quantity").send_keys("1")

    subtotal_btn.click()
    subtotal_input = driver.find_element_by_id("subtotal")
    subtotal_value = subtotal_input.get_attribute("value")
    assert subtotal_value == "4.95", "Test Failed: Nem jó érték szerepel subtotal."

    gtotal_btn.click()
    total_input = driver.find_element_by_id("gtotal")
    total_value = total_input.get_attribute("value")
    assert total_value == "9.90", "Test Failed: Nem jó érték szerepel a total mezőben."

finally:
    driver.quit()
