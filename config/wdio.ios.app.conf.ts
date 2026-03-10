import { join } from 'path';
import config from './wdio.shared.local.appium.conf';

config.capabilities = [
  {
    platformName: 'iOS',
    'wdio:maxInstances': 1,
    'appium:deviceName': 'iPhone 13',
    'appium:platformVersion': '15.4',
    'appium:orientation': 'PORTRAIT',
    'appium:automationName': 'XCUITest',
    'appium:app': join(
      process.cwd(),
      './apps/ios.demo.app.zip',
    ),
    'appium:newCommandTimeout': 240,
  },
];

exports.config = config;
