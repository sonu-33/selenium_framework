import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.custom_logger import get_logger

@pytest.fixture(scope="session") # defines a session-scoped fixture named logger
def logger(): # any test can request logger and get the same logging object
    return get_logger() # get_logger() creates a logger once per test session

@pytest.fixture(scope="session")  
def driver(): # defines driver fixture
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # starts Chrome browser once per session
    driver.maximize_window() # maximizes the browser window
    yield driver  # yields the browser object to tests
    driver.quit() # closes the browser after all tests finish

# Hook to capture screenshot on EVERY test (passed and failed)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":  # ✅ Removed "and report.failed" to capture all outcomes
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # ✅ Include pass/fail status in filename for easy identification
            status = "PASSED" if report.passed else "FAILED"
            screenshot_filename = f"{item.name}_{status}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)

            try:
                driver.save_screenshot(screenshot_path)

                if not hasattr(report, "extras"):
                    report.extras = []
                report.extras.append(pytest_html.extras.image(screenshot_path))

            except Exception as e:
                print(f"Screenshot failed for {item.name}: {e}")