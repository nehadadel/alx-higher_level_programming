#!/usr/bin/node
function factorial (x) {
  if (isNaN(x)) {
    return 1;
  }
  if (x === 1 || x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
const process = require('process');
console.log(factorial(parseInt(process.argv[2])));
