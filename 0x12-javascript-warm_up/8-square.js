#!/usr/bin/node
const process = require('process');
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
