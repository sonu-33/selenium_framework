from selenium.webdriver.common.by import By
#from pages.login_page import LoginPage
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class PIMPage(BasePage):
    # Locators
    PIM_OPTION = (By.XPATH, "//span[normalize-space()='PIM']")
    PIM_HEADER = (By.XPATH, "//h6[normalize-space()='PIM']")
    #EMP_ID = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(2) > div > div:nth-child(2) > input")
    EMP_ID = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    SEARCH = (By.XPATH, "//button[@type='submit']")
    RESET = (By.XPATH, "//button[normalize-space()='Reset']")

    #Actions
    def click_pim(self):
        self.click(self.PIM_OPTION) # This is Passed ✅

    def is_page_loaded(self):
        return self.is_element_present(self.PIM_HEADER) # This is Passed ✅

    def pim_search_emp(self, emp_id):
        self.enter_text(self.EMP_ID, emp_id) # This is Passed ✅
        self.click(self.SEARCH)

    def is_reset_present(self):
        return self.is_element_present(self.RESET)

    def reset_search(self):
        self.click(self.RESET)
        print("Reset search completed")
