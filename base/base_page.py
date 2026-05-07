from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # Common method available to ALL pages
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except EC.NoSuchElementException:
            return False

    @abstractmethod # Every subclass must implement this method
    def is_page_loaded(self):
        pass