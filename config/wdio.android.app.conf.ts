import { join } from 'path';
import config from './wdio.shared.local.appium.conf';

config.capabilities = [
  {
    platformName: 'Android',
    'wdio:maxInstances': 1,
    'appium:deviceName': 'Medium Phone API 36.1',
    'appium:platformVersion': '16.0',
    'appium:orientation': 'PORTRAIT',
    'appium:automationName': 'UiAutomator2',
    'appium:app': join(process.cwd(), './apps/android.demo.apk'),
    'appium:appWaitActivity': 'com.wdiodemoapp.MainActivity',
    'appium:newCommandTimeout': 240,
  },
];

exports.config = config;
