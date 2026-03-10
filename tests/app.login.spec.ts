import TabBar from '../src/screenobjects/components/tabBar.js';
import LoginScreen from '../src/screenobjects/LoginScreen.js';
import NativeAlert from '../src/screenobjects/components/nativeAlert.js';

const username = 'test_user@gmail.com';
const password = 'Test1234!';

describe('WebdriverIO and Appium, when interacting with a login form,', () => {
  beforeEach(async () => {
    await TabBar.waitForTabBarShown();
    await TabBar.openLogin();
    await LoginScreen.waitForDisplayed(true);
  });

  it('should be able to login successfully', async () => {
    await LoginScreen.tapOnLoginContainerButton();
    await LoginScreen.submitLoginForm({ username, password });
    await NativeAlert.waitForDisplayed();
    expect(await NativeAlert.text()).toContain('Success');

    await NativeAlert.topOnButtonWithText('OK');
    await NativeAlert.waitForDisplayed(false);
  });

  it('should be able to sign up successfully', async () => {
    await LoginScreen.tapOnSignUpContainerButton();
    await LoginScreen.submitSignUpForm({ username, password });
    await NativeAlert.waitForDisplayed();
    expect(await NativeAlert.text()).toContain('Signed Up');

    await NativeAlert.topOnButtonWithText('OK');
    await NativeAlert.waitForDisplayed(false);
  });
});
