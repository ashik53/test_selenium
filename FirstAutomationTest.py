from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:\\BrowserDriver\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


driver.get("https://rcvacademy.com")
driver.maximize_window
print(driver.title)
if driver.title == "Home El - RCV Academy":
    assert True
else:
    assert False
driver.close()




