from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ADMIN_OPTION = (By.XPATH,"//a[normalize-space()='']")

    def is_page_loaded(self):
        try:
            is_visible = self.driver.find_element(*self.USERNAME).is_displayed()
            self.logger.info("Login page verified as loaded - Username field is visible")
            return is_visible
        except Exception as e:
            self.logger.error(f"Failed to verify login page loaded: {str(e)}")
            return False

    def login(self, username, password):
        self.logger.info(f"Starting login with username: {username}")
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        self.logger.info("Login action completed")