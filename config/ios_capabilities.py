from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

IOS_CAPABILITIES = {
    "platformName": "iOS",
    "appium:deviceName": "iPhone 13",
    "appium:platformVersion": "15.4",
    "appium:orientation": "PORTRAIT",
    "appium:automationName": "XCUITest",
    "appium:app": str(ROOT_DIR / "apps" / "ios.demo.app.zip"),
    "appium:newCommandTimeout": 240,
}
