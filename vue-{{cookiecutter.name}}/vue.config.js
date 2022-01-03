const path = require('path');
const DST_PATH = '../{{cookiecutter.name}}/html/module/serve';

module.exports = {
  outputDir: path.resolve(__dirname, DST_PATH),
  configureWebpack: {
    output: {
      libraryExport: 'default',
    },
  },
  transpileDependencies: [],
};
