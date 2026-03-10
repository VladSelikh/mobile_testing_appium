from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

ANDROID_CAPABILITIES = {
    "platformName": "Android",
    "appium:deviceName": "Medium Phone API 36.1",
    "appium:platformVersion": "16.0",
    "appium:orientation": "PORTRAIT",
    "appium:automationName": "UiAutomator2",
    "appium:app": str(ROOT_DIR / "apps" / "android.demo.apk"),
    "appium:appWaitActivity": "com.wdiodemoapp.MainActivity",
    "appium:newCommandTimeout": 240,
}
