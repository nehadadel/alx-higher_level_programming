#!/usr/bin/node
const process = require('process');
if (isNaN(process.argv[2]) || (process.argv.length === 3)) {
  console.log('0');
} else {
  const arr = process.argv.slice(2);
  arr.sort(function (a, b) { return a - b; });
  arr.reverse();

  console.log(arr[1]);
}
