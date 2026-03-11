def hide_keyboard(driver, selector_to_tap_on: str):
    try:
        if driver.is_keyboard_shown():
            driver.find_element("accessibility id", selector_to_tap_on).click()
    except Exception:
        return
