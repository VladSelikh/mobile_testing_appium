import pytest

from src.screenobjects.components.tab_bar import TabBar
from src.screenobjects.login_screen import LoginScreen
from src.screenobjects.components.native_alert import NativeAlert

from config.env import USERNAME, PASSWORD

@pytest.fixture
def login_page(driver):
    tab_bar = TabBar(driver)
    login_screen = LoginScreen(driver)
    native_alert = NativeAlert(driver)

    tab_bar.wait_for_tab_bar_shown()
    tab_bar.open_login()
    login_screen.wait_for_displayed(True)

    return {
        "tab_bar": tab_bar,
        "login_screen": login_screen,
        "native_alert": native_alert,
    }


def test_should_be_able_to_sign_up_successfully(login_page):
    login_screen = login_page["login_screen"]
    native_alert = login_page["native_alert"]

    login_screen.tap_on_sign_up_container_button()
    login_screen.submit_sign_up_form(USERNAME, PASSWORD)

    native_alert.wait_for_displayed()
    assert "Signed Up" in native_alert.text()

    native_alert.tap_on_button_with_text("OK")
    native_alert.wait_for_displayed(False)


def test_should_be_able_to_login_successfully(login_page):
    login_screen = login_page["login_screen"]
    native_alert = login_page["native_alert"]

    login_screen.tap_on_login_container_button()
    login_screen.submit_login_form(USERNAME, PASSWORD)

    native_alert.wait_for_displayed()
    assert "Success" in native_alert.text()

    native_alert.tap_on_button_with_text("OK")
    native_alert.wait_for_displayed(False)
