from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def is_page_loaded(self):
        return self.driver.find_element(*self.USERNAME).is_displayed()

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)