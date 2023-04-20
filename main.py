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

select_element = driver.find_element(By.NAME, "my-select")
dropdown_menu1 = driver.find_element(By.NAME, "my-select")
dropdown_menu1.click()
options = driver.find_elements(By.TAG_NAME, "option")
for option in options:
    if option.text == "One":
        option.click()
        dropdown_menu1.click()

dropdown_menu2 = driver.find_element(By.NAME, "my-datalist")
dropdown_menu2.send_keys("San Francisco")

box1 = driver.find_element(By.ID, "my-check-1")
box1.click()
box2 = driver.find_element(By.ID, "my-check-2")
box2.click()
select_radio = driver.find_element(By.ID, "my-radio-2")
select_radio.click()

date = driver.find_element(By.NAME, "my-date")
date.send_keys("10/10/2023")

submit = driver.find_element(By.TAG_NAME, "button")
submit.click()

# keep open for 10 seconds
time.sleep(10)

# close window
driver.quit()
