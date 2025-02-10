from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service= service)

driver.get("https://facebook.com")

input_element = driver.find_element(By.CLASS_NAME, "inputtext _55r1 _6luy _9npi")
input_element.send_keys("tech with tim")


time.sleep(10)

driver.quit()
