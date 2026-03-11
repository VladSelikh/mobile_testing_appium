from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

IOS_CAPABILITIES = {
    "platformName": "iOS",
    # Specify your device name and platform version here.
    "appium:deviceName": "iPhone 17",
    "appium:platformVersion": "26.3",
    
    "appium:orientation": "PORTRAIT",
    "appium:automationName": "XCUITest",
    "appium:app": str(ROOT_DIR / "apps" / "ios.demo.app.zip"),
    "appium:newCommandTimeout": 240,
}
