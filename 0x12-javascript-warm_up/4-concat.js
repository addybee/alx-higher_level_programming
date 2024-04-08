#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] && argv[3]) {
  const result = argv[2] + ' is ' + argv[3];
  console.log(result);
}
