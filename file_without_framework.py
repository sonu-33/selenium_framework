import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless") # This is used to run the test in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # This is run with browser open mode
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options) # This is to run in headless mode

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(10)
user_name = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

user_name.send_keys("Admin")
password.send_keys("admin123")
login_button.click()

time.sleep(5)
print("End of Program")
