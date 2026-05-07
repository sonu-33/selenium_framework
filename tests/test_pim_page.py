from time import sleep

import pytest
from pages.pim_page import PIMPage
from utilities.read_properties import ReadConfig
import pandas as pd
import os

# Read config for fixed settings
base_url = ReadConfig.get_base_url()    # From config.ini
browser = ReadConfig.get_browser()      # From config.ini

# Read test data from Excel
#data = pd.read_excel("testdata/login_data.xlsx")

test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "testdata", "pim_data.xlsx")
data = pd.read_excel(test_data_path)

class TestPim:
    def test_pim(self, driver):
        driver.get(base_url)
        pim_page = PIMPage(driver)
        pim_page.click_pim() # This is Passed ✅

    @pytest.mark.parametrize("emp_id", [str(int(row["emp_id"])) for _, row in data.iterrows()])
    def test_pim_search(self, driver, emp_id):
        pim_search = PIMPage(driver)
        pim_search.is_page_loaded() # This is Passed ✅
        pim_search.pim_search_emp(emp_id) # This is Passed ✅


    def test_pim_reset(self, driver):
        pim_reset = PIMPage(driver)
        pim_reset.is_reset_present() # This is Passed ✅
        pim_reset.reset_search() # This is Passed ✅

