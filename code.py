from selenium import webdriver as wd

print("Type your username")
username = input()

print("Type your password")
password = input()

print(username)
print(password)

PATH = "C:\Program Files (x86)\ChromeWebDriver\chromedriver.exe"
driver = wd.Chrome(PATH)
driver.get("https://linkedin.com")

