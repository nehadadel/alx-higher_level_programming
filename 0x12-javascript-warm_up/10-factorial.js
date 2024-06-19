#!/usr/bin/node
function factorial (x) {
  if (isNaN(x)) {
    return NaN;
  }
  if (x === 1 || x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
const process = require('process');
console.log(factorial(parseInt(process.argv[2])));
