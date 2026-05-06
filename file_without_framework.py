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
driver.maximize_window()
time.sleep(5)
user_name = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

user_name.send_keys("Admin")
password.send_keys("admin123")
login_button.click()

time.sleep(5)

PIM_OPTION = driver.find_element (By.XPATH, "//span[normalize-space()='PIM']")
PIM_OPTION.click()
time.sleep(5)

EMP_ID = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(2) > div > div:nth-child(2) > input")

EMP_ID.click()
time.sleep(3)
EMP_ID.send_keys("777")

SEARCH = driver.find_element(By.XPATH, "//button[@type='submit']")

SEARCH.click()
time.sleep(5)

RESET=driver.find_element(By.XPATH,"//button[normalize-space()='Reset']")

RESET.click()
time.sleep(5)


print("End of Program")
