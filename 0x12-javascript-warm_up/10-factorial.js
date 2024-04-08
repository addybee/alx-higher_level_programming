#!/usr/bin/node

const { argv } = require('node:process');
const num = parseInt(argv[2]);

function factorial (no) {
  let result = 0;
  if (!no || no < 0) return (1);
  result = no * factorial(no - 1);
  return result;
}

console.log(factorial(num));
