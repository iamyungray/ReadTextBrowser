from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Konfiguration des Browsers
options = Options()
options.set_preference("dom.webnotifications.enabled", False)
options.add_argument("--start-maximized")
browser = webdriver.Firefox(options=options)

# Implizites Warten für alle Elemente im Browser hinzufügen
browser.implicitly_wait(10)

# URL aufrufen und Text auslesen
url = "https://www.example.com"
browser.get(url)
text = browser.find_element(By.TAG_NAME, "body").text

# Text verarbeiten
if "example" in text:
    print("Der Text enthält das Wort 'example'.")
    browser.get("http://hello.com")
    # auf "Português" klicken
    portuguese_tab = browser.find_element(By.LINK_TEXT, "Português")
    portuguese_tab.click()
    # auf "English" klicken
    english_tab = browser.find_element(By.LINK_TEXT, "English")
    english_tab.click()
    # Formular ausfüllen und abschicken
    form = browser.find_element(By.XPATH, "//form")
    inputs = form.find_elements(By.XPATH, "//input[@type='text']")
    inputs[0].send_keys("testmail@test.test")
    submit_button = form.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    # Neuen Tab öffnen und "https://www.calculator.net/date-calculator.html" aufrufen
    browser.execute_script("window.open('https://www.calculator.net/date-calculator.html','_blank')")
    browser.switch_to.window(browser.window_handles[1])

    # Unter dem Reiter "Start Date", "Dec" auswählen
    sleep(2)
    month_select = browser.find_element(By.ID, "today_Month_ID")
    month_select.select_by_value("11")
    calculate_button = form.find_element(By.XPATH, "//input[@type='Calculate']")
    calculate_button.click()

else:
    print("Der Text enthält das Wort 'example' nicht.")

# 5 Sekunden warten
sleep(1)
browser.quit()