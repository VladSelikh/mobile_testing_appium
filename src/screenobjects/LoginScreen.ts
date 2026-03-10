import { hideKeyboard } from '../helpers/utils.js';
import AppScreen from './AppScreen.js';

const SELECTORS = {
  SCREEN: '~Login-screen',
};

class LoginScreen extends AppScreen {
  constructor() {
    super(SELECTORS.SCREEN);
  }

  get screen() {
    return $(SELECTORS.SCREEN);
  }
  private get loginContainerButton() {
    return $('~button-login-container');
  }
  private get signUpContainerButton() {
    return $('~button-sign-up-container');
  }
  private get loginButton() {
    return $('~button-LOGIN');
  }
  private get signUpButton() {
    return $('~button-SIGN UP');
  }
  private get email() {
    return $('~input-email');
  }
  private get password() {
    return $('~input-password');
  }
  private get repeatPassword() {
    return $('~input-repeat-password');
  }
  private get biometricButton() {
    return $('~button-biometric');
  }

  async tapOnLoginContainerButton() {
    await this.loginContainerButton.click();
  }

  async tapOnSignUpContainerButton() {
    await this.signUpContainerButton.click();
  }

  async submitLoginForm({
    username,
    password,
  }: {
    username: string;
    password: string;
  }) {
    await this.email.setValue(username);
    await this.password.setValue(password);

    await hideKeyboard(SELECTORS.SCREEN);
    await this.loginButton.scrollIntoView({
      scrollableElement: this.screen,
    });
    await this.loginButton.click();
  }

  async submitSignUpForm({
    username,
    password,
  }: {
    username: string;
    password: string;
  }) {
    await this.email.setValue(username);
    await this.password.setValue(password);
    await this.repeatPassword.setValue(password);

    await hideKeyboard(SELECTORS.SCREEN);
    await this.signUpButton.scrollIntoView({
      scrollableElement: this.screen,
    });
    await this.signUpButton.click();
  }
}

export default new LoginScreen();
