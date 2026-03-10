import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from config.android_capabilities import ANDROID_CAPABILITIES
from config.ios_capabilities import IOS_CAPABILITIES


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        choices=["android", "ios"],
        help="Platform to run tests on: android or ios",
    )
    parser.addoption(
        "--appium-url",
        action="store",
        default="http://127.0.0.1:4723",
        help="Appium server URL",
    )

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")


@pytest.fixture(scope="session")
def driver(platform, request):
    appium_url = request.config.getoption("--appium-url")

    if platform == "android":
        options = UiAutomator2Options().load_capabilities(ANDROID_CAPABILITIES)
    else:
        options = XCUITestOptions().load_capabilities(IOS_CAPABILITIES)

    driver = webdriver.Remote(
        command_executor=appium_url,
        options=options,
    )

    yield driver
    driver.quit()
