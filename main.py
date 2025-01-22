from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sendemail

# -------------------- SCRAPE WENDY'S CHEESEBURGER MENU PAGE -------------------- #

# set up webdriver and provide link
driver = webdriver.Firefox()
driver.get("https://order.wendys.com/category/100/cheeseburgers?lang=en_CA")

# allow time for page to load, then close cookies prompt
time.sleep(5)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
time.sleep(5)

# scrape page for items in div, which gives cheeseburger menu options
elements = driver.find_elements(By.XPATH, "//body/div")
menu = elements[0].text
menu_list = menu.split("\n")

# creates a new list of only menu items containing "portabella"
portabellas = [item for item in menu_list if "portabella" in item.lower()]

# -------------------- SEND EMAIL -------------------- #
mailer = sendemail.CreateMail()

def check_portabella():
    if len(portabellas) > 1:
        return True
    else:
        return False

mailer.sendmail(check_portabella())
