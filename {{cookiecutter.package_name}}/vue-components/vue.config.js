const path = require('path');
const DST_PATH = '../{{cookiecutter.import_name}}/module/serve';

module.exports = {
  outputDir: path.resolve(__dirname, DST_PATH),
};
