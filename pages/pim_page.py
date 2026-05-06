from selenium.webdriver.common.by import By
#from base.base_page import BasePage
from pages.login_page import LoginPage

class PIMPage(LoginPage):
    # Locators
    PIM_OPTION = (By.XPATH, "//span[normalize-space()='PIM']")
    EMP_ID = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(2) > div > div:nth-child(2) > input")
    SEARCH = (By.XPATH, "//button[@type='submit']")
    RESET = (By.XPATH, "//button[normalize-space()='Reset']")
    
    #Actions
    def click_pim(self):
        self.click(self.PIM_OPTION)

    def is_page_loaded(self):
        return self.driver.find_element(*self.SEARCH).is_displayed()

    def pim_search_emp(self, emp_id):
        self.enter_text(self.EMP_ID, emp_id) # We have to enter value as 777 here
        self.click(self.SEARCH)

    def reset_search(self):
        self.click(self.RESET)
