from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

# initialize chrome webdriver
driver = Chrome("C://Users//liart//Downloads//chromedriver_win32//chromedriver.exe")

# open this url
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

username_field = driver.find_element(By.ID, "my-text-id")
username_field.send_keys("Arturo")

password_field = driver.find_element(By.NAME, "my-password")
password_field.send_keys("12345678")

text_field = driver.find_element(By.NAME, "my-textarea")
text_field.send_keys("typed by script!")

# keep open for 10 seconds
time.sleep(10)

# close window
driver.quit()
