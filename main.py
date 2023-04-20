from selenium.webdriver import Chrome
import time

# initialize chrome webdriver
driver = Chrome("C://Users//liart//Downloads//chromedriver_win32//chromedriver.exe")

# open this url
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# keep open for 10 seconds
time.sleep(10)

# close window
driver.quit()
