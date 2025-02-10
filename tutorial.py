from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service= service)

driver.get("https://www.facebook.com")

title = driver.title

driver.implicitly_wait(10)

email_box = driver.find_element(by=By.NAME, value="email")
pass_box = driver.find_element(by=By.NAME, value="pass")
submit_button = driver.find_element(by=By.NAME, value="login")

email_box.send_keys("")
pass_box.send_keys("")

submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

time.sleep(10)

driver.quit()
