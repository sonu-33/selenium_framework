from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.custom_logger import get_logger

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.logger = get_logger()

    # Common method available to ALL pages
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on element with locator: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click on element {locator}: {str(e)}")
            raise

    def enter_text(self, locator, text):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.send_keys(text)
            self.logger.info(f"Entered text '{text}' into element with locator: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to enter text into element {locator}: {str(e)}")
            raise

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element found with locator: {locator}")
            return True
        except Exception as e:
            self.logger.warning(f"Element not found with locator {locator}: {str(e)}")
            return False

    @abstractmethod # Every subclass must implement this method
    def is_page_loaded(self):
        pass