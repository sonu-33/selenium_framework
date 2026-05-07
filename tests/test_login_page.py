import pytest
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
import pandas as pd
import os


# Read config for fixed settings
base_url = ReadConfig.get_base_url()    # From config.ini
browser = ReadConfig.get_browser()      # From config.ini

# Read test data from Excel
#data = pd.read_excel("testdata/login_data.xlsx")

test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "testdata", "login_data.xlsx")
data = pd.read_excel(test_data_path)

class TestLogin:
    @pytest.mark.parametrize("username, password, expected", [(row["username"], row["password"], row["expected"]) for _, row in data.iterrows()])
    def test_login(self, driver, logger, username, password, expected):
        logger.info(f"Starting login test for username={username} expected={expected}")
        driver.get(base_url)           # From config.ini ✅
        logger.info(f"Opened URL: {base_url}")
        login_page = LoginPage(driver)
        login_page.login(username, password)  # From Excel ✅
        logger.info("Login form submitted")
