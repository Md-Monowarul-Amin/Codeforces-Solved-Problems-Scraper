import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://facebook.com/")

# Wait for the user to manually solve CAPTCHA & log in
# input("Press Enter after logging in and solving CAPTCHA...")

# Save cookies
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))


time.sleep(100)
driver.quit()
