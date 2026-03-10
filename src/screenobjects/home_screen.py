from appium.webdriver.common.appiumby import AppiumBy

from src.screenobjects.app_screen import AppScreen

class HomeScreen(AppScreen):
    def __init__(self, driver):
        super().__init__(driver, (AppiumBy.ACCESSIBILITY_ID, "Home-screen"))
