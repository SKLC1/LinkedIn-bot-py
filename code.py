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
time.sleep(2)

filter_by_people_btn = driver.find_element_by_css_selector("button[aria-pressed='false']")
filter_by_people_btn.click()
time.sleep(2)

all_btns = driver.find_elements_by_tag_name("button")
connect_btns_arr = [btn for btn in all_btns if btn.text == "Connect"]

for btn in connect_btns_arr:
  driver.execute_script("arguments[0].click();",btn)
  time.sleep(2)
  send = driver.find_element_by_xpath('//button[@aria-label="Send now"]')
  driver.execute_script("arguments[0].click();", send)
  time.sleep(2)