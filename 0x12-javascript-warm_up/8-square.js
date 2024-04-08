#!/usr/bin/node

const { argv } = require('node:process');
const ans = parseInt(argv[2], 10);
if (!ans) console.log('Missing size');
else {
  for (let height = 0; height < ans; height++) {
    let len = '';
    for (let width = 0; width < ans; width++) {
      len += 'X';
    }
    console.log(len);
  }
}
