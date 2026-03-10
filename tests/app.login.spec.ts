import TabBar from '../screenobjects/components/TabBar.js';
import LoginScreen from '../screenobjects/LoginScreen.js';
import NativeAlert from '../screenobjects/components/NativeAlert.js';

describe('WebdriverIO and Appium, when interacting with a login form,', () => {
  beforeEach(async () => {
    await TabBar.waitForTabBarShown();
    await TabBar.openLogin();
    await LoginScreen.waitForIsShown(true);
  });

  it('should be able login successfully', async () => {
    await LoginScreen.tapOnLoginContainerButton();
    await LoginScreen.submitLoginForm({ username: 'test@webdriver.io', password: 'Test1234!' });
    await NativeAlert.waitForDisplayed();
    expect(await NativeAlert.text()).toContain('Success');

    await NativeAlert.topOnButtonWithText('OK');
    await NativeAlert.waitForDisplayed(false);
  });

  it('should be able sign up successfully', async () => {
    await LoginScreen.tapOnSignUpContainerButton();
    await LoginScreen.submitSignUpForm({ username: 'test@webdriver.io', password: 'Test1234!' });
    await NativeAlert.waitForDisplayed();
    expect(await NativeAlert.text()).toContain('Signed Up');

    await NativeAlert.topOnButtonWithText('OK');
    await NativeAlert.waitForDisplayed(false);
  });
});
