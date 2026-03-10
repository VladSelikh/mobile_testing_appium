from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TabBar:
    def __init__(self, driver):
        self.driver = driver

    def _tap(self, accessibility_id: str):
        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, accessibility_id).click()

    def open_home(self):
        self._tap("Home")

    def open_webview(self):
        self._tap("Webview")

    def open_login(self):
        self._tap("Login")

    def open_forms(self):
        self._tap("Forms")

    def open_swipe(self):
        self._tap("Swipe")

    def open_drag(self):
        self._tap("Drag")

    def wait_for_tab_bar_shown(self, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Home"))
        )
