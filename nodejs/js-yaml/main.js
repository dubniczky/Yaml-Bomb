const yaml = require('js-yaml')
const fs = require('fs')

const file = fs.readFileSync(process.argv[2], 'utf8')
const doc = yaml.load(file)

console.log(JSON.stringify(doc).length)
