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
    @pytest.mark.parametrize("emp_id, expected", [(row["emp_id"], row["expected"]) for _, row in data.iterrows()])
    def test_pim(self, driver, emp_id, expected):
        #driver.get(base_url)           # From config.ini ✅
        pim_page = PIMPage(driver)
        pim_page.pim_search_emp(emp_id)  # From Excel ✅
