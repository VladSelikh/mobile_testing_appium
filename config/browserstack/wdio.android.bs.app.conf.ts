import { config } from '../wdio.shared.conf';

config.specs = ['./tests/**/app*.spec.ts'];

config.user = '';
config.key = '';
config.services = ['browserstack'];

config.capabilities = [
  {
    'appium:app': 'bs://8af20fc08312be0adf36abc6db343a139ca68885',
    'bstack:options': {
      // Set your BrowserStack config
      debug: true,

      // Specify device and os_version for testing
      device: 'Google Pixel 3',
      os_version: '9.0',

      // Set other BrowserStack capabilities
      projectName: 'wdio-test-project',
      buildName: 'android',
      sessionName: 'wdio-test',
    },
  },
];

exports.config = config;
