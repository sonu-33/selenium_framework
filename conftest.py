import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.custom_logger import get_logger

@pytest.fixture(scope="session") # defines a session-scoped fixture named logger
def logger(): # any test can request logger and get the same logging object
    return get_logger() # get_logger() creates a logger once per test session

@pytest.fixture(scope="session")  
def driver(): # defines driver fixture
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # starts Chrome browser once per session
    driver.maximize_window() # maximizes the browser window
    yield driver  # yields the browser object to tests
    driver.quit() # closes the browser after all tests finish