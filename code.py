from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import keyboard
import time


email = "nir123211@gmail.com"
password = "Nir322776790"


PATH = "C:\Program Files (x86)\ChromeWebDriver\chromedriver.exe"
driver = wd.Chrome(PATH)
driver.get("https://linkedin.com")

driver.maximize_window()
time.sleep(1)

email_bar = driver.find_element_by_id("session_key")
email_bar.send_keys(email)
time.sleep(1)

password_bar = driver.find_element_by_id("session_password")
password_bar.send_keys(password)
time.sleep(1)

password_bar.send_keys(Keys.RETURN)
time.sleep(1)

search_bar = driver.find_element_by_id("global-nav-typeahead")
search_bar.click()
time.sleep(1)

keyboard.write("im hiring")
time.sleep(1)
keyboard.press("enter")
time.sleep(1)

all_people = driver.find_element_by_class_name("artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 search-reusables__filter-pill-button search-reusables__filter-pill-button")
all_people.click()