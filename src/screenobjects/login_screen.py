from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.helpers.utils import hide_keyboard
from src.screenobjects.app_screen import AppScreen


class LoginScreen(AppScreen):
    SCREEN = (AppiumBy.ACCESSIBILITY_ID, "Login-screen")

    def __init__(self, driver):
        super().__init__(driver, self.SCREEN)
        self.driver = driver

    @property
    def screen(self):
        return self.driver.find_element(*self.SCREEN)

    @property
    def login_container_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-login-container")

    @property
    def sign_up_container_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-sign-up-container")

    @property
    def login_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-LOGIN")

    @property
    def sign_up_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-SIGN UP")

    @property
    def email(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "input-email")

    @property
    def password(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "input-password")

    @property
    def repeat_password(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "input-repeat-password")

    @property
    def biometric_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-biometric")

    def tap_on_login_container_button(self):
        self.login_container_button.click()

    def tap_on_sign_up_container_button(self):
        self.sign_up_container_button.click()

    def _scroll_to_element_android(self, accessibility_id: str):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{accessibility_id}"))',
        )

    def submit_login_form(self, username: str, password: str):
        self.email.send_keys(username)
        self.password.send_keys(password)

        hide_keyboard(self.driver, "Login-screen")

        if str(self.driver.capabilities.get("platformName", "")).lower() == "android":
            self._scroll_to_element_android("button-LOGIN")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "button-LOGIN"))
        ).click()

    def submit_sign_up_form(self, username: str, password: str):
        self.email.send_keys(username)
        self.password.send_keys(password)
        self.repeat_password.send_keys(password)

        hide_keyboard(self.driver, "Login-screen")

        if str(self.driver.capabilities.get("platformName", "")).lower() == "android":
            self._scroll_to_element_android("button-SIGN UP")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "button-SIGN UP"))
        ).click()
