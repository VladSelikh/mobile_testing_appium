export async function hideKeyboard(selectorToTapOn: string) {
  if (await driver.isKeyboardShown()) {
    await $(selectorToTapOn).click();
  }
}
