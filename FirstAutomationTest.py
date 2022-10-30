from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rcvacademy.com")
driver.maximize_window
print(driver.title)
if driver.title == "Home El - RCV Academy2":
    assert True
else:
    assert False
driver.close()