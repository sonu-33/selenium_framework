import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")  # Changed from default "function" to "session"
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver  # Same browser instance shared across ALL tests
    driver.quit() # Browser closes only after ALL tests are done