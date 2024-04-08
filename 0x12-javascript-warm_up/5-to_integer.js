#!/usr/bin/node

const { argv } = require('node:process');

const ans = parseInt(argv[2], 10);
if (ans) console.log('My number: ' + ans);
else console.log('Not a number');
