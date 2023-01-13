const yaml = require('yaml')
const fs = require('fs')

const file = fs.readFileSync(process.argv[2], 'utf8')
const doc = yaml.parse(file)

console.log(JSON.stringify(doc).length)
