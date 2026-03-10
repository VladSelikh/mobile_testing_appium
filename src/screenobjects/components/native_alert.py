from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NativeAlert:
    ANDROID = {
        "ALERT_TITLE": (
            AppiumBy.XPATH,
            '*//android.widget.TextView[@resource-id="com.wdiodemoapp:id/alert_title"]',
        ),
        "ALERT_MESSAGE": (
            AppiumBy.XPATH,
            '*//android.widget.TextView[@resource-id="android:id/message"]',
        ),
        "ALERT_BUTTON": '*//android.widget.Button[@text="{BUTTON_TEXT}"]',
    }

    IOS = {
        "ALERT": (
            AppiumBy.IOS_PREDICATE,
            "type == 'XCUIElementTypeAlert'",
        )
    }

    def __init__(self, driver):
        self.driver = driver

    @property
    def is_android(self):
        return str(self.driver.capabilities.get("platformName", "")).lower() == "android"

    @property
    def is_ios(self):
        return str(self.driver.capabilities.get("platformName", "")).lower() == "ios"

    def wait_for_displayed(self, is_shown=True, timeout=11):
        locator = self.ANDROID["ALERT_TITLE"] if self.is_android else self.IOS["ALERT"]
        wait = WebDriverWait(self.driver, timeout)

        if is_shown:
            return wait.until(EC.visibility_of_element_located(locator))
        return wait.until_not(EC.visibility_of_element_located(locator))

    def tap_on_button_with_text(self, text: str):
        if self.is_android:
            button_locator = (
                AppiumBy.XPATH,
                self.ANDROID["ALERT_BUTTON"].replace(
                    "{BUTTON_TEXT}", text.upper()),
            )
        else:
            button_locator = (AppiumBy.ACCESSIBILITY_ID, text)

        self.driver.find_element(*button_locator).click()

    def text(self) -> str:
        if self.is_ios:
            return self.driver.find_element(*self.IOS["ALERT"]).text

        title = self.driver.find_element(*self.ANDROID["ALERT_TITLE"]).text
        message = self.driver.find_element(*self.ANDROID["ALERT_MESSAGE"]).text
        return f"{title}\n{message}"
