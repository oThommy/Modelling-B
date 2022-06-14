const path = require('path');
const fs = require('fs');
const { error } = require('console');

console.log(fs.existsSync(path.join(__dirname, '..', 'out/algo-performance-ranking')))
console.log('hoi')