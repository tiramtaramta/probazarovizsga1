from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html"
driver = webdriver.Chrome(PATH)

try:
    driver.get(URL)
    driver.maximize_window()

    generate_btn = driver.find_element_by_id("draw-number")
    reset_btn = driver.find_element_by_id("reset-numbers")

    # TC 01
    numbers = driver.find_elements_by_class_name("balls")
    if len(numbers) == 0:
        print("ok. nincsenek számok a képernyőn")
    else:
        print("A sorsolás nem megengedett. ")

    # TC 02
    for i in range(7):
        generate_btn.click()

    numbers = driver.find_elements_by_class_name("balls")
    six = 0
    for n in numbers:
        szam = int(n.text)
        six += 1
        if szam < 1 or szam > 59:
            print("A szám nem megfelelő értékű.")
        else:
            pass
        if six > 6:
            print("Több, mint 6db számot húztak.")
        else:
            pass

    # TC 03
    for i in range(8):
        generate_btn.click()

    numbers = driver.find_elements_by_class_name("balls")
    six = 0
    for n in numbers:
        szam = n.text
        six += 1
        if six > 6:
            print("Több, mint 6db számot húztak.")
        else:
            pass

    reset_btn.click()
    numbers = driver.find_elements_by_class_name("balls")
    if len(numbers) == 0:
        print("ok. a számok törlődtek")

finally:
    driver.quit()
