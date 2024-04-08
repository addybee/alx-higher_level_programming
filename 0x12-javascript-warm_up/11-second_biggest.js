#!/usr/bin/node

const { argv } = require('node:process');

if (!argv[2]) console.log(0);
else if (!argv[3]) console.log(0);
else {
  const newArr = [];

  for (let i = 2; i < argv.length; i++) {
    newArr.push(parseInt(argv[i]));
  }
  newArr.sort((a, b) => b - a);
  console.log(newArr[1]);
}
