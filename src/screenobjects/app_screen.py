from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppScreen:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def wait_for_displayed(self, is_shown=True, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        if is_shown:
            return wait.until(EC.visibility_of_element_located(self.locator))
        return wait.until_not(EC.visibility_of_element_located(self.locator))
