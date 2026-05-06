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
    @pytest.mark.parametrize("emp_id", [(row["emp_id"]) for _, row in data.iterrows()])
    def test_pim(self, driver, emp_id):
        #driver.get(base_url)
        pim_page = PIMPage()
        pim_page.click_pim()
        pim_page.is_page_loaded()
        sleep(5)
        pim_page.pim_search_emp(emp_id)
        sleep(5)
        pim_page.reset_search()
