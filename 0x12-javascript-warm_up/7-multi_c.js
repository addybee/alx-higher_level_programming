#!/usr/bin/node

const { argv } = require('node:process');
const ans = parseInt(argv[2], 10);
if (!ans) console.log('Missing number of occurrences');
else {
  const languages = 'C is fun';
  for (let index = 0; index < ans; index++) console.log(languages);
}
