from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timezone

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"
driver = webdriver.Chrome(PATH)

now = datetime.now(timezone.utc)


def find_element(driver, search_type, value):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((search_type, value)))
    return element


try:
    driver.get(URL)
    driver.maximize_window()

    passenger_input = driver.find_element_by_id("passenger")
    departure_date = driver.find_element_by_id("departure-date")
    departure_time = driver.find_element_by_id("departure-time")
    ticket_btn = driver.find_element_by_id("issue-ticket")
    date = now.strftime("%Y/%m/%d")
    time = now.strftime("%I:%M")
    name = "Gergely"

    passenger_input.send_keys(name)
    departure_date.send_keys(date)
    departure_time.send_keys(time)
    ticket_btn.click()

    passenger_name = find_element(driver, By.ID, "passenger-name")
    assert passenger_name.text == f"{name}", "Test Failed: Nem jó név szerepel."

    departure_date_text = find_element(driver, By.ID, "departure-date-text")
    assert departure_date_text.text == f"{date}", "Test Failed: Nem jó dátum szerepel."

    side_departure_date = find_element(driver, By.ID, "side-departure-date")
    assert departure_date_text.text == f"{date}", "Test Failed: Nem jó dátum szerepel."

    departure_time_text = find_element(driver, By.ID, "departure-time-text")
    assert departure_time_text.text == f"{time}", "Test Failed: Nem jó idő szerepel."

    side_departure_time = find_element(driver, By.ID, "side-departure-time")
    assert departure_time_text.text == f"{time}", "Test Failed: Nem jó idő szerepel."

finally:
    driver.quit()
